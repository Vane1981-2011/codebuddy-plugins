# τ 全链路诊断

> 定位智能体系统真正的时延与能力瓶颈

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Engineering-7c9cff.svg)](../../docs/SKILL-CATALOG.md#engineering)
[![Version](https://img.shields.io/badge/version-2.0.0-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

用 τ-minimization 方法做四层时延诊断、能力堆叠审计和复利闭环设计。

## 什么时候用它

智能体系统变慢或变差时，容易只优化模型，却忽略路由、上下文、工具和验收环节。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

没有链路数据时的纯主观性能判断。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install tau-diagnosis
```

安装后直接描述任务，或显式调用 `/tau-diagnosis`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 系统目标、链路数据、能力清单与问题表现 |
| 主要输出 | 全链路诊断报告、瓶颈排序、能力堆叠建议与改进闭环 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **建立端到端任务链路**
2. **分层测量认知、执行、校验和收尾时延**
3. **定位主要瓶颈与次生问题**
4. **设计能力堆叠与路由优化**
5. **定义复测指标和闭环**

## 使用示例

```text
诊断一个研究型智能体为什么总在最后一步返工。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/tau-diagnosis/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/tau-diagnosis/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`τ诊断` `时延` `能力审计` `闭环`

许可：MIT。运行说明见 [`SKILL.md`](skills/tau-diagnosis/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/tau-diagnosis.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
