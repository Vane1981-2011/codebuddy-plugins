# 上下文学习机制

> 管理注意力预算，而不是堆更多提示词

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Meta%20&%20Agents-7c9cff.svg)](../../docs/SKILL-CATALOG.md#meta)
[![Version](https://img.shields.io/badge/version-1.1.0-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

解释并应用上下文内学习、注意力分配、遗忘边界与探索—利用策略，优化复杂任务的上下文组织。

## 什么时候用它

上下文越长越容易失焦，重要约束被噪声淹没，模型在探索与收敛之间失衡。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

替代模型训练，或承诺改变模型参数。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install in-context-learning
```

安装后直接描述任务，或显式调用 `/in-context-learning`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 任务目标、上下文材料、已有尝试与失败记录 |
| 主要输出 | 上下文编排策略、注意力预算、遗忘风险清单与探索计划 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **识别任务真正依赖的上下文信号**
2. **按相关度、时效和风险分层**
3. **设计探索—利用的切换条件**
4. **在关键节点主动验证而非假设记忆**
5. **清理低价值上下文并保留证据**

## 使用示例

```text
为一份长报告设计上下文分层，避免关键结论被资料淹没。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/in-context-learning/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/in-context-learning/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`上下文学习` `注意力` `记忆` `探索`

许可：MIT。运行说明见 [`SKILL.md`](skills/in-context-learning/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/in-context-learning.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
