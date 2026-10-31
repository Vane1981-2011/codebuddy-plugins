# τ 增强诊断

> 并行推理与交叉验证版全链路诊断

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Engineering-7c9cff.svg)](../../docs/SKILL-CATALOG.md#engineering)
[![Version](https://img.shields.io/badge/version-3.0.0-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

在标准 τ 诊断上叠加 S1–S4 并行推理、智能体分派、跨层验证和置信度量化。

## 什么时候用它

多系统、多角色的复杂故障，单线诊断容易漏因或误判。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

单点、低风险的简单性能问题。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install tau-diagnosis-zcode
```

安装后直接描述任务，或显式调用 `/tau-diagnosis-zcode`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 复杂系统链路、角色分工、日志与历史诊断 |
| 主要输出 | 多路径诊断、冲突证据、置信度评分与增强改进方案 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **拆分系统边界与诊断假设**
2. **并行运行多条诊断路径**
3. **跨层对照日志、指标和访谈**
4. **量化结论置信度**
5. **合并为带优先级的整改计划**

## 使用示例

```text
对跨模型、工具和人工审核的系统做联合故障诊断。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/tau-diagnosis-zcode/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/tau-diagnosis-zcode/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`增强诊断` `并行推理` `交叉验证` `置信度`

许可：MIT。运行说明见 [`SKILL.md`](skills/tau-diagnosis-zcode/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/tau-diagnosis-zcode.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
