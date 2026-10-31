# 仓颉技能工坊

> 把一本书蒸馏成一组可执行技能

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Knowledge%20&%20Docs-7c9cff.svg)](../../docs/SKILL-CATALOG.md#knowledge)
[![Version](https://img.shields.io/badge/version-1.0.3-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

将书籍、长视频、播客、课程或访谈中的框架、原则与方法论提取为原子化、可复用的技能。

## 什么时候用它

长内容读完就忘，笔记是摘要而不是可调用的工作方法。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

只做简单摘要、书评或角色扮演。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install cangjie-skill
```

安装后直接描述任务，或显式调用 `/cangjie-skill`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 书籍、字幕、播客转录、课程材料或访谈记录 |
| 主要输出 | 技能清单、触发条件、执行步骤、案例与技能文件 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **识别内容结构与核心命题**
2. **提取框架、原则和可操作步骤**
3. **合并重复概念并建立依赖**
4. **为每个技能编写触发与验收标准**
5. **生成可安装的技能包**

## 使用示例

```text
把一本经营分析书蒸馏成客户盈利、预算复盘和定价三类技能。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/cangjie-skill/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/cangjie-skill/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`知识蒸馏` `拆书` `技能生成` `RIA`

许可：MIT。运行说明见 [`SKILL.md`](skills/cangjie-skill/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/cangjie-skill.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
