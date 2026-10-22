# 标准框架：配置操作

核验日期：2026-10-22。先完成[体验识别](experience-detection.md)。以下步骤只适用于 standard harness；中文页面可使用对应译名。

## 创建与基本配置

前置条件：用户给出或当前任务已明确目标环境、用途、主要语言与新建意图。环境中需要创建权限；环境不可见时检查租户、环境状态与权限，不另选默认环境代替。

| 操作 | UI 锚点与输入 | 预期状态 / 完成证据 | 异常处理 |
| --- | --- | --- | --- |
| 新建 agent | 标准体验的 Agents → Create blank agent，或 Home 的 Agent 创建入口；填名称 | 出现该 agent 的 Overview；记录链接和环境 | 创建后页面超时，先查 Agents 列表与唯一名称，避免重复创建 |
| 创建前选主要语言与 Solution | 创建框中的设置或 Advanced settings；选择语言、Solution、schema name | 创建后的语言与解决方案符合目标 | 主要语言创建后不能更改；错误时先报告，不能擅自删建替换 |
| 编辑身份和指令 | Overview 的 Details / Instructions → Edit → Save | 离开后重开并回读改动；标题、说明与指令符合任务 | 保存报错时保留原值与错误，不继续发布 |

若使用自然语言创建，检查系统生成的名称、指令和建议；只接受任务需要的组件。自然语言创建受云类型和管理员设置影响，空白创建是可用时的替代路径。[创建与配置官方说明](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-first-bot)

指令只引用已经配置的能力。需要指向具体组件时，使用 `/` 菜单选择现有对象，并检查选择结果。不要用文字假装创建工具。保留系统引用格式；不要要求 agent 隐藏或改写系统引文。[指令官方说明](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-instructions)

## 知识源

知识源是 agent 回答时检索的资料。先确定用户授权的资料范围；不要把整个 SharePoint 站点替代用户指定的文件夹或文件。

1. 在 Overview 或 Knowledge 找到 Add knowledge。
2. 选择实际来源类型。输入明确的 URL、文件或数据表；核对选中的账户与访问范围。
3. 填写区分用途的名称和说明，完成添加。
4. 回到知识列表检查状态。标准框架知识源达到 Ready 才进入测试。
5. 用资料中有答案的问题测试，并核对返回依据。再测一个资料外问题，观察是否超出指定知识范围。

完成证据包括来源名称、类型、范围、就绪状态和测试结果；不把敏感文档正文复制进任务记录。配置入口依据[添加知识](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-add-existing-copilot)。

| 状态 / 现象 | 下一步 |
| --- | --- |
| In progress | 等待处理并适度刷新；保留状态；不要重复上传 |
| Unknown | 查数据策略、认证配置和 Dataverse search；确认所需管理员动作 |
| Error | 按错误检查格式、大小、权限、源是否删除或加密；只有确认原因和对象后才替换来源 |
| Ready 但无相关答案 | 检查资料内容、查询、访问身份与编排选择；不要立即放宽权限 |

状态与限制依据[知识测试](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-test)。SharePoint、Dataverse 的跨产品权限验证见[连接约定](../../power-platform-web/references/integrations.md)。

## 主题与编排

主题（Topic）定义一段对话的节点和分支。生成式编排按用途说明选择组件；经典编排主要按触发语句选择主题。先读取现有设置，只有任务需要时才改变编排模式。

| 操作 | UI 锚点与输入 | 验证 / 失败处理 |
| --- | --- | --- |
| 检查编排 | Settings → Generative AI → Orchestration | 记录当前值；管理员禁用时不绕过 |
| 新建主题 | Topics → Add a topic → From blank | 主题出现在列表；名称能区分用途 |
| 配置触发 | 读取 Trigger 节点属性；生成式路径检查用途说明，经典路径检查触发语句 | 用真实业务表达测试触发；不要只测标题原文 |
| 构建对话 | 节点下方 Add node；按需求选择消息、问题、条件、变量、工具或跳转 | 检查必填输入、变量类型、条件分支及结束行为；保存后清理 checker 错误 |
| 调整系统主题 | 仅修改任务所需的欢迎、回退等系统行为 | 保留原值；测试受影响入口，不能因普通主题失败而重写全部系统主题 |

生成式编排说明依据[编排文档](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-generative-actions)。主题画布与节点依据[创建和编辑主题](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-create-edit-topics)。

复杂主题不要直接凭记忆生成 YAML 并整段覆盖。官方说明复杂主题完全通过代码编辑器创建并非完整支持。若任务确需代码编辑，先读取当前主题、保存原文，再用画布和 checker 验证结果。

## 工具与 agent flow

工具是 agent 可执行的外部操作。先定义输入、输出、执行身份和预期副作用，再配置入口。

1. 打开 agent 的 Tools → Add a tool。
2. 选择已有连接器、流程或任务指定的新工具类型。面板名称可能是 New tool、See all 或直接分类；以可见项为准。
3. 配置名称与用途说明、Inputs 和 Completion。逐项核对类型、必填项、固定值与对话填充值。
4. 设置或核对工具认证方式。只有任务允许的连接身份才能用于写入操作。
5. 保存，确认工具出现在本 agent 的工具列表，再通过已授权的测试验证调用和输出。

工具不出现时，检查数据策略、可用类型和连接器权限，不用其他连接器绕过。入口与字段依据[添加工具](https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-tools-custom-agent)。

### 接入已有流程

对标准同步路径，检查流程属于正确环境和 Solution，并有 `When an agent calls the flow` 与 `Respond to the agent`。流程应已发布，响应动作的异步设置为 Off；设计响应在官方 100 秒限制内返回。Tools → Add a tool → Flow → 选择流程 → Add and configure，随后核对参数并保存。[接入流程](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flow-agent)、[流程 FAQ](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-faqs)

如果从某主题的工具节点接入，需在该主题单独验证。agent 级工具可供编排器选择；主题级调用不自动等同于 agent 级可用。需要新建或修改流程逻辑时，读取 [power-automate-web](../../power-automate-web/SKILL.md)。

### 异步响应分支

2026-10-17 的官方异步文档支持新基础设施环境的长时间流程；标准接入文档仍要求同步响应。执行时记录适用分支，不能把两份说明拼成一个流程。

环境架构不是 agent harness。按 [Agent 集成手册](../../power-automate-web/references/agent-tools.md)读取 Power Automate 官方环境调试信息，确认新架构；不能仅根据 agent 是新体验就开启异步。

仅当环境确认支持、任务需要长时间执行且目标渠道支持回调时，按异步文档在 `Respond to the agent` → Settings 打开 Asynchronous response。Teams 是文档明确测试支持的渠道；Microsoft Copilot 与电话渠道不支持回调。测试需同时检查流程运行完成和渠道实际收到结果；“已触发”不代表业务完成。不因遇到超时就直接切换异步。[异步响应官方说明](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flow-asynchronous-response)

## 认证

区分两层认证：agent 认证决定谁能对话；工具认证决定外部服务使用谁的权限。

| 层级 | UI 锚点 | 选择依据与验证 |
| --- | --- | --- |
| agent | Settings → Security → Authentication → Save | 保留已授权的目标认证方式；选择后检查主题变量及渠道兼容性；修改需发布才生效 |
| 工具 | 工具配置中的 Authentication | 受用户权限限制的数据使用 User authentication；公共、低风险服务可按任务采用 Agent author authentication |

对 Teams + Microsoft 365 内置渠道，先核对当前认证要求。手工认证还涉及 Entra 配置、SSO 与 manifest；按该分支官方文档操作，不猜应用 ID 或密钥。遇到登录、同意、证书或管理员步骤时，按共享浏览器约定处理。

不要为了演示网站方便而把企业 agent 改为 No authentication。未经认证的 agent 不能使用用户凭据工具；工具的用户认证也有渠道支持限制。完成后需要在目标渠道以适当用户身份验证访问成功及预期访问限制。[agent 认证](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configuration-end-user-authentication)、[工具认证](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-enduser-authentication)
