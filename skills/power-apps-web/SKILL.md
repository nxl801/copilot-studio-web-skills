---
name: power-apps-web
description: 通过 Power Apps 网页端创建或修改 canvas 与 model-driven 应用，配置数据和流程，验证保存、发布及共享。用于 make.powerapps.com 的应用操作；不用于本地前端项目或 Power Automate Desktop。
---

# Power Apps 网页操作

完成用户指定的应用配置。先读[浏览器约定](../power-platform-web/references/browser-contract.md)，按[任务记录](../power-platform-web/references/task-record.md)保留对象、变更和验证证据。

## 先识别对象

1. 打开 `make.powerapps.com`，核对账户、环境、应用链接和类型。
2. Canvas app（画布应用）自行设计界面与公式。Model-driven app（模型驱动应用）通过 Dataverse 表、表单、视图和导航组织业务。读取当前应用类型，不因名字相似而创建替代品。
3. 确定目标数据源、数据权限、测试数据和交付状态。保存、发布、共享分别执行和核验。
4. 若已有应用在托管 solution 中，先检查可编辑范围。不要为完成修改自行创建未托管覆盖层；跨环境更新使用[发布管理 skill](../power-platform-release/SKILL.md)。

## 按需读取

| 任务 | 参考 |
| --- | --- |
| 画布、控件、数据连接、应用调用流程 | [Canvas 应用手册](references/canvas-apps.md) |
| Dataverse 表页面、表单视图、导航、角色共享 | [模型驱动应用手册](references/model-driven-apps.md) |
| 云端流程内部逻辑或运行失败 | [Power Automate skill](../power-automate-web/SKILL.md) |
| SharePoint、Dataverse、Entra 等依赖 | [关联产品](../power-platform-web/references/integrations.md) |

## 完成条件

- 提供应用链接、环境、类型和实际交付状态。
- 核验核心页面、关键操作和数据结果。预览中的写入与流程调用也可能执行真实操作。
- 发布时确认目标版本已上线；共享时确认用户/组和权限符合任务范围。
- 共享应用不能证明用户已获数据权限。用授权的测试身份验证；不能验证时明确说明。
- 只改草稿时报告草稿完成和未发布，不声称用户已能使用新版本。
