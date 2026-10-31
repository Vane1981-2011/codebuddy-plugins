# 单文件应用工程护栏

> 让单文件 HTML 应用也能工程化交付

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Engineering-7c9cff.svg)](../../docs/SKILL-CATALOG.md#engineering)
[![Version](https://img.shields.io/badge/version-2.2.0-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

为单文件 HTML 应用提供正则、选择器、存储隔离、题库校验、导航协议和按钮规范等护栏。

## 什么时候用它

单文件应用开发快但容易埋下状态污染、选择器冲突和导航死路。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

大型框架工程的完整架构评审。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install spa-engineering-guard
```

安装后直接描述任务，或显式调用 `/spa-engineering-guard`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 单文件 HTML 应用代码、交互说明与验收标准 |
| 主要输出 | 工程检查报告、修复建议与上线前验收清单 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **扫描 DOM、CSS、存储和事件结构**
2. **检查正则与选择器陷阱**
3. **验证状态隔离和导航闭环**
4. **检查按钮、图标和色彩规范**
5. **输出阻断项与修复顺序**

## 使用示例

```text
上线前审查一个答题类单文件应用的状态和导航。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/spa-engineering-guard/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/spa-engineering-guard/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`单文件应用` `HTML` `工程护栏` `质量`

许可：MIT。运行说明见 [`SKILL.md`](skills/spa-engineering-guard/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/spa-engineering-guard.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
