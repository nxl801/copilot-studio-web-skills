"""File-delivery behavior tests. No browser, tenant, network or model invocation."""

import importlib.util
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location("suite", Path(__file__).parents[1] / "scripts" / "suite.py")
suite = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(suite)


class DeliveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "source"
        self.root.mkdir()
        for directory in ("docs", "scripts", "tests"):
            (self.root / directory).mkdir()
        data = {"name": "fixture-suite", "version": "0.1.0", "skills": ["alpha", "beta"]}
        (self.root / "suite.json").write_text(json.dumps(data))
        (self.root / "README.md").write_text("[alpha](skills/alpha/SKILL.md)\n")
        (self.root / ".gitignore").write_text("dist/\n")
        for name in data["skills"]:
            skill = self.root / "skills" / name
            (skill / "agents").mkdir(parents=True)
            (skill / "SKILL.md").write_text("---\nname: " + name + "\ndescription: A fixture skill\n---\nBody\n")
            (skill / "agents" / "openai.yaml").write_text('interface:\n  display_name: "Fixture"\n')

    def test_installs_all_skills_and_preserves_unrelated_files(self):
        target = self.base / "installed"
        target.mkdir()
        unrelated = target / "existing.txt"
        unrelated.write_text("keep")
        suite.install(self.root, target)
        for name in ("alpha", "beta"):
            self.assertEqual((target / name / "SKILL.md").read_bytes(), (self.root / "skills" / name / "SKILL.md").read_bytes())
        self.assertEqual(unrelated.read_text(), "keep")

    def test_conflict_refuses_entire_install_without_overwriting(self):
        target = self.base / "installed"
        (target / "beta").mkdir(parents=True)
        sentinel = target / "beta" / "custom.md"
        sentinel.write_text("user edit")
        with self.assertRaises(ValueError):
            suite.install(self.root, target)
        self.assertFalse((target / "alpha").exists())
        self.assertEqual(sentinel.read_text(), "user edit")

    def test_dry_run_does_not_create_destination(self):
        target = self.base / "dry"
        self.assertEqual(len(suite.install(self.root, target, True)), 2)
        self.assertFalse(target.exists())

    def test_copy_failure_removes_only_newly_created_directories(self):
        target = self.base / "installed"
        target.mkdir()
        sentinel = target / "unrelated.txt"
        sentinel.write_text("keep")
        with patch.object(suite.shutil, "copy2", side_effect=OSError("simulated disk failure")):
            with self.assertRaises(OSError):
                suite.install(self.root, target)
        self.assertEqual(list(target.iterdir()), [sentinel])

    def test_broken_runtime_dependency_is_rejected(self):
        entry = self.root / "skills" / "alpha" / "SKILL.md"
        entry.write_text(entry.read_text() + "[missing](../beta/missing.md)\n")
        with self.assertRaisesRegex(ValueError, "Broken"):
            suite.validate(self.root)

    def test_symlink_is_rejected(self):
        (self.root / "skills" / "alpha" / "external").symlink_to(self.base / "outside")
        with self.assertRaisesRegex(ValueError, "Symlink"):
            suite.validate(self.root)

    def test_package_is_reproducible_and_excludes_private_files(self):
        (self.root / "token.txt").write_text("not-a-real-token")
        evidence = self.root / "local-evidence"
        evidence.mkdir()
        (evidence / "session.txt").write_text("private fixture")
        archive, digest = suite.package(self.root, self.base / "out")
        _, second = suite.package(self.root, self.base / "out")
        self.assertEqual(digest, second)
        with zipfile.ZipFile(archive) as bundle:
            names = bundle.namelist()
            self.assertTrue(any(n.endswith("skills/alpha/SKILL.md") for n in names))
            self.assertFalse(any("token.txt" in n or "local-evidence" in n for n in names))
            self.assertIsNone(bundle.testzip())

    def test_manifest_cannot_escape_skill_directory(self):
        data = json.loads((self.root / "suite.json").read_text())
        data["skills"] = ["../escape"]
        (self.root / "suite.json").write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, "Invalid skill name"):
            suite.validate(self.root)


if __name__ == "__main__":
    unittest.main()
