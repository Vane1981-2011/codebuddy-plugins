# 贡献指南

感谢你愿意改进 CodeBuddy Skills。这个仓库的目标不是收集尽可能多的提示词，而是维护一组**可安装、可验证、边界清晰**的专业工作流。

## 可以贡献什么

- 修复插件的执行逻辑、输入输出契约或文档错误。
- 新增一个真实存在、可独立安装的技能。
- 改进展示站的可访问性、可读性或搜索体验。
- 补充测试、校验规则、示例或排错说明。
- 报告安装失败、技能不可加载、链接失效等问题。

## 新增插件的准入条件

一个插件必须同时满足以下条件，才会被合并：

1. **有明确问题**：能说清楚它解决什么任务，而不是“提升效率”。
2. **有最小输入**：用户能提供哪些材料；缺少哪些信息时不能可靠执行。
3. **有可验收输出**：报告、矩阵、清单、脚本、决策备忘等。
4. **有执行流程**：至少 3 个可检查的步骤。
5. **有适用边界**：明确写出“不适用”的场景。
6. **有真实示例**：一个可以直接复制执行的调用示例。
7. **有许可与来源**：自研或明确标注第三方来源与许可。
8. **不重复**：与现有插件的能力重叠时，优先改进现有插件，而不是新建近似条目。

## 目录规范

```text
plugins/<plugin-name>/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/<plugin-name>/SKILL.md
```

- `plugin-name` 使用小写 kebab-case，并与目录、`plugin.json`、`SKILL.md` 的 `name` 完全一致。
- `SKILL.md` 必须有 YAML frontmatter，至少包含 `name` 与 `description`。
- 已发布技能必须设置 `disable: false`，保证安装后可加载。
- 版本使用语义化版本：`MAJOR.MINOR.PATCH`。

## 修改目录

`catalog/plugins.json` 是单一事实源。新增或修改插件时，必须同步更新：

- 插件标题、领域、一句话、摘要、问题、输入、输出、流程、示例、不适用、标签、许可。
- 对应领域数量 `count`。
- 如新增领域，需要同时更新 7 大领域的展示与导航。

## 本地验证

```bash
python3 scripts/build_catalog.py
python3 scripts/build_site.py
python3 scripts/validate_repo.py
```

提交前请确认：

- 28/28 插件数量与目录一致。
- 所有 `SKILL.md` frontmatter 可解析。
- 所有 `plugin.json` 是合法 JSON。
- `marketplace.json` 与目录一致。
- 首页与 28 个详情页存在，站内链接可解析。
- 没有 `G-XXXXXXXXXX`、`TODO`、`TBD` 等占位符。

## 提交信息

建议使用：

```text
feat(plugin): add <name>
fix(plugin): correct <name> workflow
docs: clarify install steps
chore(ci): add catalog validation
```

## Pull Request

PR 描述请包含：

1. 解决的问题。
2. 改动范围。
3. 验证方式与结果。
4. 是否涉及许可、第三方来源或专业边界。
5. 截图（如涉及展示站变更）。

## 专业内容边界

- 财税、法律、投资、安全类内容必须标注“辅助材料，不替代持证专业人士意见”。
- 不得承诺收益、通过率、节税金额或其他无法验证的结果。
- 不得使用真实客户数据、合同原文、身份证号、银行账号等敏感信息作为示例。
- 引用第三方内容时必须保留来源与许可。

## 行为准则

参与本项目即表示同意遵守 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。

---

[返回首页](README.md) · [查看质量门禁](docs/QUALITY.md) · [查看架构](docs/ARCHITECTURE.md)
