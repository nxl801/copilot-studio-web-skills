---
name: power-automate-web
description: 通过 Power Automate 或 Copilot Studio 的网页设计器创建、配置、测试和排查云端流程，处理 agent 工具触发、连接引用及运行记录。用于网页端 cloud flow 任务；不用于 Power Automate Desktop 或 Copilot SDK。
---

# Power Automate 网页操作

完成用户指定的云端流程及集成。按当前网页状态操作。先读套件的[浏览器约定](../power-platform-web/references/browser-contract.md)，按[任务记录](../power-platform-web/references/task-record.md)记录目标、变更和证据。

## 开始前

1. 在 `make.powerautomate.com` 核对账户、租户、环境和目标流程。用详情页与所属 solution 区分重名流程。
2. 确定触发来源：业务事件、定时任务、Power Apps、Copilot Studio agent。不要用另一种触发器替代原有业务入口。
3. 检查用户要求到哪一层：草稿、可运行流程、agent 集成或跨环境部署。已有发布授权继续有效。
4. 在运行前识别真实写入、发信、审批和外部调用。测试也可能产生这些效果；使用授权的测试记录和收件人。

## 按任务读取

| 任务 | 参考 |
| --- | --- |
| 新建/编辑云端流程、连接、测试、排障 | [云端流程手册](references/cloud-flows.md) |
| 给 Copilot Studio 提供流程工具 | [Agent 集成手册](references/agent-tools.md) |
| SharePoint、Dataverse、Teams 等依赖 | [关联产品](../power-platform-web/references/integrations.md) |
| 在 Power Apps 内挂接流程 | [Power Apps skill](../power-apps-web/SKILL.md) |
| 导出、导入、部署到另一环境 | [发布管理 skill](../power-platform-release/SKILL.md) |

## 必须区分的状态

- Solution-aware flow 是放在解决方案中的流程。新设计器的 `Save draft` 不改变当前运行版本；`Publish` 才让更改参与运行。普通非 solution 流程不能假设有相同草稿保护。
- `Published` 与流程启用状态分别核对。保存提示不能证明触发器已经执行。
- Flow Checker 是静态检查。它不能证明连接权限、业务分支和返回结果正确。
- 草稿不能作为已运行测试通过的证据。需要运行时，按手册在已授权的开发/测试环境发布可运行版本。若任务仅允许草稿，交付草稿及未运行说明。
- 失败后先查对应运行实例；不能因网页超时反复点击 Test 或 Resubmit。

## 完成条件

给出流程链接、环境、所属 solution、保存/发布/启用状态。若已运行，给出运行实例、实际输入摘要、分支、输出与业务结果。若用于 agent，再验证一次 agent 到流程的调用。对未完成项说明具体阻塞，不用“已保存”代替“已部署”。
