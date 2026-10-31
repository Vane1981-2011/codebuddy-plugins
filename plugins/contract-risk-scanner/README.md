# 合同风险扫描器

> 签字之前，先把不利条款找出来

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Business%20&%20Finance-7c9cff.svg)](../../docs/SKILL-CATALOG.md#business)
[![Version](https://img.shields.io/badge/version-2.0.0-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

扫描六类高风险条款，按六种谈判立场加权，输出结构化风险报告与谈判备忘。

## 什么时候用它

合同审阅依赖经验，责任、付款、验收和管辖等关键条款容易漏看。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

替代执业律师的正式法律意见。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install contract-risk-scanner
```

安装后直接描述任务，或显式调用 `/contract-risk-scanner`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 合同文本、交易背景、己方立场与底线 |
| 主要输出 | 条款风险分级、Excel 报告、修改建议与谈判备忘 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **识别合同类型与己方立场**
2. **扫描责任、解约、验收、付款、IP、管辖条款**
3. **按立场和影响程度加权**
4. **给出替代条款与谈判优先级**
5. **输出需专业复核的法律边界**

## 使用示例

```text
以乙方立场审查一份系统实施合同的责任和验收条款。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/contract-risk-scanner/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/contract-risk-scanner/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`合同审查` `风险条款` `谈判` `法律科技`

许可：MIT。运行说明见 [`SKILL.md`](skills/contract-risk-scanner/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/contract-risk-scanner.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
