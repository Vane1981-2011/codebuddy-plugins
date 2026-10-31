# CodeBuddy Skills v1.0.0

**把专业工作交给可验证的 Agent。**

这是 CodeBuddy Skills 第一次以“产品级开源仓库”的形式发布：28 个可安装插件、7 大领域、统一目录、独立文档、静态展示站、质量门禁与离线快照。

## 本次发布包含

### 28 个可安装插件

- **元技能与智能体（7）**：上下文管理器、专家市场同步器、第一性原理推理、上下文学习机制、稽影、MAD 深度推理管线、技能智能中枢。
- **商业与金融（5）**：财务 BP 指挥中心、税务风险预警引擎、合同风险扫描器、风险评估矩阵、投资风险量化引擎。
- **知识与文档（5）**：仓颉技能工坊、结构化文档共创、MarkItDown 文档转换、PDF 全能工具箱、微信读书助手。
- **软件工程（5）**：高级前端交付、单文件应用工程护栏、多模态桥接层、τ 全链路诊断、τ 增强诊断。
- **内容与创意（4）**：创意策源引擎、AI 绘本生产线、声明式视频生产线、BGM 智能搜索。
- **办公与协作（1）**：上下文清理协议。
- **行业垂直（1）**：浏览器自动化执行器。

### 产品化改造

- 统一目录：`catalog/plugins.json` 作为单一事实源。
- 统一安装：marketplace + plugin.json + 一条安装命令。
- 统一文档：28 个独立 README + 28 个在线详情页。
- 统一质量：六道发布门禁 + CI 校验。
- 统一分发：Release ZIP + GitHub Pages + CHANGELOG。

### 关键修复

- 21 个技能从 `disable: true` 修复为可加载状态。
- 修复 marketplace 描述截断、分类不一致、主页指向错误。
- 修复 `mad-think-pipeline` YAML frontmatter 解析错误。
- 统一插件版本与技能版本。

## 安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install financial-bp-command-center
```

## 在线体验

<https://vane1981-2011.github.io/codebuddy-plugins/>

## 校验

```bash
python3 scripts/build_catalog.py
python3 scripts/build_site.py
python3 scripts/validate_repo.py
```

## 许可

- 根仓库：MIT
- `jiying`：Apache-2.0
- 第三方来源：见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)

## 已知边界

- 插件是工作流说明，不是沙箱；涉及外部命令、浏览器自动化、文件写入时请先在隔离环境验证。
- 财税、法律、投资、安全类输出是辅助材料，不替代持证专业人士意见。
- Star 与下载量不是本次发布的目标；本次优化的是可发现性、安装体验、文档质量与发布体系。

---

[返回首页](README.md) · [变更记录](CHANGELOG.md)
