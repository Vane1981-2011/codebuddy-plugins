# MarkItDown 文档转换

> 把多种格式统一成可检索的 Markdown

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Knowledge%20&%20Docs-7c9cff.svg)](../../docs/SKILL-CATALOG.md#knowledge)
[![Version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

将 PDF、Office、图片、音频、网页、表格、压缩包和视频链接转换为 Markdown，保留结构信息。

## 什么时候用它

资料格式分散，难以进入知识库、检索和后续分析流程。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

要求像素级还原排版或替代专业 OCR 校正。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install markitdown
```

安装后直接描述任务，或显式调用 `/markitdown`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | PDF、DOCX、PPTX、XLSX、图片、音频、HTML、CSV、JSON 或链接 |
| 主要输出 | 结构化 Markdown、提取日志与失败项清单 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **识别文件类型与可用解析路径**
2. **提取文本、表格和元数据**
3. **对图片或音频按需启用 OCR/转写**
4. **清洗格式并保留标题层级**
5. **输出 Markdown 和转换报告**

## 使用示例

```text
把一批年报 PDF 和路演 PPT 转成可检索的 Markdown 资料库。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/markitdown/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/markitdown/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`Markdown` `OCR` `文档转换` `知识库`

许可：MIT。运行说明见 [`SKILL.md`](skills/markitdown/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/markitdown.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
