# Solution 打包与导入

核查日期：2026-10-22。页面名称是定位线索，点击目标必须来自当前页面。Copilot Studio 的 solution 导入/导出资料标明适用于 standard harness；遇到其他运行模式，先核实该模式的官方交付路径。

## 打包前检查

Solution 是配置组件的交付包。开发环境通常维护 unmanaged solution；测试和生产使用 managed 发布包。此处 managed solution 与 Managed Environment 是两个概念。前者是包类型，后者是环境治理能力。[官方概念](https://learn.microsoft.com/en-us/power-platform/alm/solution-concepts-alm)

确认组件清单、源版本、目标已有版本、目标数据位置、连接主体及部署后触发行为。现有业务数据、外部 SharePoint 列表、秘密值和渠道设置不能一概当成包的一部分。

## 组装组件

| 页面锚点 | 输入或动作 | 后置状态 |
| --- | --- | --- |
| Power Apps → 环境选择器 → Solutions | 选择源环境和现有 unmanaged solution | Overview 中唯一名称、publisher、版本匹配任务 |
| 仅需新包时：New solution | 填显示名称、唯一名称、现有组织 publisher、版本 | 新 solution 可打开；不要随意改变 preferred solution |
| solution → Add existing | 加入本次 agent、flow、app 和必要组件 | Objects 清单包含预期对象 |
| Copilot Studio solution → Agent/Workflow → … → Advanced → Add required objects | 对新增的主题、flow、环境变量补依赖 | 所需对象进入包；与源清单逐项对照 |

新建 solution 的唯一名称保存后不能改。复用组织 publisher。不要从 solution 中直接删 agent 的主题组件来修复导出；应回到 Copilot Studio 编辑主题。[创建 solution](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-solution)、[agent 导入导出](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-solutions-import-export)

有自定义 connector 时，先交付 connector，再交付 connection reference 与 agent solution。缺依赖时补齐源包或按顺序部署基底 solution，不能忽略错误继续。

## 配置连接和环境变量

Connection 是账户连接；connection reference 是包中指向该连接的组件。网页入口为 solution → New → More → Connection Reference。选 connector 和正确身份的 connection；保存后检查引用者。添加到 solution 的旧 flow 不一定已经改用 connection reference。[连接引用](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-connection-reference)

Environment variable 是各环境分别设置的参数。网页入口为 solution → New → More → Environment variable。记录 schema name、类型、目标值来源及消费它的组件。Current Value 优先于 Default Value。不要把开发站点地址作为生产默认值，也不要用普通文本参数保存秘密。Secret 类型需要 Azure Key Vault 配置。[环境变量](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/environmentvariables)

仅给需要目标替换的值保留定义；是否携带 Current Value 由发布设计决定。移除“当前值随包传递”不等于删除变量定义。导入时若未显示参数页，仍检查目标现有值是否适用。

## 网页导出

1. 确认本次组件已保存，并发布需要发布的源定制。共享开发环境中先检查 `Publish all changes` 是否会激活其他人的未发布改动；必要时从组件页只发布本次对象。
2. 在 Solutions 选源 unmanaged solution → Export。
3. 核对版本与 Managed/Unmanaged 类型。面向下游环境一般导出 Managed；源码保留可另存 Unmanaged。
4. 按组织要求运行 solution checker。其检查结果不能代替业务测试。
5. 等导出结束，确认浏览器下载的实际文件、大小和版本。记录包路径及目标；未出现文件不能报告导出完成。

Managed solution 和 Default Solution 不能直接导出。官方导出向导要求关注已发布组件。[导出手册](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/export-solutions)

## 网页导入

1. 切到目标环境。再次核对环境 ID 和当前 solution 版本。
2. Solutions → Import solution → This device，选择已核对的包；若使用 host 历史包，核对所选记录的版本和来源。
3. 阅读包摘要与 Advanced settings。特别检查 `Enable Plugin steps and flows included in the solution`。启用 flow 可能触发业务处理；取消勾选也不会停用已有 flow。
4. 按连接引用选择目标连接。按环境变量填目标值。检查所用身份能访问目标数据。
5. 处理 missing dependencies。未解决前不提交。
6. 若目标已有该 solution，按下一节选择 Update 或 Upgrade。
7. 提交 Import 一次。等待后台任务，使用 Solutions → See history 查看结果。失败时读取错误或 Download Log File。

Managed 包的定制以已发布状态导入；unmanaged 包的定制可能需要发布。导入 unmanaged 会覆盖相应现有定制，不能靠删除 solution 容器撤销。[导入手册](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/import-update-export-solutions)

## 更新方式

| 方式 | 选择依据 | 不能忽略的影响 |
| --- | --- | --- |
| Update | 需要增加或更新组件，保留目标旧组件 | 源包已删除的组件仍留在目标 |
| Upgrade | 本次发布需要移除旧组件 | 新包未包含的旧组件可能删除，关联数据需评估 |
| Stage for Upgrade | 已有明确数据迁移或分阶段升级设计 | 后续 Apply Solution Upgrade 才完成清理，不是普通更新的默认选项 |

升级向导可能默认选 Upgrade。先核对差异和授权，不直接接受默认项。版本需高于现有版本。不要使用 `Overwrite customizations` 消除未知差异。[更新与升级](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/update-solutions)

## 目标验证

从 solution history 记录结果、版本、时间、错误码及 Activity ID。只有 Success 才能证明该导入操作成功。[历史记录](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/solution-history)

随后检查：

- flow 的连接有效、目标参数正确、启用状态符合授权；受控测试能在运行历史找到结果。
- app 打开目标数据，关键屏幕或表单可用；共享和数据权限符合目标用户。
- agent 的主题、知识和工具齐全；重新核实认证；按产品 skill 测试、发布并验证渠道。导入不自动证明渠道可用。

失败时转 [recovery.md](recovery.md)，不要把绿色导入通知当作完整业务验收。
