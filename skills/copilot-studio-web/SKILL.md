---
name: copilot-studio-web
description: 通过 Copilot Studio 网页创建和配置 agent、知识源、主题、工具及认证，执行测试和渠道发布。用于实际网页操作；不用于 GitHub Copilot SDK、IDE Copilot 或仅写提示词。
---

# Copilot Studio 网页操作

先识别当前 agent 的运行方式和页面体验，再执行对应流程。这里的 harness 是 agent 的运行框架；不同框架的配置入口和能力不同。

## 开始任务

1. 若本轮尚未读取，先读共享[浏览器操作约定](../power-platform-web/references/browser-contract.md)。按[任务记录](../power-platform-web/references/task-record.md)保留目标、状态和证据。
2. 记录租户、环境、agent 名称与链接。确认操作的是现有对象还是新对象。Microsoft 登录身份与 GitHub 计费账号是两回事。
3. 读[体验识别](references/experience-detection.md)。保留现有 agent 的 harness；不要为了套用菜单而迁移 agent。
4. 只读取当前任务需要的操作手册。

| 当前工作 | 读取内容 |
| --- | --- |
| 新建、改指令、加知识、编辑主题、连接工具、改认证 | [配置操作](references/authoring.md) |
| 测试、发布、渠道接入、错误定位 | [测试与发布](references/testing-publishing.md) |
| agent 调用流程、SharePoint、Dataverse 或其他产品协作 | [跨产品连接约定](../power-platform-web/references/integrations.md)；需要编辑 cloud flow 时读取 [power-automate-web](../power-automate-web/SKILL.md) |
| 跨环境迁移、Solution 导入导出或生产发布管理 | [power-platform-release](../power-platform-release/SKILL.md) |

## 执行边界

- 主操作手册覆盖 standard harness 的网页流程。GitHub Copilot harness 的有限分支见体验识别；未覆盖的功能先读对应官方文档，再依据真实页面操作。
- 把保存草稿、发布版本、配置渠道、授予用户访问分别记录。完成其中一项不代表其他项完成。
- 配置工具时检查实际连接身份。测试聊天也可能调用真实工具、发消息或写数据；测试执行范围沿用用户授权，不因入口叫 Test 而扩大。
- 先完成可审阅配置与验证。已有授权覆盖发布时直接继续；缺少目标环境、渠道或必要授权时，只暂停依赖该信息的步骤。
- 遇到数据策略或权限阻止，保存错误与所需管理员动作。不要关闭认证、换到个人连接或换环境来绕过限制。

## 完成条件

返回对象链接、目标环境、已保存的配置、测试结果和发布状态。对发布任务，再给出目标渠道的新会话验证结果。明确区分已验证、失败和未执行；没有真实网页证据时，不声称部署成功。
