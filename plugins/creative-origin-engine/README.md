# 创意策源引擎

> 让创意先经受攻击，再成为方案

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Content%20&%20Creative-7c9cff.svg)](../../docs/SKILL-CATALOG.md#content)
[![Version](https://img.shields.io/badge/version-2.0.1-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

三智能体并行提出建构、解构和数据锚定视角，经 Critic 与 Defender 交叉验证，输出二十分制策划案。

## 什么时候用它

单一模型容易生成看似完整但缺乏反证、数据锚点和执行路径的创意。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

需要立即产出的简单文案或纯灵感清单。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install creative-origin-engine
```

安装后直接描述任务，或显式调用 `/creative-origin-engine`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 一句创意、目标受众、资源约束与成功标准 |
| 主要输出 | 多视角分析、攻防记录、评分卡、可执行策划案与技能包 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **三个独立智能体并行分析**
2. **Critic 攻击关键假设**
3. **Defender 逐条辩护**
4. **融合重构并按二十分制评分**
5. **低于阈值自动返工，达标后交付**

## 使用示例

```text
策划一个面向财务负责人的 AI 读书会。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/creative-origin-engine/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/creative-origin-engine/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`创意` `多智能体` `辩论` `策划`

许可：MIT。运行说明见 [`SKILL.md`](skills/creative-origin-engine/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/creative-origin-engine.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
