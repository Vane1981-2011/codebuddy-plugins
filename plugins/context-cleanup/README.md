# 上下文清理协议

> 任务收尾时释放上下文，而不是一直背着它

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Office%20&%20Collaboration-7c9cff.svg)](../../docs/SKILL-CATALOG.md#office)
[![Version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

在实质任务完成后识别可释放内容、移除冗余中间结果、压缩记忆写入，降低 token 与积分消耗。

## 什么时候用它

长任务结束后上下文仍占用资源，中间结果和缓存不断累积。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

任务执行中清理仍可能需要的上下文。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install context-cleanup
```

安装后直接描述任务，或显式调用 `/context-cleanup`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 任务完成状态、上下文记录、记忆与缓存清单 |
| 主要输出 | 可释放清单、压缩后的记忆、保留证据与清理记录 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **确认任务已完成并核对交付物**
2. **区分证据、决策和临时中间结果**
3. **压缩长期记忆并清理缓存**
4. **保留可追溯的最小证据集**
5. **记录释放量与后续风险**

## 使用示例

```text
结束一份长报告后清理重复草稿，只保留结论和证据索引。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/context-cleanup/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/context-cleanup/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`上下文清理` `Token` `记忆压缩` `收尾`

许可：MIT。运行说明见 [`SKILL.md`](skills/context-cleanup/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/context-cleanup.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
