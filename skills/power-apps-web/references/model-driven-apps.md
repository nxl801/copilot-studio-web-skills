# 模型驱动应用网页手册

文档核查：2026-10-22。模型驱动应用围绕 Dataverse 数据模型组织界面。Dataverse 是 Power Platform 的业务数据服务。本手册未在真实租户验证。

## 1. 建立或定位应用

**输入：** 环境、solution、应用、Dataverse 表、页面和导航要求、目标角色。

1. 在 Power Apps 选择目标环境，再进入 `Solutions`。
2. 打开项目的未托管 solution。新建时使用 `New > App > Model-driven app`，输入名称和说明。
3. 通过 `Add page > Dataverse table` 选择业务需要的表。不要因为教程示例使用 Account/Contact 就把这两张表加入业务应用。
4. 在 `Pages` 与 `Navigation` 检查页面与顺序；选择页面后配置需要的表单、视图等组件。

需要环境与相应创建角色。官方建议大多数情况下不要直接在 Default Solution 中开发自定义项。来源：[Create a model-driven app](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-model-driven-app)。

## 2. 组件、保存与验证

1. 先检查实际表、列与关系。缺失数据模型时确认业务字段，不用示例表代替。
2. 在对应组件编辑器修改表单、视图和导航。区分“从应用隐藏组件”和“删除数据表/列”。删除数据结构超出普通页面修改范围。
3. 按当前编辑器完成保存与发布。若用户只要准备修改，保存后准确报告仍未发布的组件。
4. 使用 `Play` 打开运行界面，核对导航、列表、表单与允许的业务动作。

**成功证据：** 目标表与页面均可定位；发布后的应用显示预期组件；测试记录读写正确。设计器预览中看到数据只证明当前作者能访问，不能证明业务用户权限。

这些验证方法是本套件建议。发布按钮和 `Play` 入口依据 [Create a model-driven app](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-model-driven-app)。

## 3. 角色与共享

安全角色定义用户能对表执行的操作。共享应用不代替表和记录权限。

1. 从 `Apps > 目标应用 > … > Share` 打开共享面板。
2. 核对指定用户、团队或安全角色。对自定义表，确认角色包含业务需要的权限与数据范围。
3. 仅使用任务授权的角色分配。角色不存在或权限不足时保留配置清单，交给有权限的管理员处理。
4. 共享后，从 `Details` 获取 Web link。提供链接即可；发送邮件或发布消息需对应授权。
5. 用允许的测试身份核验应用可见性、表数据范围和关键动作。

**失败分层：** 看不到应用，先查共享/角色；能进入但看不到记录，查表权限和记录范围；按钮操作拒绝，查相应权限。不要把用户提升为管理员来绕过错误。

来源：[Share a model-driven app](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/share-model-driven-app)。

## 4. 与 Canvas 的交付差异

| 检查项 | Canvas | Model-driven |
| --- | --- | --- |
| 页面构成 | 屏幕、控件、公式 | 表、表单、视图、导航 |
| 数据 | 多种连接器 | 以 Dataverse 模型为中心 |
| 共享验证 | 应用权限与各数据源权限 | 应用角色、表权限及记录范围 |
| 发布验证 | 检查 Live 版本并刷新 | 检查应用及关联组件发布状态，再 Play |

此表是对官方流程的设计归纳。跨环境导入与依赖验证使用[发布管理 skill](../../power-platform-release/SKILL.md)。
