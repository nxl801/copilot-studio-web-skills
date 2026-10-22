# Copilot Studio Web Skills Suite

一套交付给 agent 的中文网页操作技能。覆盖 Copilot Studio、Power Automate、Power Apps，以及 Power Platform 跨环境部署。

**建议采用套件。当前已交付 5 个 skill。** 各产品独立维护操作手册，共用浏览器规则和任务记录。选择理由见 [架构分析](docs/architecture.md)。

版本：`0.1.0`。官方资料核查基线：`2026-10-22`。这是文档验证版；真实租户验收状态见 [验证报告](docs/validation-report.md)。

## 从哪里开始

- 首次使用：读 [入门指南](docs/getting-started.md)。
- 查看每项操作的手册：[操作索引](docs/operations-index.md)。
- 查看微软依据：[研究资料](docs/research/README.md)。
- 准备试点：[验收与维护](docs/testing-and-maintenance.md)。

## 五个 skill

| Skill | 负责的任务 |
|---|---|
| [power-platform-web](skills/power-platform-web/SKILL.md) | 跨产品任务入口、浏览器操作约定、上下文交接 |
| [copilot-studio-web](skills/copilot-studio-web/SKILL.md) | 创建 agent、知识、主题、工具、认证、测试和渠道发布 |
| [power-automate-web](skills/power-automate-web/SKILL.md) | 云端流程、agent 调用、连接、测试与运行排障 |
| [power-apps-web](skills/power-apps-web/SKILL.md) | Canvas / Model-driven 应用、数据、流程、发布和共享 |
| [power-platform-release](skills/power-platform-release/SKILL.md) | Solution、依赖、环境迁移、现有部署管道、恢复 |

直接调用产品 skill 也可以。总入口不是每次必经步骤。五个目录必须同级安装，因为它们引用同一份共享规则。

## 安装

需要支持本地 `SKILL.md` 的 agent，以及可以观察和操作已登录页面的浏览器工具。skill 不会自动提供工具、微软许可证或租户权限。

在解压后的根目录执行。安装辅助工具只需要 Python 3.9 或更新版本。

```sh
python3 scripts/suite.py validate
python3 scripts/suite.py install --dest "$HOME/.agents/skills" --dry-run
python3 scripts/suite.py install --dest "$HOME/.agents/skills"
```

上述是 Codex 当前官方支持的用户目录示例。其他 agent 使用其文档指定目录；通过 `--dest` 指定即可。安装程序拒绝覆盖同名目录。更新时先备份原目录，再明确移出旧版，不把两版文件混合。首次安装后，按运行时说明重新发现技能；如果列表中未出现，重新打开会话并检查路径。目录依据：[官方 skill 文档](https://learn.chatgpt.com/docs/build-skills)。

本次交付不自动安装到你的全局目录，也不修改微软租户。安装详情和第一次网页任务见 [入门指南](docs/getting-started.md)。

ZIP 是套件交付包，需要先解压并按目录安装。不要把它作为单个 skill 上传到 Copilot Studio；产品内部的 agent skills 与本套件用途不同。仅支持能读取同级 skill 引用的本地运行环境。

## 使用示例

```text
使用 $copilot-studio-web。
在我已登录的 Contoso 租户 DEV 环境，修改“差旅助手”的说明和指定知识源。
先核对环境及 agent 链接。只保存草稿，不发布。
完成后给出对象链接、保存状态和测试结果；未运行的检查单独列出。
```

```text
使用 $power-platform-web。
在 DEV 环境为“差旅助手”增加费用查询流程，并让现有 Power Apps 应用调用查询逻辑。
只使用我指定的测试数据。允许开发环境内发布和测试，不部署生产。
保持各调用方所需的触发器，分别验证调用结果。
```

## 已覆盖与边界

主要操作手册覆盖 Copilot Studio standard harness。GitHub Copilot harness 提供体验识别、基础知识与 Preview 分支；复杂工作流和完整部署未承诺覆盖。两种框架不能混用菜单或计费假设。

SharePoint、Teams、Entra 和 Dataverse 作为集成依赖处理。完整租户治理、Power Pages、Desktop flow、Azure 和 Dynamics 365 管理不在本版范围内。详细范围见 [操作索引](docs/operations-index.md)。

此套件是操作知识与验证规则，不是固定选择器的无人值守自动化程序。需要身份验证、管理员同意或缺少关键授权时，agent 会保留当前结果并指出具体阻塞。

## 本项目账号约束

Copilot SDK、copilot-bridge、Gateway `copilot.agent_turn` 只可使用 `SESA461332_seemu` 计费，不能用 `nxl801` 消耗 Copilot tokens。项目 push/PR 使用 `nxl801`。微软网页租户身份单独核查。本套件不包含 runner、token 或认证配置；[共享操作约定](skills/power-platform-web/references/browser-contract.md)保留这些约束。

## 目录与交付

```text
skills/       五个 skill 及按需操作参考
docs/         入门、设计、研究、验收与维护
scripts/      结构检查、安装、打包
tests/        交付工具的本地行为测试
suite.json    套件名称、版本和技能清单
dist/         可交付 ZIP 与 SHA-256 校验值
```

重新生成交付包：

```sh
python3 scripts/suite.py validate
python3 -m unittest discover -s tests -v
python3 scripts/suite.py package --output dist
```

打包范围为上述源文件及文档，不包含浏览器会话、租户导出包或凭据。验证报告说明实际执行了哪些检查。
