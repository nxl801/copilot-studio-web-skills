# 部署诊断与恢复边界

恢复不是删除后重装。先确定失败发生在打包、导入、激活、认证还是业务运行。核查日期：2026-10-22。

## 先读取证据

| 症状 | 网页检查 | 下一步 |
| --- | --- | --- |
| 导入失败或长时间无结果 | Solutions → See history；错误详情/Download Log File | 区分运行中与失败，记录版本、错误码、Activity ID；运行中不重复导入 |
| 已导入但旧行为仍在 | 对象 → Advanced → See solution layers；检查源发布状态 | 找到未发布定制或覆盖层后再决定修复，不直接清除未知 unmanaged layer |
| flow 关闭或认证失败 | flow 详情、connection reference、运行历史 | 在授权范围修复目标连接或权限，再受控测试；不要反复启用以猜测原因 |
| agent 工具/主题缺失 | 源/目标 solution Objects 对照 | 回源补必要对象后重新发布包 |
| agent 渠道不可用 | 目标认证、Publish 状态、channel、DLP 错误 | 交给产品 skill 完成缺失环节，不假定 import 失败 |
| 更新提示已有 pending upgrade | Solutions 中 `_Upgrade` 及历史 | 先确认前一次状态和数据变化；不要直接删除 holding solution |

[历史与错误详情](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/solution-history)、[solution layers](https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm)、[pending upgrade 故障](https://learn.microsoft.com/en-us/troubleshoot/power-platform/dataverse/working-with-solutions/upgrade-fails-pending-upgrade)

## 选择恢复方式

先保留失败证据、当前版本、关键参数和已有可用备份。普通配置错误优先在源修复并交付更高版本。目标连接失效则修复连接。数据恢复或删除操作须在其影响已纳入授权时执行。

| 方式 | 能恢复的内容 | 限制 |
| --- | --- | --- |
| 修复后发布更高版本 | 应用定义、逻辑与配置 | 不自动撤销已经写入的外部业务数据 |
| Pipeline 历史版本 Redeploy | 已保存的旧 solution 产物 | 需允许重部署旧版本；可能删除新组件和数据 |
| 环境备份恢复 | 受支持环境的备份状态 | 会覆盖目标环境；有区域、类型、Dataverse、策略和容量限制 |
| 删除 managed solution | 移除该包定制 | 可能删除自定义表/列数据；不能称为安全回滚 |
| 删除 unmanaged solution | 移除容器 | 保留其定制，不能撤销导入 |

[solution 删除语义](https://learn.microsoft.com/en-us/power-platform/alm/solution-concepts-alm)

## 已授权的历史版本重部署

先核实 pipeline 的 `Allow redeployments of older versions`、所选成功记录、目标环境及新版新增组件/数据。打开 Pipelines → Run history → 旧成功记录 → … → Redeploy。阅读当前警告后，按正常部署向导处理配置。

微软明确提示这项操作可能覆盖最新版本并移除新版数据及新表。若用户只授权“修复运行错误”，不能据此推定其接受这种删除。缺少影响授权时，准备版本差异和恢复方案后再询问；已有明确授权不重复询问。[旧版本重部署](https://learn.microsoft.com/en-us/power-platform/alm/redeploy-past-solution-versions)

## 已授权的环境恢复

执行前打开[当前备份恢复手册](https://learn.microsoft.com/en-us/power-platform/admin/backup-restore-environments)，核对该环境支持情况及真实可用恢复点。不能用“导出过 solution”证明业务数据已有备份。

网页路径：Power Platform admin center → Manage → Environments → 源环境 → Backup & Restore → Restore or manage。选择备份时间，再选择要覆盖的目标环境。复核目标 ID、恢复点、预期数据损失窗口和影响应用后提交一次。

不能直接向 production 类型环境恢复。若任务要求恢复生产，类型转换和停机影响也必须在范围内。不要为让目标出现在列表而随意转换、重置或更换环境。

恢复完成后检查 administration mode、connection reference、flow 状态和产品发布。恢复可能使 solution flow 关闭并需要重新绑定连接。先验证配置，再按授权启用。若外部系统已执行动作，另行核对；环境恢复不会撤销这些动作。

## 停止条件

无新证据且同一错误仍存在时，停止重复操作。输出当前环境和版本、已完成步骤、失败记录、尚缺权限或决定、建议的最小恢复动作。状态未知时写“未确认”，不要宣称恢复成功。
