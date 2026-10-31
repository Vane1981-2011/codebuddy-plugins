# BGM 智能搜索

> 从文案情绪找到合适的免费背景音乐

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Content%20&%20Creative-7c9cff.svg)](../../docs/SKILL-CATALOG.md#content)
[![Version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

从视频标题、描述和字幕提取情绪、风格与节奏关键词，搜索 Pixabay/Freesound 并下载匹配音乐。

## 什么时候用它

背景音乐检索依赖主观试听，关键词不准确，版权来源也难核对。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

绕过平台许可或用于侵权传播。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install pixabay-bgm-search
```

安装后直接描述任务，或显式调用 `/pixabay-bgm-search`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 视频文案、目标情绪、时长范围和来源偏好 |
| 主要输出 | 英文音乐关键词、候选曲目清单、预览/下载链接与来源记录 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **从文案提取情绪、风格和节奏**
2. **翻译并扩展检索关键词**
3. **按来源和时长过滤**
4. **试听并比较匹配度**
5. **记录许可信息并下载**

## 使用示例

```text
为一条三分钟的科技产品视频寻找克制、未来感的 BGM。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/pixabay-bgm-search/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/pixabay-bgm-search/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`BGM` `Pixabay` `音乐搜索` `版权`

许可：MIT。运行说明见 [`SKILL.md`](skills/pixabay-bgm-search/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/pixabay-bgm-search.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
