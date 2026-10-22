# Canvas 应用网页手册

文档核查：2026-10-22。步骤是官方操作入口的摘要；验证方法是套件设计。尚未在用户租户执行。

## 1. 新建或修改

**输入：** 应用链接或名称、环境、目标界面、数据源、读写范围、交付状态。

1. 已有应用从 `Apps` 选择 `Edit`。新应用从 `Create > Create from blank` 进入，选择响应式、平板或手机尺寸，再输入名称。
2. 进入 Power Apps Studio 后，核对应用名、屏幕树和当前选中控件。
3. 用 `Insert` 增加所需控件。修改公式前记录目标控件、属性及原公式，避免改错同名按钮或属性。
4. 使用预览核对布局与交互。涉及提交、删除或流程按钮时，仅使用已授权测试数据。

建立 canvas app 需要相应创建权限；当前创建指南明确列出 Environment Maker。来源：[Create a blank canvas app](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/create-blank-app)。

## 2. 连接数据

1. 在 Studio 选择 `Data > Add data`。
2. 选择指定连接器与已授权连接，核对实际身份、站点/数据库及表。不要仅凭显示名绑定。
3. 添加数据源后，配置 Gallery 的 `Items`、表单的 `DataSource` 等目标属性。
4. 在预览核对字段类型、空值、读取结果和允许的写入。返回数据源检查测试记录。

**成功证据：** 数据源出现在应用列表；控件读取的是指定对象；一次测试操作形成预期结果。连接创建成功不代表运行用户拥有数据权限。

来源：[Add data connections](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/add-data-connection)。

## 3. 调用 Power Automate

1. 打开 Studio 左侧 `Power Automate` 面板，选择 `Add a flow`，或按需求创建流程。
2. 现有流程需在当前环境可访问并具有 Power Apps 触发器。用流程详情确认身份，不套用 Copilot Studio 的触发器。
3. 流程出现在 `In your app` 后，在目标行为属性加入 `流程名.Run(...)`；保留该属性原有逻辑，并按实际输入契约填参数。
4. 若在外部修改流程，回到面板中的流程菜单选择 `Refresh`，核对新的输入，再保存应用。
5. 预览中调用一次，并关联流程运行实例与应用显示结果。

**注意：** 添加流程不会自动产生正确的按钮行为。客户端传入值不能当作权限证明；在流程侧验证关键业务参数。

来源：[Use Power Automate pane](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/working-with-flows)。

## 4. 保存与发布

1. `Save` 保存编辑版本。用可见成功状态确认保存完成。
2. 需要交付给现有使用者时，选择 `Publish > Publish this version`。已有授权覆盖本次发布时直接完成。
3. 从 `Apps > 应用菜单 > Details > Versions` 核对 `Live` 版本。
4. 重新打开或刷新运行中的应用，验证用户看到的版本。

保存不改变终端用户版本。发布后，仍已打开旧版应用的用户需要刷新。恢复历史版本后，也要核对实际 Live 版本。

来源：[Save and publish canvas apps](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/save-publish-app)。

## 5. 共享与验证

1. 应用保存并发布后，从 `Apps > 目标应用 > Share` 打开共享面板。
2. 输入指定用户或 Entra 安全组。按任务选择 `User` 或 `Co-Owner`，不要为了使用权限授予共同所有者。
3. 核对数据源、连接、网关和流程的依赖权限。对 Dataverse，检查相应安全角色。
4. 提交前核对面板中的通知选项。若用户未授权发通知，关闭可选通知；无法关闭时先交付待确认的共享项。
5. 提交后在 `Manage access` 核对受众与权限。使用已授权测试身份打开链接并完成核心路径。

用户只要求共享应用时，先完成可执行的应用 User 共享，单独报告数据权限缺口。若已有授权明确包含“向同一试点组授予指定列表的读取权限”，且当前身份有权操作，可继续完成该列表的最小授权，无需重复询问。不能把这种授权扩大到整个 SharePoint 站点。

**故障判断：** 应用可打开但无数据时，查数据权限、连接和筛选条件；看不到新界面时，查 Live 版本与刷新；流程参数不匹配时，查 Refresh 与按钮公式。

来源：[Share a canvas app](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/share-app)。
