# 专家市场同步器

> 让能力库跟着专家市场持续更新

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Meta%20&%20Agents-7c9cff.svg)](../../docs/SKILL-CATALOG.md#meta)
[![Version](https://img.shields.io/badge/version-2.1.0-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

检测专家与技能市场的新增和更新，按领域相关性匹配，输出可审计的安装与升级建议。

## 什么时候用它

技能市场更新频繁，人工盘点成本高，容易漏掉真正匹配的新能力。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

无来源校验的第三方插件批量安装。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install expert-sync
```

安装后直接描述任务，或显式调用 `/expert-sync`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 个人领域画像、已有技能清单、市场更新源 |
| 主要输出 | 增量清单、领域匹配报告、安装/更新建议 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **读取本地技能清单与领域偏好**
2. **拉取市场新增和版本变化**
3. **按领域、依赖和重复度评分**
4. **生成安装计划并保留变更记录**

## 使用示例

```text
检查财务与税务方向最近有哪些值得安装的新专家。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/expert-sync/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/expert-sync/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`技能市场` `同步` `匹配` `生命周期`

许可：MIT。运行说明见 [`SKILL.md`](skills/expert-sync/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/expert-sync.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
