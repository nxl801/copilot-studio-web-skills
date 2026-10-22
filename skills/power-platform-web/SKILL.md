---
name: power-platform-web
description: "通过网页协调 Copilot Studio、Power Automate、Power Apps 的跨产品配置与交付任务。用于需要多产品协作或尚需确定操作入口的任务；单一产品编辑使用对应产品 skill，跨环境迁移使用 power-platform-release。"
---

# Power Platform 网页任务总入口

把用户的业务目标转成可核验的网页操作。此套件需要浏览器控制能力和用户可用的微软租户会话；skill 本身不提供登录、权限或浏览器工具。

## 执行

1. 读取 [浏览器约定](references/browser-contract.md)。从会话和页面确定目标租户、环境、对象、操作范围及已授予的权限。缺少关键目标时先做只读定位。
2. 为跨产品任务建立 [任务记录](references/task-record.md)。简单单页修改只保留必要字段。
3. 按下表读取对应 skill。共享约定本轮已读且未变更时不重读。不要为路由而自动启动额外 agent。
4. 按依赖顺序操作：数据与连接 → flow/应用 → agent 工具与知识 → 测试 → 已授权的发布。用户现有对象与指定路线优先。
5. 跨产品切换后复核环境和对象标识。使用 [集成参考](references/integrations.md) 处理身份、连接、Dataverse、SharePoint、Teams 及策略问题。
6. 根据目标状态验收。分别报告已保存、已发布、已共享、已部署、已验证的状态。未运行的步骤不能标成通过。

## 路由

| 工作 | 读取 |
|---|---|
| agent、知识、主题、工具、认证、测试及本环境渠道发布 | [copilot-studio-web](../copilot-studio-web/SKILL.md) |
| 云端 flow、连接、agent 调用、运行历史 | [power-automate-web](../power-automate-web/SKILL.md) |
| Canvas / Model-driven 应用、数据源、保存发布共享 | [power-apps-web](../power-apps-web/SKILL.md) |
| Solution、环境迁移、部署管道、版本与恢复 | [power-platform-release](../power-platform-release/SKILL.md) |

具体操作超过本套件支持范围时，说明缺口，并查该产品官方文档。不要把 Power Pages、Azure、Dynamics 365 的完整管理能力视为已包含。

## 交付

给出目标对象链接、完成状态、实际验证证据、阻塞项和下一步。跨环境交付可使用 [交付记录模板](assets/delivery-record.md)。只保留支持结论所需的脱敏信息。
