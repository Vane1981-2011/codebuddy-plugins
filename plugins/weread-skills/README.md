# 微信读书助手

> 把阅读痕迹整理成可用的知识笔记

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Knowledge%20&%20Docs-7c9cff.svg)](../../docs/SKILL-CATALOG.md#knowledge)
[![Version](https://img.shields.io/badge/version-3.0.0-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

搜索书籍、管理书架、读取划线和书评、查看阅读统计，并生成 Obsidian 知识笔记。

## 什么时候用它

阅读数据分散在应用内，划线、想法和书评难以进入个人知识库。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

抓取非本人账号数据或绕过平台权限。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install weread-skills
```

安装后直接描述任务，或显式调用 `/weread-skills`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 微信读书账号状态、书籍/书架信息、阅读目标 |
| 主要输出 | 书籍信息、笔记与划线、阅读统计、Obsidian Markdown |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **检查登录状态与数据访问权限**
2. **拉取书籍、书架、划线和书评**
3. **按主题聚合观点与引用**
4. **生成结构化阅读笔记**
5. **输出到 Obsidian 并保留来源**

## 使用示例

```text
把本月读完的三本书整理成主题笔记和行动清单。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/weread-skills/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/weread-skills/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`微信读书` `阅读笔记` `Obsidian` `知识管理`

许可：MIT。运行说明见 [`SKILL.md`](skills/weread-skills/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/weread-skills.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
