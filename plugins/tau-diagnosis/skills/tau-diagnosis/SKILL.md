---
name: tau-diagnosis
description: >
  Use this skill when the user asks to diagnose, audit, or upgrade an AI agent
  platform thinking methodology system using Tao's Law (韬定律) τ-minimization
  framework. Triggers include: '诊断思维体系', 'τ全链路诊断', '能力堆叠审计', '思维框架升级', '平台方法诊断',
  '全链路拆解'. Performs four-layer latency diagnosis (reverse decomposition),
  four-layer capability stacking (forward construction), and compound-interest
  closed-loop design.
version: 2.0.0
agent_created: true
qualityGate: standard
zcode:
  version: "1.0"
  τ_role: gatekeeper
  τ_impact:
    - metric: τ_qa
      direction: auto
      target: auto
      mechanism: 四层时延诊断自动输出质量报告
    - metric: τ_decide
      direction: reduce
      target: 20%
      mechanism: 诊断结论直接输入Bus路由优化
  bus_compatible: true
  cross_validate_with:
    - tau-diagnosis-zcode
    - first-principles-reasoning
disable: false
---
# τ 全链路诊断与升级

## Purpose

Perform a comprehensive diagnosis and upgrade of an AI agent platform thinking methodology system
using the Tao's Law (韬定律) "global time constant τ minimization" framework. The diagnosis
identifies bottlenecks across four layers, proposes capability stacking upgrades, and designs
a compound-interest closed-loop iteration mechanism.

## When to Use

Trigger this skill when:
- The user requests a full-chain diagnosis or audit of their agent platform methodology
- Keywords appear: 诊断, τ, 全链路, 能力堆叠, 思维框架升级, four-layer, Tao's Law
- The user wants to identify bottlenecks in their thinking framework
- A major system upgrade has been completed and re-diagnosis is needed

## Workflow

### Phase 1: Load Context

Before executing the diagnosis, read the following files if they exist:

- `~/.workbuddy/SOUL.md` — Core beliefs, strategic framework, and Unified Bus routing table
- `~/.workbuddy/IDENTITY.md` — Identity and self-cognition
- `~/.workbuddy/USER.md` — User profile and working habits
- `~/.workbuddy/skills/` — Existing skill inventory
- `~/.workbuddy/cards/` — Thinking card library
- `~/.workbuddy/skills/shared/feedback/anti-patterns.yaml` — Anti-pattern registry
- `~/.workbuddy/skills/shared/feedback/feedback-loop-protocol.md` — Feedback protocol (v2.0+)
- `~/.workbuddy/tau-benchmark.yaml` — τ baseline snapshots
- `~/Documents/知微知识库/` — Knowledge base if initialized

### Phase 2: Four-Layer Latency Diagnosis (Reverse Decomposition)

**Pre-step: Anti-pattern pre-scan.** Before beginning the diagnosis, scan `anti-patterns.yaml` for known patterns that may affect the current diagnosis scope. Output any matching warnings.

Penetrate downward from the top-level capability objective through four layers.
At each layer, identify redundant paths, invalid links, and cross-layer friction.

Define the unified metric: **τ = end-to-end delay from task arrival to high-quality output**.

The four layers:

1. **L4 · Platform Layer** (Capability objective output)
   - Is there a unified optimization objective?
   - How is output quality measured?

2. **L3 · Framework Layer** (Methodology orchestration)
   - Are multiple methodologies unified under a single scheduling bus?
   - Is there "framework fragmentation" waste?

3. **L2 · Tool Layer** (Skill/plugin execution)
   - Is the feedback loop closed?
   - Does execution experience flow back to the strategy layer?

4. **L1 · Foundation Layer** (Meta-cognition base)
   - Is meta-cognition structured and directly callable?
   - Or does it require re-reading and re-understanding each time?

For the output:
- Produce a diagnostic summary table: layer, current state, bottleneck, τ contribution %, compression space
- Identify and detail the Top 3 bottlenecks: phenomenon → root cause → optimal benchmark path → optimization plan
- Analyze "knowledge folding" status: are assets vertically associated or siloed?

### Phase 3: Four-Layer Capability Stacking (Forward Construction)

Build upward from the bottom layer, each layer serving as the public foundation for the one above:

1. **L1 → L2**: Extract reusable meta-cognition into structured "thinking cards" (executable checklist format, <200 words each)
2. **L2 → L3**: Standardize methods into Prompt templates and strategy configurations, registered in routing rules
3. **L3 → L4**: Integrate multiple methodologies into a **Unified Bus** — a decision matrix that auto-matches task types to methodology combinations
4. **L4 → Self**: Introduce unified τ_total metric and capability baselines for measurable self-optimization

Output a stacking detail table: layer, current assets, gaps, upgrade actions with priorities (P0/P1/P2).

### Phase 4: Compound-Interest Closed Loop

Design the four-stage iteration cycle:

① Reverse Diagnosis → ② Forward Stacking → ③ Effect Verification → ④ Foundation Upgrade → ①

Each round's "foundation upgrade" becomes the higher starting point for the next round's "reverse diagnosis."

Output:
- Closed-loop architecture diagram
- Compound-interest mechanism table: round, foundation level, τ compression, elevating effect on next round
- Three failure modes to guard against: feedback rate collapse, template bloat, foundation ossification
- Expected growth curve showing step-jump characteristics

### Phase 5: Priority Action Checklist

Output a prioritized action list:
- **P0**: Immediate execution — actions that directly address Top 3 bottlenecks
- **P1**: Within 1-2 weeks — infrastructure upgrades
- **P2**: Monthly iteration — maintenance and prevention

Each action must specify: affected layer(s), expected effect, τ compression estimate.

### Phase 6: Output Labeling

After completing the diagnosis, explicitly label whether each produced artifact is:
- **方法论 (Methodology)**: Answering "how to think" or "how to optimize"
- **工具 (Tool)**: A directly usable asset (template, config, knowledge card)
- **技能 (Skill)**: An encapsulated executable workflow module

## Output Format

Output the complete diagnosis as a structured HTML report with:
- Professional, clean visual design (light theme)
- Structured tables for all diagnostic data
- Color-coded tags: red (critical), yellow (warning), green (pass), indigo (tau)
- Flow diagrams for the four-layer structure, closed-loop, and growth curve
- © 版权所有：默笙夏夏の知書房 in the footer

## Key Principles

1. **τ as the single optimization anchor**: All diagnosis must be measured against end-to-end delay from task arrival to high-quality output
2. **Logic folding, not stacking**: Different layers should be co-designed, not independently optimized then assembled
3. **Unified Bus requirement**: Multiple methodologies must be orchestrated by a single scheduling layer, not manually traversed
4. **Compound interest via foundation elevation**: Each iteration must make the next iteration faster, not just solve the current problem
5. **Zero new memory/tools**: All optimizations must be implementable with existing infrastructure (Markdown, YAML, file system)

## τ 分项指标体系（Phase 2 强制执行）

诊断时必须量化以下五项分项指标，`τ_total = Σ(τ_decide, τ_cognize, τ_execute, τ_qa, τ_close)`：

| 指标 | 定义 | 测量方式 | 基准值 | 目标值 |
|------|------|----------|--------|--------|
| **τ_decide** | 决策延迟：任务到达到方法论选择完成 | 从任务识别到 Bus 路由匹配的推理步数 | 3-5 步 | 0-1 步 |
| **τ_cognize** | 认知启动：方法论选择到元认知加载完成 | 从 Skill 加载到思维卡片激活的步数 | ~5 步（全文解读） | ~1 步（卡片直接调用） |
| **τ_execute** | 执行延迟：开始执行到交付物完成 | 实际执行步数（不可压缩核心） | 基准 | 维持/优化 |
| **τ_qa** | 质检延迟：执行完成到质量验证通过 | QA 评估轮次 × 每轮耗时 | 手动触发 | Bus 自动触发 |
| **τ_close** | 闭环延迟：交付到经验固化完成 | Memory/Skill/Script 三项写入步数 | 被动执行 | 结构化自动执行 |

### τ 趋势记录

每次诊断后，将 τ 分项指标写入结构化事件：

```yaml
event_type: tau_benchmark
τ_decide: 2 steps
τ_cognize: 1 step  
τ_execute: baseline
τ_qa: 1 round
τ_close: 3 writes
τ_total: "estimated 48% of baseline"
```

## 与 Unified Bus 和反馈回路的集成（Phase 4 增强）

### Bus 集成

- 诊断开始时自动加载 `~/.workbuddy/SOUL.md` 中的 Unified Bus 路由表
- 根据当前任务类型匹配 Bus 路由序列，对比实际执行链路，识别偏离和未覆盖场景
- 诊断结论中的优化建议直接输出为 Bus 路由规则更新

### 反馈回路集成

- 读取 `~/.workbuddy/skills/shared/feedback/anti-patterns.yaml` 中的反模式库
- 诊断时检查当前体系是否存在已知反模式
- 新发现的反模式自动追加到反模式库
- 输出结构化 JSON 供反馈回路自动解析

### 卡片库集成

- 读取 `~/.workbuddy/cards/` 中的所有思维卡片
- 诊断时检查 L1 层元认知卡片化覆盖率
- 新建议的卡片自动生成模板

## 输出增强

HTML 报告之外，额外输出：

1. **结构化诊断 JSON** (`tau-diagnosis-result.json`)：供 Bus 和反馈回路自动解析
2. **τ 基准快照** (`tau-benchmark.yaml`)：记录当前 τ 分项指标

### JSON 输出格式

```json
{
  "diagnosis_id": "TAU-DIAG-YYYYMMDD-R{N}",
  "layers": {
    "L1": {"status": "critical|warning|ok", "τ_pct": 25, "bottleneck": "..."},
    "L2": {"status": "...", "τ_pct": 25, "bottleneck": "..."},
    "L3": {"status": "...", "τ_pct": 35, "bottleneck": "..."},
    "L4": {"status": "...", "τ_pct": 15, "bottleneck": "..."}
  },
  "top3_bottlenecks": [...],
  "τ_metrics": {
    "τ_decide": {"current": 4, "target": 1, "unit": "steps"},
    "τ_cognize": {"current": 5, "target": 1, "unit": "steps"},
    "τ_execute": {"current": "baseline", "target": "baseline"},
    "τ_qa": {"current": "manual", "target": "auto"},
    "τ_close": {"current": "passive", "target": "structured"}
  },
  "τ_total_compression": "estimated 52%",
  "actions": {"P0": [...], "P1": [...], "P2": [...]},
  "anti_patterns_found": ["AP-YYYYMMDD-NNN"],
  "cards_recommended": ["card-id-1", "card-id-2"]
}
```

## Reference

Load `references/tau-framework.md` for the detailed four-layer diagnosis methodology,
output templates, and framework definitions when executing the diagnosis.

Load `~/.workbuddy/skills/shared/feedback/feedback-loop-protocol.md` for structured feedback 
integration during the compound-interest closed loop design phase.

## Zcode 集成

### τ 角色与贡献

本技能在 Zcode 体系中承担 **gatekeeper** 角色，遵循 `skills/shared/zcode/zcode-embedding-standard.md` 标准。

| 指标 | 方向 | 机制 | 目标压缩 |
|------|------|------|---------|
| τ_qa | auto | 四层时延诊断自动输出质量报告 | auto |
| τ_decide | reduce | 诊断结论直接输入Bus路由优化 | 20% |

### 质量门禁

- **等级**: standard
- **依据**: `skills/shared/skill-quality-gate.md`
- **执行前**: 输入校验 + 反模式预检（`skills/shared/feedback/anti-patterns.yaml`）
- **执行后**: 输出校验 + 交付判定（三阶段门禁）

### 交叉验证

- **协同技能**: tau-diagnosis-zcode, first-principles-reasoning
- **校验协议**: `skills/shared/zcode/zcode-embedding-standard.md` 第 4 节

### 反馈闭环

- **输出触发**: Memory 写入 + τ 快照更新 + 反模式比对（如适用）
- **遵循协议**: `skills/shared/feedback/feedback-loop-protocol.md`

---
*Zcode 嵌入版本: 1.0 | © 版权所有：默笙夏夏の知書房 - 2026-07-09*
