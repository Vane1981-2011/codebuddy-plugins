# AI 绘本生产线

> 从故事结构到版面一致性的完整流水线

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Content%20&%20Creative-7c9cff.svg)](../../docs/SKILL-CATALOG.md#content)
[![Version](https://img.shields.io/badge/version-3.5.0-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

覆盖七种作品类型、四种角色系统和五种版面模式，保持角色与风格一致性。

## 什么时候用它

绘本生成常见角色漂移、版面失衡和图文叙事脱节。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

普通单张图片生成或商业版权不明的角色复刻。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install picture-book-pipeline
```

安装后直接描述任务，或显式调用 `/picture-book-pipeline`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 故事主题、目标读者、作品类型、画风与篇幅 |
| 主要输出 | 分镜脚本、角色设定、页面文案、插图提示词与版面文件 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **确定作品类型与叙事结构**
2. **建立角色和视觉圣经**
3. **拆分分镜与页面文案**
4. **生成插图并校验一致性**
5. **按版面模式排版和质检**

## 使用示例

```text
制作一本面向儿童的国风双语绘本。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/picture-book-pipeline/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/picture-book-pipeline/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`绘本` `分镜` `角色一致性` `版面`

许可：MIT。运行说明见 [`SKILL.md`](skills/picture-book-pipeline/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/picture-book-pipeline.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
