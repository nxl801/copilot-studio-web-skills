# 通过现有 Pipeline 部署

Pipeline 是组织配置的分阶段部署路径。这里使用现有路径；新建 host、环境和治理设置需要另有明确任务。核查日期：2026-10-22。

## 检查适用条件

开发环境需要 Dataverse，并与 pipeline 关联。执行者需要运行 pipeline 及向目标环境导入的权限。管线、目标受管环境、区域和许可条件以当前租户配置及[官方设置指南](https://learn.microsoft.com/en-us/power-platform/alm/set-up-pipelines)为准。若入口缺失，先核对环境、solution 类型、关联及权限，不立即新建重复管线。

普通发布先完成 [solution 准备](solutions.md)。Pipelines 不自动发布源环境中的未发布定制。它交付 solution 和目标配置，不迁移 Dataverse 表内业务记录。[Pipeline 概览](https://learn.microsoft.com/en-us/power-platform/alm/pipelines)

Pipeline 当前固定使用 Upgrade，且不使用 Overwrite customizations；不能在向导中改选 Update。提交前对照组件清单，核实移除旧组件及相关数据的影响已在授权范围内。若任务要求保留目标旧组件，应采用组织允许的手动 Update 路径；组织不允许该路径时，准备影响说明并请求所缺决定，不能绕过管线治理。[官方导入行为说明](https://learn.microsoft.com/en-us/power-platform/alm/pipelines)

## 操作与核验

| 阶段 | 当前网页锚点及动作 | 应观察的状态 |
| --- | --- | --- |
| 选包 | Power Apps/Power Automate → 源开发环境 → Solutions → 打开 unmanaged solution | 名称、版本、组件正确 |
| 选路径 | solution → Pipelines，或 Overview → Deploy | pipeline 和目标 stage 符合任务 |
| 预检 | 选择 stage → Deploy here → Now/Later → Next | 目标依赖检查通过；Upgrade 删除影响已核查；时间与时区正确 |
| 配置 | 填 connection reference、environment variable | 连接主体和数据位置属于目标环境 |
| 提交 | 阅读部署摘要，填写可追踪的说明，Deploy 一次 | 出现本次部署记录 |
| 等待 | Pipelines → Run history → 对应记录 | 终态成功，或明确失败/审批等待 |
| 验收 | 打开目标环境执行产品检查 | 包版本、配置和关键业务行为一致 |

按 stage 顺序推进。首个阶段提交后，后续阶段使用同一包；源环境后续编辑不会自动进入这次发布。需要新变更时创建新的发布版本和部署记录。[运行手册](https://learn.microsoft.com/en-us/power-platform/alm/run-pipeline)

## 分支处理

- `Pending approval`：记录审批状态及审批人线索，不能代替审批人批准，也不另建路径绕过流程。
- `Missing dependencies`：根据预检清单修复源包或先部署基底包。修复后再发起新检查。
- 权限、Managed Environment 或许可阻塞：记录页面事实及所需管理员动作。不要自动切换到其他生产环境或购买许可。
- 已定时但需改期：使用当前记录的取消/改期入口，先确认记录和时间；不叠加第二条相同部署。
- Failed：保存 Run history 错误；先确认有没有已应用的组件或后续动作，再按 [恢复手册](recovery.md) 决定处理。

完成报告区分“已请求”“审批中”“包已部署”和“目标业务验证通过”。
