# 稽影 · 多智能体信任基础设施

> 让多智能体的每一步都可追溯、可拦截

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Meta%20&%20Agents-7c9cff.svg)](../../docs/SKILL-CATALOG.md#meta)
[![Version](https://img.shields.io/badge/version-1.0.7-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

六智能体编排与宪法即代码，结合 TEP 可信执行协议、七项质量门禁和十类认知偏见交叉验证。

## 什么时候用它

多智能体系统容易出现责任不清、质量波动、偏见叠加和不可追溯。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

替代法律、审计或合规专业意见。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install jiying
```

安装后直接描述任务，或显式调用 `/jiying`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 任务目标、执行策略、约束与验收标准 |
| 主要输出 | 编排轨迹、门禁报告、偏见交叉验证、可信执行记录 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **规划任务并分配角色与权限**
2. **研究、创作、审查与执行分离**
3. **运行宪法规则和质量门禁**
4. **对关键结论做偏见交叉验证**
5. **输出可追溯的执行凭证与改进项**

## 使用示例

```text
对一份高风险分析报告执行多智能体审查与门禁验收。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/jiying/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/jiying/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`多智能体` `信任` `质量门禁` `可追溯`

许可：Apache-2.0；本插件目录内的许可证优先。运行说明见 [`SKILL.md`](skills/jiying/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/jiying.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
