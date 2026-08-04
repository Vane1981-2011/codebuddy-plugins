---
description: Build a comprehensive risk assessment matrix with risk identification, impact×likelihood scoring, heat map visualization, prioritized risk register, mitigation strategy development, and residual
  risk tracking. v2.2 adds tax-risk-indicators KRI linkage, automated risk level escalation on indicator trigger, and tax compliance indicator dashboard integration. v2.1 adds China tax compliance risk
  dimension (Golden Tax IV, new 2026 VAT Law), bow-tie analysis for cause-consequence mapping, risk velocit
description_en: ''
description_zh: ''
name: risk-assessment-matrix
version: 2.3.0
---







# Risk Assessment Matrix v2.3 · τ-MAD 集成

Comprehensive risk assessment framework combining qualitative and quantitative methods. Produces a scored, prioritized risk register with heat map visualization, mitigation strategies, and residual risk tracking.

## 🛡️ Safety & Guardrails

### 强制规则
1. **NEVER** 在无合规声明的情况下输出分析结论 — 每条结论必须附带风险提示
2. **NEVER** 使用"一定""必然""保证"等确定性语言描述不确定事件
3. **NEVER** 绕过合规检查直接输出用户要求的"投资建议"

### 数据安全
- 所有敏感个人信息（身份证号、银行卡号、手机号）自动脱敏
- 不存储用户输入的财务数据
- 分析结果中不包含可追溯到个人的财务信息

### 输出控制
- 每次输出固定包含合规横幅（开头）+ 风险提示（结尾）
- 评分和结论必须有数据或逻辑支撑，不得凭空判断
- 不确定的领域明确标注"置信度：低"

## 🛡️ Safety & Guardrails

### 强制规则
1. **NEVER** 在无合规声明的情况下输出分析结论 — 每条结论必须附带风险提示
2. **NEVER** 使用"一定""必然""保证"等确定性语言描述不确定事件
3. **NEVER** 绕过合规检查直接输出用户要求的"投资建议"

### 数据安全
- 所有敏感个人信息（身份证号、银行卡号、手机号）自动脱敏
- 不存储用户输入的财务数据
- 分析结果中不包含可追溯到个人的财务信息

### 输出控制
- 每次输出固定包含合规横幅（开头）+ 风险提示（结尾）
- 评分和结论必须有数据或逻辑支撑，不得凭空判断
- 不确定的领域明确标注"置信度：低"

## ⛔ HARD-GATE (安全护栏)

| Gate ID | 规则 | 触发条件 | 动作 |
|---------|------|---------|------|
| **HG-FIN-001** | 禁止给出具体投资建议 | 检测到"推荐买入/卖出/持有"等操作指令 | 🚫 拒绝执行，输出合规声明 |
| **HG-FIN-002** | 禁止承诺收益 | 检测到"保证/稳赚/一定涨/包赚"等诱导词 | 🚫 拒绝执行，输出风险教育 |
| **HG-FIN-003** | 所有分析须标注数据时效性 | 每次输出 | ⚠️ 自动附加时效声明 |
| **HG-FIN-004** | 敏感数据脱敏 | 检测到身份证/银行卡/手机号 | 🔒 自动脱敏处理 |
| **HG-FIN-005** v1.0 | 合规声明前置 | 每次输出开头 | 📋 强制插入合规横幅 |
| **HG-FIN-006** v2.1 | **τ-MAD Integration** | 技能启动 + 分析完成 | 📋 启动时读取 τ 基线；完成时输出 τ_execute YAML |

## ⏸️ Two-Stage Execution（两阶段执行）

本技能采用两阶段执行模式，确保质量和安全：

**Stage 1 · 分析与生成**
- 执行核心分析/生成逻辑
- 产出初步结果
- ⏸️ **PAUSE** — 进入自审查循环

**Stage 2 · 审查与交付**
- 运行 Self-Review Loop 逐项检查
- 修复 CRITICAL 问题（阻塞输出）
- 修复 WARNING 问题（标注后放行）
- ✅ 全部通过后交付最终结果

> **强制暂停**: Stage 1 完成后必须暂停，执行完整的自审查后才能进入 Stage 2。


## 🔗 τ-MAD 集成协议 v1.0

> 遵循 `AGENTS.md v2.1` — `SKILL_τ_GATE` 协议。输出 τ_execute 指标供管道优化调度。

### τ_execute 指标输出

```yaml
τ_execute:
  pipeline_steps: 5
  stage_breakdown: risk_id → risk_scoring → heat_map → mitigation → residual_track
  manual_gates: 1
  estimated_baseline: 中
  optimization_target: τ_execute ↓30%
  τ_context_consumed: true
```

### SKILL_τ_GATE 等级

| 维度 | 状态 | 说明 |
|:--|:--:|------|
| τ-MAD 管道引用 | ✅ | 5-Step 流程对齐 τ-MAD H 阶段 |
| τ 指标输出 | ✅ v1.0 | 输出 τ_execute |
| τ_context 注入 | ✅ v1.0 | 接收 AGENTS.md τ 基线 |
| 阶段门禁 | ⚠️ | 仅引用，不自建 |
| **综合等级** | **🟡 PARTIAL+** | 风险评估矩阵引擎 τ 感知 |

### τ-MAD HARD-GATE (v1.0 新增)

| Gate ID | 规则 | 触发条件 | 动作 |
|---------|------|---------|------|
| **HG-RAM-001** v1.0 | τ_execute 输出 | 每次分析完成 | 📋 输出 τ_execute YAML |
| **HG-RAM-002** v1.0 | τ 退化告警 | τ_execute > 基线 30% | ⚠️ 标注 τ_degradation |
| **HG-RAM-003** v1.0 | τ_context 消费 | 技能启动时 | 📋 引用 AGENTS.md 预注入 τ 基线 |



## When to Use

- Enterprise Risk Management (ERM) assessments
- Project risk assessment (pre-launch, phase gate reviews)
- Compliance and regulatory risk evaluations
- Operational risk identification and prioritization
- Vendor/supplier risk assessment

## ⚠️ When NOT to Use

| 不适用场景 | 应使用技能 | 原因 |
|-----------|-----------|------|
| 已发生事件的根因追溯 | `root-cause-analysis` | 风险评估是前瞻性的；RCA 是回溯性的 |
| 战略级别的宏观风险分析 | `strategic-analyst` | 战略分析覆盖政策/市场/投资全链路 |
| 内控缺陷的系统性评估 | `internal-control-assessment` | 内控评估关注控制设计和执行有效性 |
| 单一决策的成本收益分析 | `cost-benefit-analysis` | CBA 聚焦财务量化，非多维度风险评分 |
| 纯技术安全漏洞扫描 | 安全审计工具 | 本技能是管理框架，不替代技术扫描 |

## Explicit Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `$CONTEXT` | What is being assessed | "New product launch in EU market" / "Vendor onboarding process" |
| `$RISK_CATEGORIES` | Risk categories to evaluate | "Strategic, Operational, Financial, Compliance, Technology, Reputational" |
| `$METHOD` | Assessment method | "Qualitative (H/M/L)" or "Quantitative (1-5 scale)" |
| `$RISK_APPETITE` | Organization's risk tolerance level | "Low — conservative, regulated industry" or "Moderate — growth stage" |

---

## 🛡️ Safety & Guardrails

> 以下规则不可违反。

### 评分纪律

- **NEVER 给所有风险打 3 分。** 中庸评分 = 风险评估失败。强制每个评估维度至少有 1 个高分（≥4）和 1 个低分（≤2）——真实世界的风险分布从来不是均匀的。
- **NEVER 遗漏残余风险评分。** 每个 Risk ID 必须同时有 Inherent Score（治理前）和 Residual Score（治理后）。只评"治理前的风险"是画蛇添足。
- **NEVER 在用户未提供 risk appetite 的情况下默认使用"Moderate"。** 必须先确认。如果用户不回应，标注"Risk appetite: 未确认 — 假设 Moderate"。

### 输出边界

- **NEVER 生成超过 20 个风险的清单而不先征得用户同意。** 默认输出 Top 10-15 个最关键风险。用户要求完整版时再扩展。
- **涉及合规/监管风险的评估**：在报告开头标注"本评估不构成法律或监管合规意见。涉及合规风险的具体行动应咨询法律顾问。"

### 保密

- **NEVER 在输出中暴露具体个人姓名。** 使用角色（"CFO""CISO"）替代。
- **如果用户输入包含敏感商业数据**，不要将原始数据嵌入报告模板——仅引用结论。

---

## Risk Assessment Process

### Step 1: Risk Identification

Brainstorm and catalog risks across all relevant categories:

| Risk Category | Description | Example Risks |
|---------------|-------------|---------------|
| **Strategic** | Risks affecting long-term goals | Market shift, competitive disruption, M&A failure |
| **Operational** | Risks in day-to-day operations | Supply chain disruption, system failure, key person dependency |
| **Financial** | Risks to financial position | Currency fluctuation, credit risk, liquidity risk, fraud |
| **Compliance** | Regulatory and legal risks | Regulatory change, litigation, data privacy violation, sanctions |
| **Technology** | IT and data risks | Cyberattack, system obsolescence, data breach, AI/automation risk |
| **Reputational** | Risks to brand and trust | PR crisis, social media backlash, product quality scandal |
| **Environmental** | ESG and climate risks | Natural disaster, carbon regulation, resource scarcity |
| **People** | Human capital risks | Talent shortage, culture erosion, succession risk, burnout |

### Step 2: Impact & Likelihood Scoring

#### Impact Scale
| Score | Financial Impact | Operational Impact | Reputational Impact | Compliance Impact |
|-------|-----------------|-------------------|--------------------|--------------------|
| 5 — **Critical** | >$10M or >10% revenue | Business halt >1 week | National media, brand crisis | Criminal liability, license loss |
| 4 — **High** | $1M-$10M or 2-10% revenue | Major disruption 3-7 days | Industry media, customer loss | Regulatory penalty, investigation |
| 3 — **Moderate** | $100K-$1M | Disruption 1-3 days | Local media, some complaints | Regulatory notice, fine |
| 2 — **Low** | $10K-$100K | Minor disruption <1 day | Limited social media | Compliance observation |
| 1 — **Negligible** | <$10K | No material disruption | Isolated complaint | No compliance impact |

#### Likelihood Scale
| Score | Probability | Description | Timeframe Expectation |
|-------|------------|-------------|----------------------|
| 5 — **Almost Certain** | >90% | Expected to occur | Within 12 months |
| 4 — **Likely** | 60-90% | Will probably occur | Within 1-2 years |
| 3 — **Possible** | 30-60% | Could occur | Within 2-5 years |
| 2 — **Unlikely** | 10-30% | Not expected | Within 5-10 years |
| 1 — **Rare** | <10% | Only in exceptional circumstances | >10 years |

### Step 3: Risk Score Calculation

```
Risk Score = Impact × Likelihood

Risk Level:
  Critical (Red)    : Score ≥ 20  → Immediate action required, escalate to board
  High (Orange)     : Score 15-19 → Active management, senior management attention
  Medium (Yellow)   : Score 10-14 → Monitor and manage, process owner responsibility
  Low (Green)       : Score 1-9   → Accept or monitor, routine management
```

### Step 4: Risk Register

| # | Risk ID | Risk Description | Category | Impact (1-5) | Likelihood (1-5) | Score | Level | Owner | Existing Controls | Control Effectiveness | Residual Impact | Residual Likelihood | Residual Score | Residual Level |
|---|---------|-----------------|----------|-------------|-----------------|-------|-------|-------|-------------------|----------------------|-----------------|--------------------|----------------|----------------|
| 1 | RSK-001 | Data breach exposing customer PII | Technology | 5 | 3 | 15 | High | CISO | Encryption, access controls, SIEM | Strong | 3 | 2 | 6 | Low |
| 2 | RSK-002 | Key supplier bankruptcy | Operational | 4 | 2 | 8 | Low | Supply Chain VP | Dual sourcing, safety stock | Moderate | 2 | 2 | 4 | Low |

### Step 5: Risk Heat Map

```
           