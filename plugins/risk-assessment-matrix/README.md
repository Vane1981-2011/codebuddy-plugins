# 风险评估矩阵

> 把风险从形容词变成可排序的决策项

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Business%20&%20Finance-7c9cff.svg)](../../docs/SKILL-CATALOG.md#business)
[![Version](https://img.shields.io/badge/version-2.3.0-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

完成风险识别、影响×概率评分、热力图、风险登记册、缓释策略与剩余风险跟踪。

## 什么时候用它

风险讨论常停留在「高、中、低」，缺少量化依据、责任人和剩余风险视图。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

需要精算定价或监管资本计量的场景。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install risk-assessment-matrix
```

安装后直接描述任务，或显式调用 `/risk-assessment-matrix`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 业务目标、风险清单、影响与概率判断、控制措施 |
| 主要输出 | 风险矩阵、热力图、优先登记册、缓释计划与剩余风险跟踪表 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **建立风险分类与评分尺度**
2. **评估影响和发生概率**
3. **绘制热力图并确定优先级**
4. **设计缓释措施与责任人**
5. **复核剩余风险与触发条件**

## 使用示例

```text
为新业务上线建立跨部门风险登记册和季度复盘机制。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/risk-assessment-matrix/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/risk-assessment-matrix/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`风险管理` `热力图` `风险登记册` `缓释`

许可：MIT。运行说明见 [`SKILL.md`](skills/risk-assessment-matrix/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/risk-assessment-matrix.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
