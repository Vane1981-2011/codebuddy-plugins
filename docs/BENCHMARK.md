# 高星项目拆解：我们借鉴了什么，又如何落到本仓库

> 对标不是为了复制外观，而是找出“一个技能仓库为什么会被看见、被理解、被安装、被信任”的结构性原因。

## 1. 采样方法与快照

- 采样时间：2026-10-31
- 数据来源：GitHub REST API `repos/{owner}/{repo}` 的 `stargazers_count`
- 采样对象：Agent Skills / Claude Skills 方向上公开、结构完整、可安装的代表性仓库
- 说明：Star 数会随时间变化，本文只记录采样时点，不将热度等同于质量。

| 仓库 | Stars（采样） | 代表性结构 |
|---|---:|---|
| [`obra/superpowers`](https://github.com/obra/superpowers) | 309,458 | 方法论清晰、多宿主安装、技能目录内附脚本与测试 |
| [`anthropics/skills`](https://github.com/anthropics/skills) | 185,347 | 官方技能规范、模板与极简目录 |
| [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) | 112,011 | Hero 视觉、生命周期图、30 秒 Quick Start、`docs/` 与 `evals/` |
| [`Leonxlnx/taste-skill`](https://github.com/Leonxlnx/taste-skill) | 106,365 | 单一价值主张明确、垂直场景清晰 |
| [`ComposioHQ/awesome-claude-skills`](https://github.com/ComposioHQ/awesome-claude-skills) | 78,357 | Banner、徽章、TOC、分类目录、一句话说明 |
| [`vercel-labs/skills`](https://github.com/vercel-labs/skills) | 37,301 | CLI 快速开始、安装与排错文档、信息层级简洁 |
| [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills) | 29,038 | 大数字徽章、领域表、按宿主安装、分类目录 |

## 2. 七个共性，而不是七个巧合

### 2.1 首屏先回答“是什么、给谁用、解决什么问题”

高星仓库不会用“赋能、闭环、生态”开场，而是用一句可验证的话说明用途。用户在前 10 秒内要能判断：

- 这是技能、插件、CLI，还是教程？
- 它解决的是哪类任务？
- 我是否属于目标用户？
- 我需要付出多少安装成本？

**本仓库的落点**：首屏标题“把专业工作交给可验证的 Agent”，副标题直接列出 28 个技能覆盖的领域，并提供“30 秒安装”和“浏览技能”两个明确入口。

### 2.2 安装路径必须短到可以背下来

高星项目的 Quick Start 通常只有 1–3 条命令，并且命令块可以被直接复制。

**本仓库的落点**：

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install financial-bp-command-center
```

首页、每个插件 README、每个详情页都提供同样的安装路径，避免用户在不同页面看到不同说法。

### 2.3 分类是导航，不是标签墙

成熟仓库按“用户任务”分类，而不是按文件名、作者或技术栈分类。分类数量通常控制在 5–10 个，每个分类下有 3–8 个条目。

**本仓库的落点**：7 大领域、28 个插件，每个领域都有明确的能力描述和数量；首页提供领域卡片、筛选器与领域到插件的映射表。

### 2.4 每个技能都要有独立的“适用边界”

高星项目不只写“能做什么”，还写“什么时候不要用”。这是专业感的来源，也是降低误用的关键。

**本仓库的落点**：`catalog/plugins.json` 为每个插件设置 `problem`、`input`、`output`、`workflow`、`example`、`not_for` 六个字段；每个详情页都有 `NOT FOR` 区块。

### 2.5 文档、示例和评估是产品的一部分

成熟仓库通常包含：

- `README.md`：入口与快速开始
- `docs/`：安装、架构、贡献、排错
- `examples/` 或 `evals/`：真实输入与预期输出
- `CHANGELOG.md`：版本与兼容性
- `LICENSE`、`SECURITY.md`、Issue 模板：可信度基础设施

**本仓库的落点**：新增 `docs/ARCHITECTURE.md`、`docs/INSTALL.md`、`docs/QUALITY.md`、`docs/BENCHMARK.md`、`CHANGELOG.md`、`SECURITY.md`、Issue 表单与 CI。

### 2.6 视觉不是为了好看，而是为了建立信息层级

高星仓库的 Banner、截图、架构图和徽章，承担的是“快速定位信息”的功能：

- Banner 说明品牌与价值主张。
- 架构图说明系统边界。
- 截图说明真实产品形态。
- 徽章说明许可、版本、平台与构建状态。

**本仓库的落点**：新增 `docs/assets/banner.svg`、`mark.svg`、首页截图、社交预览图；首页使用五层架构图、领域地图和插件卡片建立层级。

### 2.7 发布与维护机制决定“看起来是否可信”

有 Release、有 CI、有 Issue 模板、有版本记录的仓库，更容易被判断为“有人维护”。这不是装饰，而是降低使用者的决策风险。

**本仓库的落点**：`v1.0.0` Release、ZIP 快照、GitHub Pages、`validate.yml`、Issue 表单、PR 模板、`THIRD_PARTY_NOTICES.md`。

## 3. 结构映射：借鉴项 → 本仓库实现

| 借鉴项 | 来源项目 | 本仓库实现 | 可检查产物 |
|---|---|---|---|
| 一句话价值主张 | `taste-skill`、`superpowers` | 首屏标题与副标题 | `docs/index.html` |
| 30 秒安装 | `agent-skills`、`vercel-labs/skills` | 两条命令 + 复制按钮 | 首页、README、详情页 |
| 领域分类 | `awesome-claude-skills` | 7 大领域、28 插件 | `catalog/plugins.json` |
| 独立技能说明 | `anthropics/skills` | 28 个独立 README | `plugins/*/README.md` |
| 架构与生命周期 | `agent-skills` | 五层架构 + 执行契约 | `docs/ARCHITECTURE.md` |
| 评估与质量 | `superpowers` | CI 校验 + 发布门禁 | `.github/workflows/validate.yml` |
| 视觉与社交预览 | 多个高星仓库 | Banner、截图、OG 图 | `docs/assets/` |
| 版本与发布 | 成熟开源项目 | `v1.0.0` + ZIP | GitHub Releases |
| 贡献入口 | 成熟开源项目 | Issue 表单、PR 模板、贡献指南 | `.github/` |

## 4. 我们刻意没有照搬的部分

- **不追求技能数量**：28 个可安装插件比 300 个无法判断质量的条目更有用。
- **不制造虚假热度**：不购买 Star、不写“10 万用户”这类无法验证的数字。
- **不把 Star 当目标**：Star 是结果，不是产品指标；先解决“被看见、被理解、被安装、被信任”。
- **不复制他人文案与结构细节**：只借鉴信息架构与工程实践，所有插件说明基于本仓库真实能力重写。
- **不把专业判断包装成确定结论**：财税、法律、投资类插件明确标注辅助属性与复核要求。

## 5. 结论

高星项目的共同点不是“写得更多”，而是：

1. 让用户在 10 秒内知道这是什么。
2. 让用户在 30 秒内完成安装。
3. 让用户在 3 分钟内判断一个技能是否适合自己。
4. 让用户在遇到问题时知道去哪里反馈。
5. 让贡献者知道如何新增或修改一个技能。

本仓库的改造围绕这五件事展开，而不是围绕“再写 28 段介绍”展开。

---

[返回首页](index.html) · [查看架构](ARCHITECTURE.html) · [查看质量门禁](QUALITY.html)
