---
name: power-platform-release
description: 通过 Power Platform 网页打包、导入、升级或用现有 pipelines 部署 Copilot Studio、Power Automate、Power Apps 解决方案，并核验目标环境。用于跨环境交付、部署排障和明确请求的恢复任务；仅编辑内容或单一渠道发布时使用相应产品 skill。
---

# Power Platform 网页交付

ALM 指应用生命周期管理，即把同一套应用和配置从开发环境交付到测试、生产环境。本 skill 负责跨环境交付；各产品 skill 负责内容编辑和产品发布。

## 进入任务

1. 读取 [网页操作约定](../power-platform-web/references/browser-contract.md)。已有会话和授权继续有效。
2. 按 [任务记录](../power-platform-web/references/task-record.md) 核对租户、源/目标环境 ID、solution 唯一名称、版本及完成范围。名称相同不代表同一环境。
3. 先检查目标环境现状、已有版本和依赖。明确要达到“包已导出”“已导入”“测试通过”还是“目标渠道可用”。
4. 在目标页面核实权限和组织策略。Environment Maker 不等于 Dataverse 数据权限。不要为完成部署自行创建环境、购买许可或扩大管理员权限。

明确的部署授权覆盖同一目标和范围内的必要步骤，不再次索要统一审批。发现新增目标、扩大共享范围、删除组件、覆盖数据或更改租户策略超出已有授权时，先完成可审阅的影响说明，再询问缺失决定。平台自身的审批流程照常执行。

## 按任务读取

| 任务 | 读取 |
| --- | --- |
| 打包、导入、更新或升级 | [solutions.md](references/solutions.md) |
| 使用已配置的部署管线 | [pipelines.md](references/pipelines.md) |
| 导入后异常、历史版本重部署、环境恢复 | [recovery.md](references/recovery.md) |
| Entra、DLP、Teams、SharePoint 或数据访问阻塞 | [集成边界](../power-platform-web/references/integrations.md) |

默认复用组织现有 solution、publisher 和发布路径。没有指定路径时，先检查已有 pipeline；否则采用网页导出/导入。不要把设置 pipeline host 或修改治理策略混入普通部署任务。

## 完成条件

- 用导入历史或 pipeline run 的终态证明包已部署，记录版本、目标环境和运行记录。
- 在目标环境复核连接映射、环境变量、flow 启用状态和关键数据来源。
- 按任务范围完成产品检查。Copilot Studio 导入后仍需核实认证并发布 agent；应用共享与数据权限分别验证。
- 目标渠道或应用用目标用户权限完成一次关键业务验证。没有可用测试身份时，准确标注这一项未验证。
- 任务若只要求导出或导入，达到该范围即结束，不自动扩大到发布、共享或真实业务执行。

部署失败时先查历史和具体错误。已有后台任务、状态未知或相同前置错误未修复时，不重复提交。报告已完成状态、失败位置、可继续步骤和证据。
