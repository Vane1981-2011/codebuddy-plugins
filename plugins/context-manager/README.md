# 上下文管理器

> 让下一次对话记得这一次的结论

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Meta%20&%20Agents-7c9cff.svg)](../../docs/SKILL-CATALOG.md#meta)
[![Version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

在对话开始加载项目上下文，在结束前沉淀进展、决策与待办，避免重复解释和上下文断层。

## 什么时候用它

跨会话工作时反复复述背景，关键决策散落在历史对话里。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

一次性闲聊，或没有复用价值的临时问答。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install context-manager
```

安装后直接描述任务，或显式调用 `/context-manager`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 当前任务、历史对话、已有上下文文件 |
| 主要输出 | 结构化上下文卡、决策记录、待办清单与更新后的上下文文件 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **定位项目上下文文件与最近一次检查点**
2. **提取目标、约束、已完成事项和未决问题**
3. **只保留影响后续决策的信息并写入检查点**
4. **新会话加载摘要后再进入任务执行**

## 使用示例

```text
加载「渠道预算复盘」的上下文，继续上周未完成的差异分析。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/context-manager/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/context-manager/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`上下文` `记忆` `跨会话` `协作`

许可：MIT。运行说明见 [`SKILL.md`](skills/context-manager/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/context-manager.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
