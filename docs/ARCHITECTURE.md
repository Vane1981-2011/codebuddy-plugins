# 架构设计：从技能文件到可运营的能力市场

> 这个仓库不是 28 个 Markdown 文件的集合，而是一套“可发现、可安装、可执行、可验证、可分发”的 Agent 技能产品架构。

## 1. 设计目标

| 目标 | 要解决的问题 | 可检查的产物 |
|---|---|---|
| 可发现 | 用户不知道有哪些能力、也不知道该用哪个 | 首页、领域地图、搜索、独立详情页、Sitemap |
| 可理解 | 只有一个技能名，缺少输入、输出和边界 | 每个插件独立 README 与详情页 |
| 可安装 | 复制文件、改配置、手动注册，安装成本高 | marketplace + plugin.json + 一条安装命令 |
| 可执行 | 技能描述模糊，执行结果不可预期 | SKILL.md 中的触发、流程、输出与质量门 |
| 可验证 | 无法判断仓库是否完整、技能是否启用 | 目录校验、YAML 校验、链接校验、CI |
| 可分发 | 没有版本、没有发布包、无法迁移 | CHANGELOG、Release、ZIP 快照、Pages |

## 2. 五层架构

```text
L0  市场与发现层   README · 领域地图 · 搜索 · 详情页 · SEO / OG / Sitemap
        ↓
L1  能力目录层     catalog/plugins.json（单一事实源）
        ↓
L2  执行契约层     plugin.json + SKILL.md + 独立 README
        ↓
L3  质量与证据层   质量门禁 · 专业边界 · 来源说明 · CI 校验
        ↓
L4  分发与快照层   marketplace · Release ZIP · GitHub Pages · CHANGELOG
```

### L0 · 市场与发现层

**职责**：让需要能力的人在 30 秒内判断“这里有没有我要的东西”。

- 首屏只回答三个问题：是什么、给谁用、怎么开始。
- 7 大领域是导航，不是装饰；每个领域都写明能力边界和插件数量。
- 28 个插件卡片支持关键词搜索与领域筛选。
- 每个插件都有独立详情页，包含问题、输入、输出、流程、示例和“不适用”。
- 静态站提供 canonical、Open Graph、Twitter Card、Schema.org 和 sitemap。

**失败模式**：把所有技能平铺成一张长列表，用户只能靠名字猜用途。

### L1 · 能力目录层

**职责**：用一个结构化文件统一“产品语言”和“机器可读数据”。

`catalog/plugins.json` 是单一事实源，保存：

- 7 个领域：`id`、中英文名、图标、颜色、描述、数量。
- 28 个插件：名称、标题、领域、一句话、摘要、问题、输入、输出、流程、示例、不适用、标签、许可。
- 仓库元数据：schema 版本、仓库地址、更新时间。

生成链：

```text
catalog/plugins.json
  ├── .codebuddy-plugin/marketplace.json
  ├── plugins/<name>/.codebuddy-plugin/plugin.json
  ├── plugins/<name>/README.md
  ├── docs/SKILL-CATALOG.md
  ├── docs/SKILL-CATALOG.html
  └── docs/plugins/<name>.html
```

**设计原则**：人只维护一处，其他产物全部生成；生成结果进入版本控制，发布时无需依赖本地环境。

### L2 · 执行契约层

**职责**：让“技能”从一段说明变成可执行、可验收的工作流。

每个插件由三个文件构成最小闭环：

```text
plugins/<name>/
├── README.md                       # 给人看：问题、输入、输出、安装
├── .codebuddy-plugin/plugin.json   # 给市场看：名称、版本、许可、技能入口
└── skills/<name>/SKILL.md          # 给 Agent 看：触发、流程、交付契约
```

`SKILL.md` 的 frontmatter 至少包含 `name`、`description`，并统一设置 `disable: false`，保证安装后可加载。正文负责：

1. **触发条件**：什么问题应该调用它。
2. **最小输入**：没有哪些信息就不能可靠执行。
3. **执行流程**：按顺序拆成可检查的步骤。
4. **输出契约**：交付什么、以什么结构交付。
5. **边界**：什么场景不适用，哪些结论需要专业复核。

### L3 · 质量与证据层

**职责**：让“专业”不只是一种宣称，而是可追溯的证据链。

| 门禁 | 检查内容 | 失败后果 |
|---|---|---|
| 目录一致性 | 28 个插件、7 个领域、数量与名称一致 | 市场出现幽灵条目 |
| 技能可加载 | frontmatter 可解析、`disable` 不为 true | 安装后技能不可用 |
| 文档完整性 | 每个插件有 README、输入、输出、边界 | 用户无法判断适用性 |
| 链接完整性 | 站内链接、插件链接、安装链接可解析 | 用户路径中断 |
| 专业边界 | 财税、法律、投资类插件标注辅助属性 | 误导为专业结论 |
| 发布可复现 | 构建脚本可从单一事实源重建产物 | 仓库与线上不一致 |

### L4 · 分发与快照层

**职责**：让能力可以被安装、升级、迁移和归档。

- `marketplace.json`：宿主添加市场时读取的入口。
- `plugin.json`：单插件安装元数据。
- `v1.0.0` Release：完整 ZIP 快照，便于离线迁移和归档。
- GitHub Pages：公开可访问的产品展示与详情页。
- `CHANGELOG.md`：版本变更与兼容性说明。

## 3. 插件之间如何组合

单个插件解决一个明确问题；组合后形成端到端工作流。

### 财务 BP 工作流

```text
contract-risk-scanner
        ↓  识别付款、验收、违约与管辖风险
tax-risk-early-warning-engine
        ↓  检查发票、收入、成本费用与特殊业务风险
financial-bp-command-center
        ↓  量本利、客户盈利、预算与投资可行性
investment-risk-engine
        ↓  收益、回撤、组合指标复核
risk-assessment-matrix
        ↓  统一风险排序与决策建议
```

### 知识蒸馏工作流

```text
markitdown → weread-skills → cangjie-skill → doc-coauthoring
  格式统一      阅读痕迹        拆成技能        写成文档
```

### 内容生产工作流

```text
creative-origin-engine → picture-book-pipeline → video-production-pipeline
        创意辩论              版面与角色一致性          声明式视频生产
                                   ↘ pixabay-bgm-search
```

### 元能力工作流

```text
context-manager → mad-think-pipeline → jiying → context-cleanup
   跨会话记忆          并行推理与交叉验证      信任与门禁      收尾释放
```

## 4. 目录结构

```text
codebuddy-plugins/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── CHANGELOG.md
├── THIRD_PARTY_NOTICES.md
├── catalog/
│   └── plugins.json                 # 单一事实源
├── .codebuddy-plugin/
│   └── marketplace.json             # 市场入口
├── plugins/
│   └── <28 个插件>/
│       ├── README.md
│       ├── .codebuddy-plugin/plugin.json
│       └── skills/<name>/SKILL.md
├── docs/
│   ├── index.html                   # 展示站首页
│   ├── plugins/<name>.html          # 28 个详情页
│   ├── SKILL-CATALOG.html           # 可筛选的完整索引
│   ├── ARCHITECTURE.md / .html
│   ├── BENCHMARK.md / .html
│   ├── QUALITY.md / .html
│   ├── INSTALL.md / .html
│   ├── styles.css
│   ├── app.js
│   └── assets/
├── scripts/
│   ├── build_catalog.py
│   ├── build_site.py
│   └── validate_repo.py
└── .github/
    ├── ISSUE_TEMPLATE/
    ├── PULL_REQUEST_TEMPLATE.md
    └── workflows/validate.yml
```

## 5. 为什么不做成一个大而全的技能

- **安装粒度**：用户只需要财务 BP，不应该被迫安装 28 个技能。
- **维护边界**：一个插件的变更不影响其他插件的版本与许可。
- **质量责任**：每个插件都能独立验收，而不是用一个“总技能”掩盖薄弱环节。
- **组合能力**：插件通过输入输出契约组合，而不是通过复制粘贴提示词组合。
- **可发现性**：领域 → 插件 → 详情页的层级，符合用户从问题到方案的决策路径。

## 6. 版本与演进

- 插件版本以 `plugin.json` 与 `SKILL.md` 中的较新语义版本为准。
- 破坏性变更必须更新主版本，并在 `CHANGELOG.md` 中写明迁移方式。
- 新增插件必须同时更新目录、市场、README、详情页和校验规则。
- 每次发布生成完整 ZIP 快照，保证离线可迁移。

---

[返回首页](index.html) · [查看质量门禁](QUALITY.html) · [查看高星项目对标](BENCHMARK.html)
