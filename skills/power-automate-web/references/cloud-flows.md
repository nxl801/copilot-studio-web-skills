# 云端流程网页手册

文档核查：2026-10-22。以下步骤来自微软公开文档，并加入面向操作 agent 的验证方法。UI 名称是定位线索；以当前页面可见控件为准。本手册没有真实租户测试记录。

## 1. 定位与建立流程

**输入：** 环境、现有流程链接或唯一名称、触发事件、数据来源、预期输出、允许执行的业务动作。

1. 打开 [Power Automate](https://make.powerautomate.com)，核对右上角环境选择器。
2. 修改现有流程时，从 `My flows` 或 `Solutions` 打开目标，再读详情页。检查所有者、连接、启用状态及所属 solution。找到对象后编辑，不新建同名替代品。
3. 需要可部署流程时，打开指定 solution，选择 `New > Automation > Cloud flow`，再选择符合业务的类型。没有 solution 时先确认应使用的项目 solution。
4. 在触发器卡片填写资源、筛选条件和输入类型。按业务添加动作，再绑定动态内容。卡片出现红色字段时先解决必填或表达式问题。
5. 在 solution 的对象列表确认流程和依赖已经出现。

**已有流程加入 solution：** `Solutions > 目标 solution > Add existing > Automation > Cloud flow`。`From Dataverse` 和 `Outside Dataverse` 分别列出已有 solution 流程与非 solution 流程。部分旧流程有迁移限制；失败时保留原对象并读取错误。

来源：[Create a cloud flow in a solution](https://learn.microsoft.com/en-us/power-automate/create-flow-solution)。

## 2. 连接和连接引用

连接保存服务登录信息。连接引用是 solution 中指向连接的组件。两者不能只按显示名判断身份。

| 目标 | 网页操作 | 成功证据 |
| --- | --- | --- |
| 建立引用 | `Solutions > 目标 solution > New > More > Connection Reference`；填写名称、连接器、已核对身份的连接 | 对象列表出现引用，详情显示目标连接 |
| 修复失效连接 | 在 `Connections` 查底层连接；按页面要求修复登录或选择已授权替代连接 | 连接恢复有效，原流程引用仍指向预期身份 |
| 修改引用 | 打开 solution 内引用并更改连接 | 等待异步更新完成，再检查引用此组件的流程 |

已有非 solution 流程加入 solution 后，不一定自动改用连接引用。先看设计器或 Flow Checker 的迁移提示。更新共享引用可能影响多个流程；先检查依赖。启用流程的人还需拥有或获准使用相关连接，不能用管理员个人连接悄悄替代业务身份。

来源：[Use a connection reference](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-connection-reference)。

## 3. 保存、发布和版本

1. 读取工具栏。如果存在 `Save draft`，先保存草稿并核对标题旁状态。
2. 运行验证需要已发布、可运行版本。草稿目前不能测试。开发/测试环境发布在授权范围内时，解决阻塞项后选择 `Publish`，再核对状态。
3. 若仅授权准备草稿，停在草稿交付；记录无法进行运行验证的原因。
4. `Version history` 可查看历史并恢复为新草稿。恢复后仍须按目标重新发布。
5. 导出 solution 前确认目标更改已发布。导出包含最后已发布版本，不含未发布草稿和版本历史。

**限制：** 普通流程的 `Save` 与 solution 流程的 `Save draft` 不等价。先识别设计器和版本类型，不根据旧教程推断运行版本。

来源：[Drafts and versioning](https://learn.microsoft.com/en-us/power-automate/drafts-versioning)、[Cloud flows designer](https://learn.microsoft.com/en-us/power-automate/flows-designer)。

## 4. 测试与运行记录

**输入：** 测试样例、预期分支、预期输出、允许的副作用、可查验的目标记录。

1. 先看 Flow Checker，解决影响执行的问题。
2. 在可运行版本选择 `Test > Manually`。按触发器类型执行测试事件。不要假设所有流程都会显示 `Run flow`。
3. 返回详情页，从运行历史打开本次实例。用时间、输入或关联记录识别本次运行，不能只看“最近一个绿色结果”。
4. 检查触发器、条件、动作和输出。动作成功后还要检查业务结果，例如目标记录是否只有一条、返回值是否正确。
5. 记录运行状态、时间、耗时、关键结果和错误动作。输出包含秘密或个人数据时只保留必要摘要。

重复运行可能重复写入或发信。`Resubmit` 前先确认上次已经完成哪些动作。使用静态结果时，明确标注“模拟输出”，不能将其作为真实连接调用成功证据。

来源：[Test cloud flows](https://learn.microsoft.com/en-us/power-automate/guidance/coding-guidelines/test-cloud-flows)、[Cloud flow tutorial](https://learn.microsoft.com/en-us/power-automate/get-started-with-cloud-flows)。

## 5. 有证据地排障

| 现象 | 先检查 | 下一步与停止条件 |
| --- | --- | --- |
| 没有运行实例 | 流程是否启用、触发事件和筛选条件、连接器触发机制 | 仅在测试范围创建新事件；等待该连接器正常触发窗口。不要反复创建业务数据 |
| 保存失败 | 卡片必填项、表达式、错误文本 | 修复首个明确错误后重试；无变化的同一错误保留证据并报告 |
| 401/403 | 连接身份、资源权限和组织策略 | 修复授权范围内的连接；缺少权限时交给资源管理员，不提高权限绕过 |
| 404 | 目标列表、文件、表或端点 | 用当前真实资源重新选择，不猜资源 ID |
| 429 | 运行量、连接器限额、重试策略 | 按实际错误等待或调整已授权流程；不要连续重跑 |
| 全绿但结果错误 | 条件实际值、动态字段、循环输入、返回类型 | 对比业务预期，修复映射；不能把运行成功当业务成功 |

错误码只提供调查方向，不独立证明原因。来源：[Troubleshoot cloud flow errors](https://learn.microsoft.com/en-us/power-automate/troubleshoot-flow-errors)。
