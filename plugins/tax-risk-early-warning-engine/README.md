# 税务风险预警引擎

> 用指标和阈值把税务风险前置

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Business%20&%20Finance-7c9cff.svg)](../../docs/SKILL-CATALOG.md#business)
[![Version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

覆盖发票、特殊业务、收入、成本费用四类十五项指标，提供三区阈值、建安参数与风险解释。

## 什么时候用它

税务风险往往在稽查或申报后才暴露，指标口径分散且缺少可解释的预警线。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

代替税务机关认定或专业税务意见。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install tax-risk-early-warning-engine
```

安装后直接描述任务，或显式调用 `/tax-risk-early-warning-engine`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 发票、收入、成本费用、业务类型与申报数据 |
| 主要输出 | 风险指标看板、三区预警、证据清单与整改建议 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **确认行业与业务场景**
2. **计算十五项风险指标**
3. **按绿/黄/红三区判定**
4. **关联凭证和业务证据**
5. **输出整改优先级与复核清单**

## 使用示例

```text
对建安企业季度发票和成本费用数据做税务风险扫描。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/tax-risk-early-warning-engine/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/tax-risk-early-warning-engine/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`税务风险` `金税四期` `建安` `预警指标`

许可：MIT。运行说明见 [`SKILL.md`](skills/tax-risk-early-warning-engine/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/tax-risk-early-warning-engine.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
