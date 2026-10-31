# 结构化文档共创

> 先对齐读者，再写内容

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Knowledge%20&%20Docs-7c9cff.svg)](../../docs/SKILL-CATALOG.md#knowledge)
[![Version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

通过上下文转移、分段迭代和读者测试，完成提案、技术规格、决策文档等结构化内容。

## 什么时候用它

文档一次性生成后逻辑松散，读者看不懂，修改也缺少明确依据。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

纯营销文案或需要法律定稿的正式合同。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install doc-coauthoring
```

安装后直接描述任务，或显式调用 `/doc-coauthoring`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 文档目标、读者、背景材料、约束与现有草稿 |
| 主要输出 | 文档大纲、分段草稿、审阅意见与读者验证结果 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **明确读者、目的和决策动作**
2. **转移必要上下文并建立大纲**
3. **分段共创和逐段确认**
4. **模拟目标读者做理解测试**
5. **修订并输出最终版本**

## 使用示例

```text
为管理层编写一份新业务立项决策文档。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/doc-coauthoring/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/doc-coauthoring/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`文档` `提案` `技术规格` `共创`

许可：MIT。运行说明见 [`SKILL.md`](skills/doc-coauthoring/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/doc-coauthoring.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
