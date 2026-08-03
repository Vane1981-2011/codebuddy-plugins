---
name: jiying
description: >
  多Agent信任基础设施——宪法即代码。6Agent编排(Planner→Researcher→Creator→Reviewer) + 康德/马尔库塞/海德格尔三条哲学规则自动阻断/警告AI输出。
  TEP v1.0可信执行协议 · 7项质量门禁 · 10种认知偏见交叉验证 · 不确定性预算 · 断点恢复。
  触发条件：用户需要多Agent协作、AI信任验证、宪法检查、质量门禁。
  关键词：稽影、jiying、多Agent、信任、宪法、编排、AI Agent、trust、constitution。
---

# 稽影 (Jiying) · 多Agent信任基础设施

> 稽察审视，追影溯源 — 让每一次AI执行都变得可验证

## 概述

稽影是一个带价值宪法的多 Agent 知识工作编排系统。你输入一个意图，多个 AI Agent 协作完成——同时三条宪法确保你始终是决策者。

```
用户意图 → Planner → Researcher → Creator → Reviewer → 质量门禁 → 导出
              ↑          ↑          ↑          ↑
          宪法系统    守护进程    审计系统    演化引擎
```

## 快速开始

```bash
git clone https://github.com/Vane1981-2011/jiying.git
cd jiying
npm install
npm run dev
```

打开 http://localhost:5173 → 配置 DeepSeek API Key → 输入意图 → 点"开始"

## 核心能力

### ⚖️ 宪法即代码
- **尊严（康德）**: AI必须在前25%位置声明身份 → 未声明则阻断
- **自主（马尔库塞）**: 每次输出≥2个真正不同的替代方案 → 不足则警告
- **追问（海德格尔）**: 必须声明具体可质疑的前提假设 → 缺失则警告

### 🔗 TEP v1.0 可信执行协议
Agent间信任验证开放标准。8组件信封，Ed25519非对称签名。

### 🛡️ 7项预检门禁
对标Hermes：宪法状态→Agent参与→覆盖率≥60%→占位符检测→评分≥3→假设完整→去重(Jaccard>85%)

### 🧠 10种认知偏见交叉验证
Critic+Defender双prompt架构，检测确认偏误、锚定效应等10种偏见。

## 命令

| 命令 | 说明 |
|:-----|:-----|
| `npm run dev` | 启动开发服务器 |
| `npm test` | 运行178个测试 |
| `npm run build` | 生产构建 |
| `node server/index.js` | 启动服务端(端口3456) |

## 链接

- GitHub: https://github.com/Vane1981-2011/jiying
- ClawHub: https://clawhub.ai/vane1981/skills/jiying
- 作品展示: https://vane1981-2011.github.io/jiying/portfolio/

## 许可

Apache 2.0 · © 2026 Vane1981
