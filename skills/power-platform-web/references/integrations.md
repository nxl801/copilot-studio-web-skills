# 微软生态集成参考

检索基线：2026-10-22。只在当前任务涉及相关服务时阅读相应段落。这里覆盖集成边界；不等于每个微软产品都有完整管理 skill。

## 共用对象

| 名称 | 通俗说明 | 网页核对重点 |
|---|---|---|
| Tenant | 组织的身份和管理边界 | 当前组织、账号及专属云 |
| Environment | 应用、流程和数据所在的隔离区 | 环境 ID、类型、区域、Dataverse 可用性 |
| Solution | 打包应用组件的容器 | unique name、版本、publisher、依赖 |
| Connection | 服务的登录连接 | 所有者、服务、状态、授权范围 |
| Connection reference | solution 中指向连接的引用 | 逻辑名称和目标环境实际连接的绑定 |
| Environment variable | 不同环境使用不同值的配置 | 定义、默认值、当前值；秘密值不进入记录 |
| DLP / Data policy | 限制连接器及数据组合的策略 | 具体策略、连接器组合和受影响环境 |

## Dataverse 与权限

Dataverse 是 Power Platform 的业务数据服务。制作权限、应用共享权限和表数据权限应分别核查。Environment Maker 不自动拥有环境数据权限；不能用“能建应用”证明“能读业务表”。在 Dataverse 环境中检查适用安全角色和具体表权限。见 [官方角色说明](https://learn.microsoft.com/en-us/power-platform/admin/database-security)。

读写表前确认逻辑名称、关键字段、拥有者、测试记录范围。不要为了测试清空业务表。修改结构后回到应用/flow 更新字段映射并验证。

## SharePoint 知识与数据

知识检索和连接器动作是不同路径。先区分用户要“回答文档问题”还是“读取/写入列表”。Copilot Studio 的 SharePoint 知识需要匹配认证配置与用户已有内容权限；选择 No authentication 不能检索该类 SharePoint 知识。被引用页面内的链接不会自动成为知识源。见 [官方 SharePoint 知识说明](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-add-sharepoint)。

网页操作时核对站点、文档库或列表的实际 URL；检查接入状态；用有权用户验证引用，再在用户授权的测试范围内验证无权用户边界。不要为解决检索失败而扩大站点共享。

## Entra 与工具身份

Microsoft Entra ID 是微软组织身份服务。agent 的用户认证和工具的服务连接分别配置。官方区分 agent author authentication 与 user authentication；涉及用户私有数据时要核查工具实际用谁的权限。见 [工具认证](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-enduser-authentication)。

手动认证时按当前渠道官方指南核查应用注册、回调地址、作用域和同意状态。不要为了排障默认为全部应用权限或要求全局管理员。发现管理员同意需求时，给出具体配置和理由，让有权人员完成。

## Teams 与 Microsoft 365

agent 发布、添加渠道、个人安装、组织目录可见和管理员批准可能是不同状态。操作必须匹配用户指定的分发范围。实际测试使用目标渠道和目标身份；开发者测试面板不能替代 Teams 验收。具体步骤见 [Copilot Studio skill](../../copilot-studio-web/SKILL.md)。

## 策略阻塞

遇到连接器无法组合、保存失败或策略提示时，记录错误码、连接器名称、环境和策略名。管理中心当前文档路径为 Security → Data and privacy → Data policy；运行时以实际页面为准。官方数据策略区分 Business、Non-business 和 Blocked，规则会约束数据组合。见 [管理数据策略](https://learn.microsoft.com/en-us/power-platform/admin/prevent-data-loss)。

只获应用配置授权时，不能改租户策略来消除错误。可以准备最小变更建议并继续与阻塞无关的工作。用户明确授权治理修改时，仍须读取对应官方当前操作手册与影响范围；本版本没有覆盖完整的策略管理生命周期。
