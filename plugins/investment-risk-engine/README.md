# 投资风险量化引擎

> 用收益、回撤与组合指标检验投资判断

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Business%20&%20Finance-7c9cff.svg)](../../docs/SKILL-CATALOG.md#business)
[![Version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

基于组合绩效与风险模型计算夏普比率、最大回撤、资产配置和组合优化，并生成 HTML 分析报告。

## 什么时候用它

投资分析容易只看收益，忽略回撤、波动、相关性和组合风险。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

构成投资建议或承诺未来收益。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install investment-risk-engine
```

安装后直接描述任务，或显式调用 `/investment-risk-engine`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 资产收益序列、权重、基准与风险偏好 |
| 主要输出 | 绩效指标、风险归因、组合优化结果与 HTML 报告 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **校验时间序列和资产权重**
2. **计算收益、波动、夏普和最大回撤**
3. **分析相关性与集中度**
4. **运行约束下的组合优化**
5. **生成可复核的报告与假设说明**

## 使用示例

```text
比较三种资产配置方案的收益风险特征并生成报告。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/investment-risk-engine/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/investment-risk-engine/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`投资` `组合` `夏普比率` `最大回撤`

许可：MIT。运行说明见 [`SKILL.md`](skills/investment-risk-engine/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/investment-risk-engine.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
