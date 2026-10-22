# 任务记录与跨产品交接

只在任务涉及多个对象、部署或中断恢复时建完整记录。小修改可以在会话中记录同样的必要信息。

## 记录字段

```yaml
goal: 用户要求的结果
authorization: 已授权操作、目标范围、明确排除的操作
tenant: 组织标识，不含凭据
environment: 名称及 ID 或可核查 URL
experience: standard / github-copilot / unknown
objects:
  - product: Copilot Studio / Power Automate / Power Apps
    name: 实际名称
    id_or_url: 实际标识
    state: observed / edited / saved / published / shared / verified / blocked
dependencies: 相关 solution、flow、连接引用、数据源及所属环境
last_verified: 已观察到的状态、时间与证据
next_action: 下一步和所需前置状态
blockers: 缺失权限、输入或功能；没有则为空
```

字段是记录提示，不是要求用户逐项填写的表格。先从已有对话和网页读取信息。不要把“unknown”当作默认正确值；只有依赖它的变更需要等到确认。

## 交接内容

跨产品交接至少携带对象 ID、环境 ID、输入输出字段、身份方式、已验证状态。比如 agent 调用 flow 时，交接 flow 的 ID、solution、输入参数类型、输出字段和错误语义，而不是只传 flow 名称。

身份需要区分：制作者登录账号、连接拥有者、运行中的最终用户。使用作者凭据运行工具不能视为最终用户拥有同样的数据权限。

## 完成状态

| 状态 | 可支持的结论 | 不能据此推出 |
|---|---|---|
| 已保存 | 页面变更已持久化 | 最终用户已得到新版 |
| 已发布 | 对象对应版本已发布 | 已授权所有用户访问 |
| 已共享 | 指定主体获得所分配权限 | 数据源权限和许可证已齐备 |
| 已导入 | 目标环境有 solution 与组件 | 连接、flow、agent 渠道均已可用 |
| 已运行验证 | 指定身份、输入和渠道下的结果符合预期 | 所有身份和路径均正确 |

报告验证的具体范围。没有证据时写“未验证”，不要写“预计通过”。
