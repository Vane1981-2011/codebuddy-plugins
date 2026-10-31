# 浏览器自动化执行器

> 双通道、时钟校准与五层守护的自动化模板

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-Industry-7c9cff.svg)](../../docs/SKILL-CATALOG.md#industry)
[![Version](https://img.shields.io/badge/version-2.1.0-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

面向合法授权的浏览器自动化场景，提供双通道并行、RTT 校准、拟人化点击、自适应轮询与容错守护。

## 什么时候用它

浏览器自动化在时序、网络抖动和页面变化下容易失败，也缺少可观测的容错层。

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

绕过平台规则、攻击系统或未经授权的抢购/刷单。

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install snap-up-assassin
```

安装后直接描述任务，或显式调用 `/snap-up-assassin`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | 授权场景、目标页面、操作步骤与风险约束 |
| 主要输出 | 自动化脚本、选择器配置、校准数据与执行日志 |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

1. **确认授权范围和平台规则**
2. **校准本地时钟与网络 RTT**
3. **配置双通道和自适应轮询**
4. **加入点击、失败和退出守护**
5. **回放日志并做合规复盘**

## 使用示例

```text
为内部测试环境编写一个带超时和失败恢复的页面操作脚本。
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/snap-up-assassin/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/snap-up-assassin/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：`浏览器自动化` `RTT校准` `容错` `合规`

许可：MIT。运行说明见 [`SKILL.md`](skills/snap-up-assassin/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情](https://vane1981-2011.github.io/codebuddy-plugins/plugins/snap-up-assassin.html) · [提交问题](https://github.com/Vane1981-2011/codebuddy-plugins/issues)
