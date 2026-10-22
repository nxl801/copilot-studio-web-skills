# 入门指南

## 1. 准备运行条件

准备一个能读取本地 skill 且能控制浏览器的 agent。浏览器至少需支持：读取可见界面、点击、输入、选择标签、等待状态，以及任务需要时的文件上传/下载。

用户在浏览器登录有权使用的微软工作账号。MFA 是额外的身份验证步骤；需要时由用户完成。不要把密码或验证码发给 skill。

首个试点使用明确的开发/测试环境。确认该环境可见且有相应创建权限。许可证、容量与功能可用性以当前租户为准。不同产品所需权限可能不同；能创建 agent 不代表能给 Dataverse 表授权。

## 2. 安装整个套件

解压交付包。进入含 `suite.json` 的目录，执行：

```sh
python3 scripts/suite.py validate
python3 scripts/suite.py install --dest "$HOME/.agents/skills" --dry-run
python3 scripts/suite.py install --dest "$HOME/.agents/skills"
```

`--dry-run` 只检查并显示计划。正式安装复制全部五个 skill。程序发现任一同名目录时拒绝安装，不覆盖已有技能。

如果运行时不使用这个目录，将 `--dest` 改为它支持的目录。也可以人工复制 `skills/` 下的五个子目录；保持它们同级，不要只复制 `SKILL.md`。当前 Codex 用户目录依据：[官方文档](https://learn.chatgpt.com/docs/build-skills)。

安装后在 agent 的 skill 列表确认五个名称。只读安装文件不等于运行时已经发现它们。运行时没有自动发现时，可先显式要求读取对应 `SKILL.md`，但这不替代浏览器工具配置。

## 3. 第一次任务：只读确认

将以下请求交给 agent，并替换目标值：

```text
使用 $power-platform-web。
打开我已经登录的 Copilot Studio 页面。
仅查看，不创建或修改资源。
确认当前租户、环境、可见 agent，以及所用的运行框架。
告诉我哪些必要信息能从页面确认，哪些尚不能确认。
```

预期：agent 用真实页面确定目标上下文。它不能假装已创建对象，也不应要求你逐项重复页面上已有的信息。若缺少浏览器操作能力，应明确指出。

## 4. 第二次任务：创建可验证草稿

以下例子不需要 Power Automate，也不发布渠道：

```text
使用 $copilot-studio-web。
在 Contoso 的 DEV 环境，新建 standard harness agent“技能试点助手”。
用中文回答。仅说明这是内部试点，不添加知识源、外部工具或自动触发器。
保存草稿，并在测试面板确认欢迎与范围说明。
允许这次开发环境测试。不要发布或共享。
交付环境、agent 链接、保存状态和实际测试证据。
```

环境或框架入口不可用时，agent 应报告原因。它不能改用其他环境，或迁移现有对象来满足示例。

## 5. 增加产品协作

先选一个实际需要的分支。避免为了试用套件一次创建所有产品。

| 业务目标 | 调用 | 需要提供或从页面获取 |
|---|---|---|
| agent 查询列表并返回结果 | power-automate-web + copilot-studio-web | 列表、输入输出、连接身份、测试数据 |
| 给现有应用加查询按钮 | power-apps-web | 应用链接、控件/屏幕、流程及参数 |
| 部署到 TEST | power-platform-release | 源/目标环境、solution、版本、目标连接、是否发布 |

对于 solution-aware flow，未发布草稿当前不能运行测试。若你只允许草稿，验收应停在配置与静态检查。要验证真实调用，需要授权在指定开发环境发布并运行。见 [流程版本手册](../skills/power-automate-web/references/cloud-flows.md)。

## 6. 给出清楚的任务范围

不要求使用固定格式。只要说明目标、对象、环境和完成层级即可。例如：

```text
将 DEV 中已经测试的 Travel solution 1.2.0.0 部署到 TEST。
使用现有发布管道和已指定的 TEST 连接。
允许本次导入、启用所需流程、发布 agent，以及共享给 Travel-Pilot 组使用。
不改租户策略，不部署 PROD，不发送额外通知。
用已授权测试数据验证一次，并给出运行记录与目标渠道链接。
```

已有授权覆盖上述步骤时，agent 应持续完成，不重复询问统一审批。实际遇到新影响或管理员操作时，再询问缺失决定。

## 7. 阅读交付结果

交付记录应说明：实际对象、状态、证据、未验证项和阻塞。导入成功、发布成功与用户能使用是不同结论。

使用 [交付模板](../skills/power-platform-web/assets/delivery-record.md) 可统一复杂任务记录。需要正式试点验收时，按 [验收指南](testing-and-maintenance.md)执行。
