# 质量门禁：让“专业”成为可检查的条件

> 一个技能仓库最容易犯的错误，是只展示能力，不展示边界；只展示结果，不展示证据。这里把发布条件写成可以自动检查的规则。

## 1. 发布前的六道门

| 门禁 | 检查对象 | 通过条件 | 自动化 |
|---|---|---|---|
| G1 目录完整性 | `catalog/plugins.json` | 28 个插件、7 个领域、每个领域数量匹配、名称不重复 | `validate_repo.py` |
| G2 技能可加载 | 28 个 `SKILL.md` | frontmatter 可解析、含 `name` 与 `description`、`disable` 不为 true | `validate_repo.py` |
| G3 插件可安装 | 28 个 `plugin.json` | JSON 合法、名称与目录一致、包含 `skills` 入口、版本合法 | `validate_repo.py` |
| G4 文档完整 | 28 个插件 README | 含安装命令、输入、输出、工作流、适用边界 | `validate_repo.py` |
| G5 展示一致 | `docs/` | 首页、28 个详情页、目录页存在；无占位符；关键链接可解析 | `validate_repo.py` |
| G6 发布可复现 | 生成脚本 | 从单一事实源重建后，目录、市场与文档一致 | CI |

## 2. 28/28 的含义

本仓库把“完整”定义为：

- **28/28 插件有独立 README**：不是把根 README 复制 28 次，而是每个插件有自己的问题、输入、输出、流程、示例与边界。
- **28/28 技能默认启用**：修复历史 `disable: true`，安装后即可加载。
- **28/28 插件进入市场清单**：`marketplace.json`、`plugin.json`、磁盘目录三方一致。
- **28/28 详情页可访问**：每个插件都有独立 URL，支持被搜索、被分享、被引用。

## 3. 本地校验

```bash
python3 scripts/build_catalog.py
python3 scripts/build_site.py
python3 scripts/validate_repo.py
```

校验器会输出：

```text
OK 28 plugins / 7 domains
OK 28 SKILL.md frontmatter
OK 28 plugin.json
OK 28 plugin README
OK 28 detail pages
OK marketplace = catalog
OK no placeholders
```

任何一项失败都会以非零状态退出，CI 会阻止合并。

## 4. 专业边界

以下领域的插件明确标注“辅助材料”属性：

| 领域 | 插件示例 | 边界 |
|---|---|---|
| 税务 | `tax-risk-early-warning-engine` | 不替代税务师意见，不构成申报结论 |
| 法律 | `contract-risk-scanner` | 不替代律师审阅，不构成法律意见 |
| 投资 | `investment-risk-engine` | 不构成投资建议，历史数据不代表未来收益 |
| 财务 | `financial-bp-command-center` | 依赖输入数据质量，需业务与财务共同复核 |
| 安全 | `jiying` | 信任机制降低风险，不保证绝对安全 |

## 5. 内容质量规则

- 一句话说明不超过两行，先说“解决什么问题”，再说“怎么做到”。
- 输入必须是用户能提供的材料，而不是“请提供完整业务数据”这类空话。
- 输出必须是可验收的交付物，例如报告、矩阵、清单、脚本或决策备忘。
- 每个插件至少有一个真实调用示例。
- 每个插件必须写明“不适用”，避免能力被过度承诺。
- 不使用无法验证的用户量、收入、排名或效果数据。

## 6. 问题分级与响应

| 级别 | 定义 | 处理方式 |
|---|---|---|
| P0 | 安装失败、技能不可加载、市场清单损坏 | 24 小时内修复并发布补丁版本 |
| P1 | 输出结构错误、关键计算逻辑错误 | 3 个工作日内修复 |
| P2 | 文档缺失、示例不清、链接失效 | 下一个版本修复 |
| P3 | 表达优化、新增场景、视觉改进 | 进入 backlog |

## 7. 不做什么

- 不用 Star 数证明质量。
- 不用“全自动”“零误差”描述专业判断。
- 不把未经验证的第三方内容包装成自研能力。
- 不在没有输入的情况下生成确定性结论。
- 不为了数量而拆出低价值的“伪插件”。

---

[返回首页](index.html) · [查看架构](ARCHITECTURE.html) · [查看安装指南](INSTALL.html)
