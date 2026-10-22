# Teams 试点发布

适用 standard harness。核查日期：2026-10-22。先完成[测试与发布](testing-publishing.md)中的发布前检查。

## 明确使用范围

“让某组成员在 Teams 私聊 agent”与“把 agent 加到团队频道/群聊”不同。先从请求确定目标。Teams 的团队所对应的 Microsoft 365 组不一定是可共享的安全组；核对组标识和支持类型。

只授予聊天权限，不授予协作编辑、评估或对话记录查看权限。若当前共享面板提示会附加环境角色，先核对必要性及已有授权。共享条件涉及认证方式和租户权限，按当前页面和[官方共享说明](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-share-bots)核查；不要为了出现共享按钮随意更改认证。

## 操作与证据

| 步骤 | 网页锚点与动作 | 完成判据 |
|---|---|---|
| 授予聊天访问 | agent 顶部 `… > Share`，输入指定安全组，检查仅聊天/使用权限，提交 Share | 回读共享列表中的组和权限；未授权通知时不勾邮件邀请 |
| 配置渠道 | `Channels > Teams and Microsoft Copilot`；只需 Teams 时不额外勾选 Microsoft Copilot；`Add channel` | 显示已连接，范围符合任务 |
| 取得试点入口 | 渠道面板 `Availability options > Copy link` | 取得该 agent 的安装入口；在交付中提供，不自动群发 |
| 可发现性 | 任务需要时用 `Show to my teammates and shared users`，核对受众，更新显示设置 | 显示 Added to Teams；仅对已共享受众发现，不推定全组织可见 |
| 验收 | 授权的试点用户安装/打开入口，新会话运行用例 | 能聊天、认证正确、数据与工具结果符合该用户权限 |

先发布至少一次，再配置渠道。链接能打开不证明用户已有聊天权限。组织商店展示、管理员批准、用户安装和实际聊天分别记录。[官方 Teams 渠道手册](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams)

若目标是组织目录，按已有授权使用管理员提交分支；不能为小组试点直接选 `Show to everyone in my org`。平台要求管理员处理时，交付具体待处理配置与状态。

## 团队频道或群聊

用户明确要求团队频道/群聊时，再读官方 Teams 文档的相关章节。该分支涉及额外会话范围与权限前提，不把它当作小组私聊分发的等价方案。若需要扩大 agent 可访问范围，先完成影响说明并确认新增范围。仅安装失败时，先检查共享、认证与组织策略，不开放全组织来排错。
