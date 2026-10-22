# 先识别页面体验

核验日期：2026-10-22。官方文档与租户界面可能分批更新。下列英文文字是定位提示，不是固定选择器。

## 识别顺序

1. 读取当前页面的产品名、环境选择器、对象名与页面链接。
2. 查找运行框架信息。若页面没有明示，结合可见导航与官方说明判断，并在任务记录注明依据。
3. 只切换编辑体验，不自动升级、转换或迁移已有 agent。新建任务若需要确定框架，用业务要求和渠道约束选择。

| 观察到的界面 | 可采用的路径 | 不应作出的推断 |
| --- | --- | --- |
| 现有 agent 有 Overview、Topics、Tools、Test，且对象属于 standard harness | 使用本 skill 的主操作手册 | “classic experience”不等于 classic orchestration；标准框架也支持生成式编排 |
| 首页有 Other ways to build 或菜单 Open classic experience | 用户要建 standard agent 时，可从这些入口进入 | 不能因此升级、复制或转换现有 agent |
| 新框架对象有 Build、Preview，以及知识/工作流组件 | 使用下方 GitHub Copilot harness 分支 | 不要寻找标准框架的 Topics 菜单并据此认定对象损坏 |
| Teams 精简版、Copilot Chat 或 Customer Conversation 专用创建入口 | 阅读该产品分支文档后继续 | 不套用标准网页版的完整能力列表 |

微软官方入口资料：[Start building](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/authoring-first-bot)、[访问标准框架](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/switch-experiences)、[框架比较](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/choose-harness)。官方页面仍同时出现旧的 New experience 开关说明与新的 Other ways to build 说明；以当前可见入口为准。

## GitHub Copilot harness：已研究的有限分支

本套件提供以下识别与基础操作。完整 workflow、skills、memory 和迁移流程不在当前操作手册覆盖范围。遇到这些任务，先沿官方链接读取对应说明；不能伪造按钮路径。

| 任务 | UI 锚点与输入 | 验证 | 失败处理 |
| --- | --- | --- | --- |
| 给已确认的新框架 agent 增加知识 | Build 的组件面板 → Knowledge → Add knowledge；选择用户指定来源 | 回读来源和访问范围，再在 Preview 提问 | 若实际界面提供独立 Knowledge 标签，用该标签；若来源不可用，查权限与框架支持 |
| 交互测试 | Preview；输入已授权的用例；需要隔离上下文时新建会话 | 检查答案、来源、工具调用及可见执行结果；End user preview 可检查用户视图 | 用可见工具错误定位；不要把测试动作当作无副作用 |
| 发布准备 | 检查保存的名称、说明、指令、知识和所需能力；完成 Preview | 留存草稿测试证据和目标渠道 | 发布前读取该框架当前发布步骤与渠道支持；不直接复用标准框架的渠道菜单 |

来源：[新增知识](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/knowledge-add-existing-copilot)、[Preview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/preview-overview)、[发布概览](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/publication-fundamentals-publish-channels)。上述知识文档的文字与导航说明存在混合，应先观察页面再定位。

## 计费与身份

GitHub Copilot harness 是 Copilot Studio 中的框架名称。它不表示网页通过本地 GitHub Copilot SDK 账号计费。微软说明其创建与运行活动可消耗 Copilot Credits，账单按环境和 agent 管理。核对实际 Microsoft 租户的容量及允许使用范围。[成本管理](https://learn.microsoft.com/en-us/power-platform/admin/manage-usage-github-copilot-harness)

若任务另行调用本地 Copilot SDK、copilot-bridge 或 Gateway `copilot.agent_turn`，遵守项目约定：仅使用 `SESA461332_seemu`，不得使用 `nxl801` 消耗 Copilot tokens。仓库 push/PR 使用 `nxl801`。这两类 GitHub 身份不替代 Microsoft 租户身份。
