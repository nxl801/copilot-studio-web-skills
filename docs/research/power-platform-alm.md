# Power Platform ALM 与治理研究

检索和阅读日期：2026-10-22。仅使用微软官方资料。没有登录租户，也没有执行真实发布。本文件记录设计依据；具体网页流程在 [power-platform-release](../../skills/power-platform-release/SKILL.md)。

## 结论

建议把跨环境发布单独做成 skill。Copilot Studio、Power Automate、Power Apps 共用环境、solution、连接引用和环境变量。它们各自仍有发布与业务验证步骤。把部署放在三个产品 skill 内会重复维护同一套规则。

这是本项目的结构判断，不是微软规定的 skill 划分。微软官方资料支持的是下列产品事实。

## 官方事实及影响

| 事实 | 对网页 agent 的影响 | 官方来源 |
| --- | --- | --- |
| 环境属于 Microsoft Entra 租户；环境角色不自动赋予 Dataverse 数据权限 | 每次跨产品核对租户与环境 ID；把创建权限和数据权限分开检查 | [Environments overview](https://learn.microsoft.com/en-us/power-platform/admin/environments-overview) |
| 开发使用 unmanaged，向非开发环境交付 managed 是官方 ALM 最佳实践 | 技能须区分源码包和部署包；managed solution 不等于 Managed Environment | [Solution concepts](https://learn.microsoft.com/en-us/power-platform/alm/solution-concepts-alm) |
| Connection reference 指向实际 connection；旧资源加入 solution 不保证自动迁移连接方式 | 不能只看资源已经在包里，还要看连接绑定 | [Connection reference](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-connection-reference) |
| 环境变量把可变参数与应用逻辑分开；Current Value 优先于默认值 | 导入前后都核对目标站点、列表等参数；秘密用受支持的秘密配置 | [Environment variables](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/environmentvariables) |
| Agent 的新增主题与 flow 需要补充 required objects；导入后要重新配置认证并发布 | 打包清单与导入后验收必须分开；渠道和知识完整性另行检查 | [Export/import agents](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-solutions-import-export) |
| Pipelines 依阶段部署同一个产物；不迁移 Dataverse 表数据，也不自动发布源未发布定制 | 管线成功不能证明数据、权限或渠道就绪 | [Pipelines overview](https://learn.microsoft.com/en-us/power-platform/alm/pipelines) |
| Pipeline 当前固定采用 Upgrade，不能选择 Update | 提交前检查被移除的组件和数据影响；保留旧组件的需求需选择被组织允许的其他路径 | [Pipeline 导入行为](https://learn.microsoft.com/en-us/power-platform/alm/pipelines) |
| Update 保留旧组件；Upgrade 可以删除新包已移除的组件 | 不盲目接受向导默认 Upgrade；先理解差异 | [Upgrade or update](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/update-solutions) |
| 历史版本 Redeploy 可能移除新版数据与新表 | 不写“一键安全回滚”；说明影响和可用恢复点 | [Redeploy past versions](https://learn.microsoft.com/en-us/power-platform/alm/redeploy-past-solution-versions) |

## 网页发布顺序

以下是本项目根据官方流程整理的执行顺序：

1. 读取现有授权、源/目标环境、solution 版本及业务完成范围。
2. 在源 solution 收齐对象和依赖。核对 connector、连接引用和环境变量。
3. 保存并发布本次需要发布的源定制。检查共享环境中批量发布的影响。
4. 走现有 pipeline，或从源导出后到目标 Import solution。
5. 核对目标连接和参数。处理依赖；手动导入选择 Update/Upgrade，pipeline 核查固定 Upgrade 的影响。
6. 从 solution history 或 pipeline run 确认终态。
7. 到目标执行 flow、app、agent 的产品验证。依授权完成发布和共享。

[导出操作](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/export-solutions)、[导入操作](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/import-update-export-solutions)、[运行 pipeline](https://learn.microsoft.com/en-us/power-platform/alm/run-pipeline)、[查看 solution history](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/solution-history)

## 微软生态的治理边界

### DLP

DLP 是数据防泄漏策略，即控制哪些连接器和数据路径可以一起使用。Copilot Studio 数据策略可以限制未认证聊天、知识源、工具、HTTP、渠道和事件触发。策略按 Business、Non-business、Blocked 分组，并可实时阻止操作。页面出现阻塞时，先记录连接器、策略和环境；不要把改变策略作为普通发布修复。[Copilot Studio data policies](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention)

### Entra、Teams 与 SharePoint

Entra 是微软身份服务。编辑者登录、agent 用户认证、工具连接身份和底层数据访问是不同检查点。工具可采用用户认证；渠道支持和 Teams 单点登录要求需按实际组合核对。[工具用户认证](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-enduser-authentication)

条件访问可能使 Teams 等渠道中的 agent 无响应。应由管理员根据错误与登录上下文检查策略，不能把关闭认证作为修复。[Conditional Access](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-conditional-access)

SharePoint 知识和数据连接还受网站权限、端点过滤及具体接入模式影响。渠道可用不证明目标用户能读取内容。验收需用目标用户可访问的资料和身份。

### 备份与恢复

Solution 产物不是业务数据备份。环境恢复覆盖目标环境，并受环境类型、区域、Dataverse、策略和容量限制。生产环境不能直接恢复；恢复后还可能需要处理连接及 flow 启用状态。备份保留期以租户当前设置为准，不在 skill 中写死为统一天数。[Backup and restore](https://learn.microsoft.com/en-us/power-platform/admin/backup-restore-environments)

## 新变化的维护要求

当前官方页面已经出现新的 agent 运行模式适用范围，以及 2026 年末环境类型和 pipelines 管理要求的变更说明。发布技能应在执行时检查当前模式、租户提示和官方前置条件。不要沿用“所有 Developer 环境都免费可建”“所有 agent 都走同一导出路径”等固定假设。具体日期与许可条件不在此重复，避免后续与官方更新冲突。[环境概览](https://learn.microsoft.com/en-us/power-platform/admin/environments-overview)、[Pipeline 设置](https://learn.microsoft.com/en-us/power-platform/alm/set-up-pipelines)

## 还需真实租户验证

- 实际租户中的导航名称、语言和功能开关。
- Agent 使用的运行模式与可导出的组件。
- 目标环境的权限、DLP、许可和容量。
- 外部数据、共享和渠道设置是否完整恢复。
- 普通用户身份下的端到端业务结果。

本次研究不能代替这些验证；交付物应如实标注“官方文档核查完成，租户运行验收待执行”。
