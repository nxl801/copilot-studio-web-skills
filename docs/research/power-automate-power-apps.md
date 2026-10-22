# Power Automate 与 Power Apps 官方资料研究

核查日期：2026-10-22。仅研究公开文档，没有连接租户或执行应用、流程。下列链接均已打开阅读正文；部分 Learn 页面出现登录提示，但返回了公开正文。产品可能因地区、运行框架和租户发布批次而不同。

## 结论与技能边界

建议分别提供 `power-automate-web` 和 `power-apps-web`，让总入口按实际产品路由。这是本套件的设计判断。依据是两类产品的对象、运行入口和完成证据不同；一个“保存成功”规则不能覆盖两者。

- Power Automate 的主对象是触发器、动作、连接和运行实例。
- Power Apps 的主对象是应用、页面/组件、数据权限和已发布版本。
- 与 Copilot Studio 的集成需要独立检查输入输出契约、运行框架、流程可见性和调用证据。

具体操作已收敛到 [Power Automate skill](../../skills/power-automate-web/SKILL.md) 与 [Power Apps skill](../../skills/power-apps-web/SKILL.md)，此处不复制手册。

## 已核实的关键差异

| 事实 | 对技能设计的影响 | 官方来源 |
| --- | --- | --- |
| Solution-aware flow 有草稿和发布版本；草稿当前不能测试，solution 导出只带已发布版本 | 区分静态检查、运行验证与部署。授权只到草稿时不声称完成运行测试 | [Drafts and versioning](https://learn.microsoft.com/en-us/power-automate/drafts-versioning) |
| 流程可在 solution 内创建，也可添加已有流程；存在迁移限制 | 先定位原流程，再决定加入 solution，不复制同名对象规避问题 | [Create a flow in a solution](https://learn.microsoft.com/en-us/power-automate/create-flow-solution) |
| Connection 与 connection reference 不同；旧流程加入 solution 后不保证自动转换 | 将身份、连接、引用作为独立检查对象 | [Connection reference](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-connection-reference) |
| 标准框架的 agent flow 工具需要对应触发/响应并同步返回 | 使用标准分支约束；其他框架重新查兼容性 | [Create agent flow tool](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-flow-create) |
| 新基础设施提供有渠道限制的异步回调 | 与标准同步规则分开；按环境能力及目标渠道选择 | [Asynchronous response support](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flow-asynchronous-response) |
| 调用工具的测试应核验 agent 真正调用流程并返回结果 | 不能仅以工具出现在列表判成功 | [Call agent flow](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-use-flow) |
| Canvas 保存与发布不同；共享还需处理数据与依赖权限 | 将 Save、Publish、Share 分开验证 | [Save and publish](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/save-publish-app)、[Share canvas app](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/share-app) |
| Model-driven 应用按角色及 Dataverse 表权限共享 | 用业务身份验证数据范围，不能只测试作者账号 | [Share model-driven app](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/share-model-driven-app) |

## 操作手册入口

| 产品操作 | 微软官方手册 |
| --- | --- |
| 设计器和 Save/Test 区别 | [Cloud flows designer](https://learn.microsoft.com/en-us/power-automate/flows-designer) |
| 静态检查、手动测试、模拟、重提运行 | [Test cloud flows](https://learn.microsoft.com/en-us/power-automate/guidance/coding-guidelines/test-cloud-flows) |
| 查看运行历史 | [Cloud flow tutorial](https://learn.microsoft.com/en-us/power-automate/get-started-with-cloud-flows) |
| 连接、触发及动作错误 | [Troubleshoot cloud flow errors](https://learn.microsoft.com/en-us/power-automate/troubleshoot-flow-errors) |
| 复用流程供 agent 调用 | [Modify existing flow](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flow-modify-use-with-agent) |
| 新建 Canvas | [Create blank app](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/create-blank-app) |
| Canvas 数据连接 | [Add data connections](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/add-data-connection) |
| Canvas 与流程绑定 | [Power Automate pane](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/working-with-flows) |
| 新建模型驱动应用 | [Model-driven app designer](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-model-driven-app) |

## 尚需在用户环境验证

- 登录身份、环境权限、许可证与组织策略。
- 本租户实际呈现的设计器、运行框架和工具入口。
- 开发环境的最小端到端样例：一次应用交互或 agent 调用，对应一次流程运行与可查验业务结果。
- 发布和共享后，授权测试用户的访问结果。

这些项目属于验收工作，不属于已经完成的文档研究。
