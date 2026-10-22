# 操作手册与支持范围

“已覆盖”表示有基于官方资料的操作流程，**不表示已经在真实租户完成验收**。所有页面路径均需结合当前界面重新定位。

| 产品/能力 | 操作参考 | 本版覆盖 |
|---|---|---|
| 通用网页控制 | [浏览器约定](../skills/power-platform-web/references/browser-contract.md) | 定位、状态验证、重试、中断恢复、身份与授权 |
| Copilot Studio 体验 | [体验识别](../skills/copilot-studio-web/references/experience-detection.md) | standard 主路径；GitHub harness 有限分支 |
| agent 配置 | [配置手册](../skills/copilot-studio-web/references/authoring.md) | 创建、指令、知识、主题、工具、认证 |
| agent 测试与发布 | [测试发布](../skills/copilot-studio-web/references/testing-publishing.md) | 草稿测试、渠道配置、分发状态、真实渠道验证 |
| Teams 试点 | [Teams 分发](../skills/copilot-studio-web/references/teams-pilot.md) | 安全组聊天权限、安装入口、可发现性与权限验证 |
| Power Automate | [云端流程](../skills/power-automate-web/references/cloud-flows.md) | solution 流程、连接、版本、运行历史、错误调查 |
| agent 调用流程 | [集成手册](../skills/power-automate-web/references/agent-tools.md) | 同步主路径、有条件的异步路径、参数与结果验证 |
| Power Apps Canvas | [画布应用](../skills/power-apps-web/references/canvas-apps.md) | 控件、公式、数据、flow、保存发布共享 |
| Power Apps Model-driven | [模型驱动应用](../skills/power-apps-web/references/model-driven-apps.md) | 表页面、表单视图、导航、角色与共享 |
| 跨环境发布 | [Solutions](../skills/power-platform-release/references/solutions.md) | 包类型、依赖、连接引用、环境变量、导入导出 |
| 部署管道 | [Pipelines](../skills/power-platform-release/references/pipelines.md) | 运行已有管道、审批状态、阶段与包版本 |
| 发布后故障 | [恢复参考](../skills/power-platform-release/references/recovery.md) | 历史与层、修复、旧版重部署、环境恢复边界 |
| 其他微软服务 | [集成参考](../skills/power-platform-web/references/integrations.md) | SharePoint、Teams、Entra、Dataverse、数据策略的关联检查 |

## 需要另行扩展的范围

- GitHub Copilot harness 的完整 workflow、skills、memory 及发布生命周期。
- Power Automate Desktop 的机器连接、桌面录制和无人值守运行。
- Power Pages、Dynamics 365 和 Azure 各产品的完整配置与部署。
- 新建企业部署管道平台、全租户 DLP 治理、许可采购与容量规划。
- 国家云、政府云、旧版 Teams 精简体验等专属环境的逐项验收。

这些范围出现实际任务时，先查该产品官方文档，再决定补 references 还是新 skill。不会因为属于微软生态就默认受支持。
