# 官方资料与研究结论

核查日期：2026-10-22。研究只使用微软官方文档与微软官方样例站点作为产品依据。技能安装方式另参考 OpenAI 官方文档。

操作手册对官方流程做必要摘要；网页验证、重试与交付格式是本套件的设计。文档更新不代表目标租户已经获得同样功能。实际执行仍须核对当前页面和适用范围。

| 研究主题 | 文档 | 主要用途 |
|---|---|---|
| Copilot Studio | [研究记录](copilot-studio.md) | 框架差异、制作、工具、测试、渠道、认证 |
| Power Automate / Power Apps | [研究记录](power-automate-power-apps.md) | 云端流程、草稿发布、应用类型、数据与共享 |
| ALM / 治理 | [研究记录](power-platform-alm.md) | 环境、Solution、依赖、管道、恢复与策略 |

## 官方最佳实践入口

- [Copilot Studio 实施指导](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/overview)：以项目生命周期组织实施与管理。
- [实施主题索引](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/implement-overview)：工具、主题、编排、集成及渠道。
- [Microsoft Copilot Studio Implementation Guide](https://microsoft.github.io/CopilotStudioSamples/guides/implementation-guide/)：架构与项目评审框架。本次核查了网页概述和版本记录，未把下载幻灯片逐页核查算作已完成。
- [Power Platform 自动化建议](https://learn.microsoft.com/en-us/power-platform/well-architected/operational-excellence/automate-tasks)：选用适合工作负载的工具，并纳入测试和运维。

## 应用到套件的设计

产品文档支持明确区分环境、组件、发布和权限。套件据此拆分三个产品 skill 与一个发布 skill；共同网页行为放总入口。这个拆分是设计推论，不是微软对 agent skill 的规定。

当前文档存在兼容分支。例如同步 agent flow 与新基础设施异步响应的要求不同。手册保留条件和出处，不把其中一条规则当成全产品通用事实。

来源正文已经通过浏览工具核查。完整官方 URL 保留在各研究文档和操作手册内。维护者遇到入口、限制或许可变化时，应重新打开相应原页，不根据搜索摘要改规则。
