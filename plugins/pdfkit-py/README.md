# PDF 全能工具箱

> 五十条命令覆盖 PDF 全生命周期

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Knowledge%20&%20Docs-7c9cff.svg)](../../docs/SKILL-CATALOG.md#knowledge)
[![Version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

以纯 Python 完成 PDF 阅读、编辑、转换、表单、加密、签名、OCR、书签、压缩和拆分合并。

## 什么时候用它

PDF 操作散落在多个工具，批量处理和可复现性差。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

绕过文档权限或处理无权访问的材料。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install pdfkit-py
```

安装后直接描述任务，或显式调用 `/pdfkit-py`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | PDF 文件与目标操作说明 |
| 主要输出 | 处理后的 PDF、提取结果、校验报告与命令记录 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **识别 PDF 结构和操作目标**
2. **选择最小必要命令集**
3. **在副本上执行并检查页数、字体和表单**
4. **输出处理结果与校验记录**
5. **保留可复现的命令清单**

## 使用示例

```text
批量拆分合同附件、提取表单字段并生成校验清单。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/pdfkit-py/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/pdfkit-py/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`PDF` `OCR` `表单` `批处理`

许可：MIT。运行说明见 [`SKILL.md`](skills/pdfkit-py/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/pdfkit-py.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
