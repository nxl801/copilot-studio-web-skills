# Copilot Studio 的流程工具

文档核查：2026-10-22。适用范围先看 agent 当前的运行框架与工具入口；不要把不同框架的异步能力混用。

## 1. 选择集成方式

- 用户需要 agent 调用确定的业务步骤时，使用 agent flow 工具。
- 用户需要修改业务事件或定时云端流程时，保留原触发入口。将已有触发器替换为 agent 触发器会改变原业务行为；仅在任务确实要求替换时执行。
- `Power Apps` 触发器用于应用调用，不能当作 Copilot Studio agent 触发器。

这些是本套件的操作设计建议。微软的流程概念见 [Use agent flows with your agent](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-flow)。

## 2. 标准框架的同步流程工具

**输入：** agent 与环境、流程名称、输入字段及类型、输出字段及类型、连接身份、预期响应时间、业务副作用。

**官方约束：** 针对 standard harness 文档分支，流程需要 `When an agent calls the flow` 和 `Respond to the agent`。响应动作的 `Settings > Networking > Asynchronous response` 应为 `Off`，响应须在 100 秒动作限制内返回。这个数值和开关仅适用于该文档分支。长时间的后续工作不能用“已经完成”响应掩盖。

1. 新建时，在 Copilot Studio 的 `Flows > New flow > Agent flow` 打开模板。
2. 在触发器添加输入，再在响应前添加实际动作。使用必要的连接。
3. 在响应动作设置返回字段。正常分支与异常分支的输出结构应一致。
4. 核对响应模式；发布流程，并确认发布状态。

来源：[Create an agent flow as a tool](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-flow-create)。

**复用已有云端流程：** 在 Power Automate 核对环境与流程，再编辑触发器和响应。该分支要求流程位于与 agent 相同环境的 solution。确认所有响应分支使用同一输出结构。需要保留原调用方时先设计独立包装流程，不直接破坏原入口。

只允许新建草稿时，不执行上面的 Publish。交付已保存的流程和静态检查结果，并注明挂接与调用验证可能因尚未发布而未完成；不要为完成挂接突破草稿范围。

来源：[Modify an existing flow](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flow-modify-use-with-agent)。

## 3. 新基础设施的异步分支

仅当任务确实需要长任务或异步返回时读取该分支。先核实环境已经支持新基础设施，再核实发布渠道。微软 2026-10-17 的文档允许在响应动作 `Settings` 中打开 `Asynchronous response`，然后保存或发布。

环境架构的官方判定：在 Power Automate 选择目标环境，按 `Ctrl+Alt+A` 打开环境调试信息，读取 `environmentFlowHostingType`。`SelfHostMultiTenant` 表示新架构，`LogicApps` 表示旧架构。若当前工具不能发送该快捷键或信息不可见，记录能力未确认，不猜测。这是官方提供的页面检查，不读取浏览器令牌。环境架构与 agent 的 standard/GitHub Copilot harness 是不同维度。[架构检查方法](https://learn.microsoft.com/en-us/power-automate/environment-architecture)

- 回调正式支持 Microsoft Teams。
- Microsoft Copilot 和电话渠道不支持此回调。
- 其他渠道尚未正式测试，不能假定可用。
- 用户在流程完成前发来新消息时，流程仍继续运行，但 agent 会先处理最新请求。
- 环境不支持异步时，可能提前返回“flow completed”，后台流程却仍在运行。以运行实例和业务结果证明完成。

若无法核实基础设施或渠道支持，保留标准同步方案，或提交待验证的异步配置，不直接上线。异步模式的完成证据应包括最终回调。即时响应只证明触发成功；不能将其写为业务已完成。

异步验收在已授权发布的目标 Teams 新会话中观察最终回调，并关联同一次 flow 运行。测试面板只用于前置检查，不能替代渠道回调验收。

来源：[Asynchronous response support](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flow-asynchronous-response)。本节与上一节属于不同兼容分支，不能把异步文章中的旧“两分钟”描述改写成通用同步时限。

## 4. 挂接工具并验证

1. 在 Copilot Studio 打开目标 agent，进入 `Tools > Add a tool > Flow`。
2. 选择刚发布的流程，再选 `Add and configure`。
3. 设置名称、描述和输入来源。描述说明何时使用及所需业务前提。
4. 配置完成后的行为，保存工具。
5. 同步路径用测试面板发起应调用该流程的请求。核对 agent 实际调用、实际输入、流程运行实例和返回值。异步路径按上一节在目标 Teams 会话验证最终回调。

**成功证据：** 对话触发了正确工具；流程收到正确类型的输入；运行和业务结果符合预期；agent 的答复与返回值一致。需要发布 agent 时转到 [Copilot Studio skill](../../copilot-studio-web/SKILL.md)。发布流程不等于发布 agent。

来源：[Call an agent flow from an agent](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-use-flow)。

## 5. 找不到流程或调用失败

| 现象 | 排查顺序 |
| --- | --- |
| 工具列表没有目标 | 环境 → 发布状态 → 触发器/响应类型 → solution → 当前账户可见权限 → 运行框架支持范围 |
| 输入缺失或类型错误 | 工具输入设置 → 流程触发器字段 → 测试面板实际值 |
| agent 报错但流程有记录 | 查该运行实例首个失败动作；随后核对响应模式、超时和返回结构 |
| 流程运行成功但 agent 回答错误 | 输出字段映射 → 工具完成行为 → 该次 agent 测试轨迹 |

同一失败证据没有变化时，停止盲目重试。保留对象链接与错误信息，再确定缺失权限、数据或兼容条件。
