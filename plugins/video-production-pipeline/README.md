# 声明式视频生产线

> 用组件和参数复现视频生产

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Content%20&%20Creative-7c9cff.svg)](../../docs/SKILL-CATALOG.md#content)
[![Version](https://img.shields.io/badge/version-4.0.0-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

基于 Remotion 的声明式视频流程，覆盖参考拆解、脚本、组件、封面、BGM、多分辨率与质检。

## 什么时候用它

视频制作依赖手工时间线，难以复用、批量化和版本控制。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

未经授权复制他人视频或音乐。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install video-production-pipeline
```

安装后直接描述任务，或显式调用 `/video-production-pipeline`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 主题、参考视频、脚本/素材、时长与输出规格 |
| 主要输出 | Remotion 工程、渲染视频、封面、BGM 清单与质检报告 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **逆向拆解参考视频节奏和视觉**
2. **编写分镜与动画参数**
3. **搭建可复用组件**
4. **匹配封面和背景音乐**
5. **多分辨率渲染并做质检**

## 使用示例

```text
为一条知识类短视频建立可复用的模板和生产流程。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/video-production-pipeline/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/video-production-pipeline/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`视频` `Remotion` `模板` `渲染`

许可：MIT。运行说明见 [`SKILL.md`](skills/video-production-pipeline/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/video-production-pipeline.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
