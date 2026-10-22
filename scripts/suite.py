#!/usr/bin/env python3
"""Validate, install and package this local skill suite; no network or credentials."""

import argparse
import hashlib
import json
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
LINK = re.compile(r"\[[^\]]*\]\(([^\s)]+)\)")


def manifest(root):
    data = json.loads((root / "suite.json").read_text(encoding="utf-8"))
    names = data.get("skills", [])
    if not names or len(names) != len(set(names)):
        raise ValueError("Skill list is empty or contains duplicate names")
    if not all(isinstance(n, str) and NAME.fullmatch(n) for n in names):
        raise ValueError("Invalid skill name")
    if not NAME.fullmatch(data.get("name", "")):
        raise ValueError("Invalid suite name")
    if not re.fullmatch(r"\d+\.\d+\.\d+", data.get("version", "")):
        raise ValueError("Version must be major.minor.patch")
    return data


def source_files(root):
    """An allowlist prevents accidental delivery of local evidence or credentials."""
    paths = [root / "README.md", root / "suite.json", root / ".gitignore"]
    for directory in ("skills", "docs", "scripts", "tests"):
        base = root / directory
        if base.is_symlink():
            raise ValueError("Symlink is not permitted: " + directory)
        paths.extend(base.rglob("*"))
    files = []
    for path in paths:
        if path.is_symlink():
            raise ValueError("Symlink is not permitted: " + str(path.relative_to(root)))
        if "__pycache__" in path.parts or path.name == ".DS_Store":
            continue
        if path.is_file():
            files.append(path)
    return sorted(set(files))


def within(path, parent):
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def validate(root):
    root = root.resolve()
    data = manifest(root)
    actual = {p.name for p in (root / "skills").iterdir() if p.is_dir()}
    if actual != set(data["skills"]):
        raise ValueError("Skill directories do not match suite.json")
    for name in data["skills"]:
        entry = root / "skills" / name / "SKILL.md"
        content = entry.read_text(encoding="utf-8")
        front = re.match(r"\A---\n(.*?)\n---(?:\n|$)", content, re.S)
        if not front:
            raise ValueError("Missing frontmatter: " + name)
        fields = front.group(1)
        match = re.search(r"^name:\s*[\"']?([a-z0-9-]+)[\"']?\s*$", fields, re.M)
        if not match or match.group(1) != name:
            raise ValueError("Frontmatter name mismatch: " + name)
        if not re.search(r"^description:\s*\S.+$", fields, re.M):
            raise ValueError("Missing one-line description: " + name)
        if "[TODO:" in content:
            raise ValueError("Unfinished skill scaffold: " + name)
        if not (entry.parent / "agents" / "openai.yaml").is_file():
            raise ValueError("Missing UI metadata: " + name)
    files = source_files(root)
    for path in files:
        if path.suffix != ".md":
            continue
        for raw in LINK.findall(path.read_text(encoding="utf-8")):
            url = urlsplit(raw.strip("<>"))
            if url.scheme or url.netloc or not url.path:
                continue
            target = (path.parent / unquote(url.path)).resolve()
            if not within(target, root) or not target.exists():
                raise ValueError("Broken/escaping link: {} -> {}".format(path.relative_to(root), raw))
            if within(path, root / "skills") and not within(target, root / "skills"):
                raise ValueError("Runtime skill depends on uninstalled file: " + raw)
    return data, files


def install(root, destination, dry_run=False):
    data, _ = validate(root)
    destination = destination.expanduser().resolve()
    source = (root / "skills").resolve()
    if within(destination, source) or within(source, destination):
        raise ValueError("Install destination overlaps suite sources")
    conflicts = [n for n in data["skills"] if (destination / n).exists() or (destination / n).is_symlink()]
    if conflicts:
        raise ValueError("Refusing to overwrite: " + ", ".join(conflicts))
    if dry_run:
        return [str(destination / n) for n in data["skills"]]
    destination.mkdir(parents=True, exist_ok=True)
    created = []
    try:
        for name in data["skills"]:
            target = destination / name
            target.mkdir()  # Exclusive reservation: never reuse an existing directory.
            created.append(target)
            for child in (source / name).iterdir():
                if child.name == "__pycache__" or child.name == ".DS_Store":
                    continue
                if child.is_dir():
                    shutil.copytree(child, target / child.name, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"))
                else:
                    shutil.copy2(child, target / child.name)
    except Exception:
        for path in reversed(created):
            shutil.rmtree(path)
        raise
    return [str(p) for p in created]


def package(root, output):
    root = root.resolve()
    data, files = validate(root)
    output = output.expanduser().resolve()
    # Packaging inside an allowlisted source folder would package previous output.
    if any(within(output, (root / d).resolve()) for d in ("skills", "docs", "scripts", "tests")):
        raise ValueError("Package output must be outside source folders")
    output.mkdir(parents=True, exist_ok=True)
    stem = data["name"] + "-" + data["version"]
    archive = output / (stem + ".zip")
    with tempfile.TemporaryDirectory(dir=output) as staging:
        temporary = Path(staging) / archive.name
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
            for path in files:
                info = zipfile.ZipInfo(stem + "/" + path.relative_to(root).as_posix(), (2026, 10, 22, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                bundle.writestr(info, path.read_bytes())
        temporary.replace(archive)
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    (output / (archive.name + ".sha256")).write_text(digest + "  " + archive.name + "\n", encoding="utf-8")
    return archive, digest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("validate")
    setup = commands.add_parser("install")
    setup.add_argument("--dest", type=Path, required=True)
    setup.add_argument("--dry-run", action="store_true")
    pack = commands.add_parser("package")
    pack.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        root = args.root.resolve()
        if args.command == "validate":
            data, files = validate(root)
            print("Validated {} skills, {} source files; local links resolve.".format(len(data["skills"]), len(files)))
        elif args.command == "install":
            paths = install(root, args.dest, args.dry_run)
            print(("Plan only" if args.dry_run else "Installed") + ":\n" + "\n".join(paths))
        else:
            archive, digest = package(root, args.output)
            print(str(archive) + "\nSHA-256: " + digest)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print("Error: " + str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
