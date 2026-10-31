# 财务 BP 指挥中心

> 把业财融合方法变成可计算的经营工具

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Business%20&%20Finance-7c9cff.svg)](../../docs/SKILL-CATALOG.md#business)
[![Version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

覆盖四讲二十二模块与八个工具模型，从量本利、客户盈利到预算监控和投资可行性。

## 什么时候用它

财务分析停留在报表解释，难以前置到业务决策，也缺少统一的计算口径。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

替代法定会计处理或审计意见。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install financial-bp-command-center
```

安装后直接描述任务，或显式调用 `/financial-bp-command-center`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 收入、成本、客户、供应商、预算与投资参数 |
| 主要输出 | 计算模型、结构化 JSON、经营诊断与决策建议 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **确认业务场景与口径**
2. **选择量本利、盈利或投资模型**
3. **校验输入与计算过程**
4. **输出敏感性分析和经营建议**
5. **形成可复用的管理驾驶舱**

## 使用示例

```text
用客户盈利模型判断哪些客户应提价、收缩或重点维护。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/financial-bp-command-center/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/financial-bp-command-center/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`财务BP` `业财融合` `量本利` `预算` `投资`

许可：MIT。运行说明见 [`SKILL.md`](skills/financial-bp-command-center/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/financial-bp-command-center.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
