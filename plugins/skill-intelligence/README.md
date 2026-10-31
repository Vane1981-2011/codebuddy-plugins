# 技能智能中枢

> 从「找技能」升级为「管理能力资产」

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Meta%20&%20Agents-7c9cff.svg)](../../docs/SKILL-CATALOG.md#meta)
[![Version](https://img.shields.io/badge/version-2.0.0-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

联合搜索多个技能市场，按场景匹配评分，并检查冗余、冲突、质量与生命周期。

## 什么时候用它

技能数量增长后，发现难、选择难、重复安装多，缺少健康度和升级策略。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

未经审查自动安装来源不明的代码。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install skill-intelligence
```

安装后直接描述任务，或显式调用 `/skill-intelligence`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 任务场景、已有技能、质量偏好、市场来源 |
| 主要输出 | 候选技能评分表、推荐安装路径、健康检查与升级/归档建议 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **解析场景与能力缺口**
2. **联合检索多个技能市场**
3. **按相关性、质量、依赖和维护状态评分**
4. **检查重复与冲突**
5. **生成安装、升级或归档计划**

## 使用示例

```text
为「建安企业税务风险体检」匹配技能组合并检查重复项。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/skill-intelligence/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/skill-intelligence/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`技能发现` `评分` `健康度` `生命周期`

许可：MIT。运行说明见 [`SKILL.md`](skills/skill-intelligence/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/skill-intelligence.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
