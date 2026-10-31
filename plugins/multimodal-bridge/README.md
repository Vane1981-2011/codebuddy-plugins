# 多模态桥接层

> 为纯文本模型接上图像、视频和 3D 能力

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Engineering-7c9cff.svg)](../../docs/SKILL-CATALOG.md#engineering)
[![Version](https://img.shields.io/badge/version-1.1.0-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

提供 OCR、生图、图片搜索、3D/特效与视频理解五条桥接路径，按任务自动选择。

## 什么时候用它

文本模型无法直接处理视觉素材，工具切换和格式转换成本高。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

未经授权的人脸识别或版权素材复制。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install multimodal-bridge
```

安装后直接描述任务，或显式调用 `/multimodal-bridge`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 图片、视频、文本需求与目标输出格式 |
| 主要输出 | 提取文本、生成图片、搜索素材、3D/视频结果与处理记录 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **识别输入模态和目标任务**
2. **选择最少必要的桥接路径**
3. **调用对应工具并校验结果**
4. **转换为目标格式**
5. **记录来源、参数和失败回退**

## 使用示例

```text
从产品图片提取文字并生成一组营销配图。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/multimodal-bridge/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/multimodal-bridge/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`多模态` `OCR` `生图` `视频`

许可：MIT。运行说明见 [`SKILL.md`](skills/multimodal-bridge/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/multimodal-bridge.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
