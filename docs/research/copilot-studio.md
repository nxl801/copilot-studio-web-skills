# Copilot Studio 官方资料研究

研究日期：2026-10-22。研究范围是 agent 操作网页，不是 GitHub Copilot SDK。已打开并阅读下列微软官方页面；没有操作真实租户。流程尚需在目标租户做网页验收。

## 结论

建议单独设置 `copilot-studio-web` 产品 skill，并复用套件的浏览器、连接和发布规范。Copilot Studio 的对象编辑、编排、知识状态、认证与渠道有独立完成条件。把这些内容全部塞进通用 Microsoft 网页 skill，会使选择入口和判断完成状态更困难。这是本项目设计判断，不是微软发布的 skill 划分标准。

## 官方事实及设计影响

| 官方事实 | 对 skill 的影响 | 官方来源 |
| --- | --- | --- |
| 当前产品有多个 harness；标准框架与 GitHub Copilot harness 的编辑与运行能力不同 | 操作前识别对象，不能混用菜单；保留现有框架 | [框架比较](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/choose-harness) |
| 新首页提供不同创建入口；标准入口有 Other ways to build / Open classic experience | 根据可见 UI 定位，不能把旧开关写成唯一入口 | [开始构建](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/authoring-first-bot)、[标准体验入口](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/switch-experiences) |
| 标准 agent 的主要语言创建后不能更改 | 把语言选择放在创建前核对 | [创建 agent](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-first-bot) |
| 生成式与经典编排采用不同组件选择方式 | 主题说明、触发短语和工具可见性需按现有模式验证 | [生成式编排](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-generative-actions) |
| 仅写指令不会创建所引用的能力 | 先配置知识或工具，再引用并测试 | [编写指令](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-instructions) |
| 知识添加与知识可测试是两个状态 | 等待 Ready，并检查实际问答证据 | [添加知识](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-add-existing-copilot)、[测试知识](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-test) |
| agent 认证与工具使用的身份有不同配置 | 验证对话入口和外部数据权限两层边界 | [agent 认证](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configuration-end-user-authentication)、[工具认证](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-enduser-authentication) |
| 保存修改与发布为不同操作；发布会更新连接的渠道 | 交付需分别报告草稿、发布、分发与渠道验证 | [发布与渠道](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels) |
| 新框架的创建和运行活动可消耗 Copilot Credits | 不能将名称中的 GitHub 理解成本地 GitHub 账号计费 | [新框架成本](https://learn.microsoft.com/en-us/power-platform/admin/manage-usage-github-copilot-harness) |

## 关键版本差异

**同步与异步流程。** 标准接入资料仍要求同步响应和 100 秒动作限制。2026-10-17 更新的异步资料说明新基础设施环境可启用异步回调，且渠道支持不同。套件将两者作为条件分支，并要求验证环境能力与渠道结果。[标准流程接入](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flow-agent)、[异步响应](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flow-asynchronous-response)

**网页入口。** 官方旧创建页仍使用 New experience 开关说明，新入口页采用 Other ways to build。套件保留语义锚点并要求读取真实界面。页面更新日期不保证某个租户已经取得同一功能。

**产品中也有 skills。** 新框架内部的 agentic skills 与本仓库给外部 agent 使用的网页操作 skills 不同。不要把仓库打包文件自动上传到 Copilot Studio，也不要把 Azure Bot Service 的代码型 skills 混入本项目。

## 操作手册映射

| 产品工作 | 本地交付 | 补充官方手册 |
| --- | --- | --- |
| 创建、配置、知识、主题、工具、认证 | [配置操作](../../skills/copilot-studio-web/references/authoring.md) | [主题](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-create-edit-topics)、[工具](https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-tools-custom-agent)、[流程 FAQ](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-faqs) |
| 测试、发布、排障 | [测试与发布](../../skills/copilot-studio-web/references/testing-publishing.md) | [测试面板](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-test-bot)、[错误代码](https://learn.microsoft.com/en-us/troubleshoot/power-platform/copilot-studio/authoring/error-codes) |
| 框架和体验识别 | [体验识别](../../skills/copilot-studio-web/references/experience-detection.md) | [新框架 Preview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/preview-overview)、[新框架发布](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/publication-fundamentals-publish-channels) |

## 已知范围

- 标准框架提供从配置到发布的操作路径，但未声称已通过目标租户实测。
- GitHub Copilot harness 提供已研究的知识、Preview 与发布准备路径。完整 workflow、memory、内部 skills 和迁移流程需在执行时补充官方资料。
- Teams 精简版、主权云、Customer Conversation 和 Copilot Chat 的能力不自动等同于标准商业云网页版。
- 管理员策略、许可、容量、区域和分批开放会改变页面可用项。无法确认的能力应标记为待验证，而不是尝试关闭治理设置。
