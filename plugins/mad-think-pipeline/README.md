# MAD 深度推理管线

> 把复杂判断拆成可交叉验证的并行路径

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Meta%20&%20Agents-7c9cff.svg)](../../docs/SKILL-CATALOG.md#meta)
[![Version](https://img.shields.io/badge/version-2.0.0-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

以 S1–S4 管线完成问题分解、并行推理、交叉验证与综合，适合架构决策和根因诊断。

## 什么时候用它

单线推理容易过早收敛，复杂问题缺少多路径对照和置信度校准。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

需要秒级回答的轻量问题。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install mad-think-pipeline
```

安装后直接描述任务，或显式调用 `/mad-think-pipeline`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 复杂问题、约束、可用证据与决策期限 |
| 主要输出 | 问题分解、并行推理路径、交叉验证结果、综合结论 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **S1 建立问题结构与判断标准**
2. **S2 从不同假设并行推理**
3. **S3 对照证据、冲突与置信度**
4. **S4 综合为可执行结论并标注边界**

## 使用示例

```text
对「自建还是采购」做多路径技术经济论证。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/mad-think-pipeline/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/mad-think-pipeline/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`深度推理` `并行` `交叉验证` `架构决策`

许可：MIT。运行说明见 [`SKILL.md`](skills/mad-think-pipeline/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/mad-think-pipeline.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
