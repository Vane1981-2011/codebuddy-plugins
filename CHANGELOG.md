# Changelog

All notable changes to this repository are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and [Semantic Versioning](https://semver.org/).

## [1.0.0] - 2026-10-31

### Added

- 新增统一能力目录 `catalog/plugins.json`，作为 7 大领域、28 个插件的单一事实源。
- 新增 28 个独立插件 README，包含问题、安装、输入、输出、工作流、示例、不适用与交付契约。
- 新增公开展示站 `docs/index.html`、28 个插件详情页与 `docs/SKILL-CATALOG.html`。
- 新增 `docs/ARCHITECTURE.md`、`docs/BENCHMARK.md`、`docs/QUALITY.md`、`docs/INSTALL.md`。
- 新增 `docs/assets/` 品牌标识、Banner、首页截图与社交预览图。
- 新增 GitHub Issue 表单、PR 模板与 `validate.yml` CI 工作流。
- 新增 MIT 根许可、`jiying` Apache-2.0 插件许可与第三方来源说明。
- 新增 `v1.0.0` 离线发布包与 GitHub Pages 展示站。

### Changed

- 重新组织 28 个插件为 7 大领域：元技能与智能体、商业与金融、知识与文档、软件工程、内容与创意、办公与协作、行业垂直。
- 标准化 `marketplace.json` 与 28 个 `plugin.json`：统一名称、摘要、版本、作者、分类、首页、仓库、许可与技能入口。
- 修复 21 个插件的 `disable: true` 状态，确保安装后可加载。
- 重写根 README，围绕“是什么、怎么装、能做什么、凭什么信”组织信息层级。
- 将各插件主页从单一 GitHub 仓库地址统一到插件详情页。
- 修复 `mad-think-pipeline` 的 YAML frontmatter 引号错误。

### Fixed

- 修复 marketplace 中部分描述被截断、分类不一致、主页指向错误仓库的问题。
- 修复插件版本与 `SKILL.md` 版本不一致的问题，统一取较新的语义版本。
- 修复展示站缺失的导航页、详情页与站内链接。
- 修复静态站的 canonical、Open Graph、Twitter Card、Schema.org 与 sitemap。

### Security

- 新增安全策略与私密报告渠道。
- 在 README、插件详情页与质量文档中补充专业判断边界与数据脱敏提示。
- CI 校验 JSON、YAML、目录一致性、文档完整性与占位符。

## [0.4.1] - 2025-08-06

### Added

- 新增 `jiying` 多智能体信任基础设施。
- 新增 `creative-origin-engine` 创意策源引擎。
- 批量注册本地技能到 CodeBuddy 插件市场。

### Changed

- 统一插件市场的基础元数据格式。

---

[返回首页](README.md) · [发布说明](RELEASE_NOTES.md) · [质量门禁](docs/QUALITY.md)
