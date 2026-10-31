# 第一性原理推理

> 把复杂问题拆到不可再拆的事实

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Meta%20&%20Agents-7c9cff.svg)](../../docs/SKILL-CATALOG.md#meta)
[![Version](https://img.shields.io/badge/version-2.0.0-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

以准备、执行、质检、复盘四阶段闭环组织推理，结合三层推理体系与工程化交付检查。

## 什么时候用它

复杂任务容易被经验类比带走，缺少可复核的假设、证据和验收标准。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

已有明确标准答案的简单事实查询。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install first-principles-reasoning
```

安装后直接描述任务，或显式调用 `/first-principles-reasoning`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 问题陈述、目标、约束、可获得的证据 |
| 主要输出 | 问题树、关键假设、证据链、方案比较、质检结论与复盘 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **界定目标、边界与成功标准**
2. **拆解事实、假设与因果链**
3. **生成并比较多条解决路径**
4. **用验收门禁检查证据和结论**
5. **沉淀可复用的方法与模板**

## 使用示例

```text
从第一性原理拆解「是否应该进入一个新区域市场」。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/first-principles-reasoning/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/first-principles-reasoning/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`推理` `问题拆解` `决策` `质检`

许可：MIT。运行说明见 [`SKILL.md`](skills/first-principles-reasoning/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/first-principles-reasoning.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
