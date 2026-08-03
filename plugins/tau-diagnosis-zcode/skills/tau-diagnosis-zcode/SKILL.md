---
name: tau-diagnosis-zcode
description: >
  增强版 τ 全链路诊断与升级引擎（zcode强化版）。继承 tau-diagnosis v2.0 四层时延诊断框架 + ZCode
  mad-think-pipeline S1-S4 并行推理管线，融合 Unified Bus 编排、Agent
  分派矩阵、交叉验证与置信度量化。Trigger when the user needs enhanced diagnosis with parallel
  reasoning paths, cross-layer validation, or when standard tau-diagnosis
  encounters complex multi-system audit scenarios. Keywords: 增强诊断, zcode诊断,
  并行推理诊断, τ深度诊断, 多路径验证, enhanced tau audit.
version: 3.0.0
agent_created: true
qualityGate: enhanced
trigger_recommended:
  - 增强诊断
  - zcode诊断
  - 并行推理诊断
  - τ深度诊断
  - 多路径验证
  - enhanced tau audit
  - 全链路增强诊断
  - 交叉验证诊断
dependencies:
  - tau-diagnosis
  - mad-think-pipeline
  - first-principles-reasoning
supersedes:
  - tau-diagnosis (for enhanced scenarios only; standard tau-diagnosis remains
    available for routine use)
zcode:
  version: "1.0"
  τ_role: integrator
  τ_impact:
    - metric: τ_close
      direction: reduce
      target: 60%
      mechanism: S3交叉验证 + 反馈缝合自动执行
    - metric: τ_qa
      direction: auto
      target: auto
      mechanism: 多Agent并行分派 + 置信度量化
  bus_compatible: true
  cross_validate_with:
    - tau-diagnosis
    - mad-think-pipeline
    - first-principles-reasoning
disable: true
---

# τ 全链路诊断与升级 — ZCode 增强版 v3.0

> **继承关系：** tau-diagnosis v2.0（四层诊断框架） + mad-think-pipeline v2.0（S1-S4 并行推理管线）
> **v3.0 核心增强：** 在保留 v2.0 所有功能的基础上，注入 ZCode 四阶段推理引擎、多Agent并行分派、交叉验证与置信度量化

---

## 一、双引擎融合架构

```
┌────────────────────────────────────────────────────────────┐
│              tau-diagnosis-zcode v3.0                       │
│                                                             │
│  ┌──────────────────────┐    ┌───────────────────────────┐ │
│  │ tau-diagnosis v2.0    │    │ ZCode mad-think-pipeline   │ │
│  │                      │    │                           │ │
│  │ · 四层时延诊断(L1-L4) │ ←→ │ · S1 问题拆解              │ │
│  │ · 四层能力堆叠        │    │ · S2 并行推理(多Agent)     │ │
│  │ · 复利闭环设计        │    │ · S3 交叉验证(置信度)      │ │
│  │ · τ 分项指标体系       │    │ · S4 合成输出              │ │
│  │ · Bus + 反馈回路集成  │    │ · Agent 分派矩阵           │ │
│  └──────────────────────┘    └───────────────────────────┘ │
│                                                             │
│  增强点：                                                   │
│  1. 每层诊断不再顺序执行，拆解为独立子问题后并行推理        │
│  2. 层间结论交叉验证，冲突自动标记回溯                      │
│  3. 每层诊断结论附加置信度标签(high/medium/low)             │
│  4. 大规模审计(10+技能/模块)自动启用多Agent并行分派         │
└────────────────────────────────────────────────────────────┘
```

---

## 二、增强版诊断流程

### Phase 0: 诊断模式判定

在执行前，根据诊断范围自动选择模式：

| 条件 | 模式 | 说明 |
|------|------|------|
| 诊断对象 ≤ 5 个组件 | **标准模式** | 继承 tau-diagnosis v2.0 顺序流程 |
| 诊断对象 6-20 个组件 | **并行模式** | 每层拆解为子问题 → S2 并行推理 |
| 诊断对象 ≥ 20 个组件 | **全并行模式** | S1 拆解 → S2 多Agent分派 → S3 交叉验证 |
| 跨系统/跨平台审计 | **增强交叉验证** | S3 强制多路径交叉验证 + 冲突回溯 |

### Phase 1: S1 问题拆解（Context Loading + Task Decompose）

**继承 tau-diagnosis Phase 1（Load Context），注入 ZCode S1（Task Decompose）：**

步骤：
1. **加载上下文**（tau-diagnosis Phase 1 全部文件加载）
2. **需求还原**：区分诊断的表面需求与底层需求（加载 real-needs-classifier 卡片）
3. **结构化拆解**：
   ```
   诊断目标 → 拆解为 4 层独立子任务
   ├── L4 平台层子任务：[L4-Q1, L4-Q2, ...]
   ├── L3 框架层子任务：[L3-Q1, L3-Q2, ...]
   ├── L2 工具层子任务：[L2-Q1, L2-Q2, ...]
   └── L1 基础层子任务：[L1-Q1, L1-Q2, ...]
   ```
4. **推理类型匹配**：

| 子任务类型 | 推理方式 | 推荐 Agent | 置信度策略 |
|-----------|---------|-----------|-----------|
| 结构统计（数量/分布） | 工具获取（Read/Grep/Bash） | explorer | high |
| 性能瓶颈判定 | 链式推理 + 数据支撑 | reasoning_engine | medium |
| 功能缺失识别 | 规范对比 + 多维扫描 | code_generator | medium |
| 兼容性判断 | 逆向推断 + 规范检查 | explorer | medium |
| 优化方案设计 | 第一性原理重构 + 多路径 | reasoning_engine | low→迭代提升 |

5. **输出 S1 结构**：
```json
{
  "scope": {"layers": 4, "components": 14, "mode": "parallel"},
  "tasks": [
    {"id": "L4-1", "layer": "L4", "question": "...", "reasoning_type": "statistical", "agent": "explorer"},
    {"id": "L3-1", "layer": "L3", "question": "...", "reasoning_type": "causal", "agent": "reasoning_engine"}
  ],
  "dependency_graph": {
    "L1-1": [],
    "L2-1": ["L1-1"],
    "L3-1": ["L2-1"],
    "L4-1": ["L3-1"]
  }
}
```

### Phase 2: S2 并行推理（Multi-Agent Parallel Diagnosis）

**继承 tau-diagnosis Phase 2（Four-Layer Latency Diagnosis），注入 ZCode S2（Parallel Reason）：**

1. **Agent 分派矩阵**（增强版）：

| 诊断层 | 主 Agent | 并行 Agent | 推理深度 | 置信度要求 |
|--------|---------|-----------|---------|-----------|
| L4·平台层 | reasoning_engine | explorer(τ数据统计) | L2 | medium+ |
| L3·框架层 | reasoning_engine | explorer(Bus路由检查) | L2 | medium+ |
| L2·工具层 | code_generator | explorer(文件扫描) | L1-L2 | medium |
| L1·基础层 | reasoning_engine | — | L1（第一性原理） | medium+ |

2. **并行推演**：
   - 每层独立启动 Agent 并行推理
   - 每个 Agent 独立推演至结论（附带置信度）
   - 中间推理步骤记录到 τ 追踪日志

3. **工具调用增强**：
   - 自动调用 Read/Grep/Bash 获取诊断所需数据
   - 不依赖人工提供诊断素材
   - 工具调用结果直接注入 Agent 推理上下文

4. **输出 S2 阶段结论**：
```json
{
  "layer": "L2",
  "agent": "code_generator",
  "conclusions": [
    {"finding": "7/14技能缺少quality_gate", "confidence": "high", "evidence": "file scan"},
    {"finding": "反馈回路覆盖率 7%", "confidence": "high", "evidence": "grep result"}
  ],
  "τ_measurements": {"τ_decide": 2, "τ_cognize": 3, "τ_execute": "baseline"},
  "reasoning_trace": ["step1: scan skills/", "step2: grep qualityGate", "step3: compute coverage"]
}
```

### Phase 3: S3 交叉验证（Cross-Layer Verify）

**继承 tau-diagnosis Phase 2（诊断输出），注入 ZCode S3（Cross-Verify）：**

1. **层间一致性检查**：
   - L1 诊断结论是否与 L2 的"基础层卡片使用率"一致？
   - L2 诊断结论是否在 L3 的"Bus 路由覆盖"中得到印证？
   - L3 诊断结论是否与 L4 的"τ 基准数据"矛盾？

2. **冲突检测与回溯**：
   - 冲突标记 → 回溯到 S2 重新推理
   - 回溯次数上限：每层最多 2 次
   - 持续冲突 → 标注为 "unresolved"，置信度降为 low

3. **遗漏检查**（自检清单）：
   - "是否遗漏了跨层依赖？"
   - "是否将结果性指标误判为根因？"
   - "优化建议是否与死亡清单冲突？"
   - "是否考虑了对非诊断对象的连锁影响？"

4. **不确定性量化**：
   - 每个诊断结论附带置信度标签
   - 低置信度结论在输出时显式标注

5. **输出 S3 验证报告**：
```json
{
  "cross_validation": {
    "consistency_score": 0.85,
    "conflicts": [
      {"layers": ["L2", "L3"], "finding": "L2反馈链路裂 vs L3反馈协议v2.0", "resolution": "L2统计仅覆盖Bus强制注入前的时间窗口", "confidence": "medium"}
    ],
    "omissions_found": ["跨技能依赖未纳入L2诊断"],
    "uncertainty_labels": {"L1-confidence": "medium", "L2-confidence": "high", "L3-confidence": "medium", "L4-confidence": "high"}
  }
}
```

### Phase 4: S4 合成输出（Synthesize）

**继承 tau-diagnosis Phase 3-6（Capability Stacking + Closed Loop + Output），注入 ZCode S4（Synthesize）：**

1. **结论合成**（四层结论 → 统一诊断报告）：
   - 合并各 Agent 的平行结论
   - 冲突点单独说明，标注置信度
   - 去除重复发现

2. **方案合成**（四层升级建议 → 统一行动清单）：
   - 按 P0/P1/P2 优先级排序
   - 每条行动标注：涉及层、预期 τ 压缩、置信度
   - 行动之间的依赖关系图

3. **置信度矩阵**：

| 诊断结论 | L1置信度 | L2置信度 | L3置信度 | L4置信度 | 综合 |
|---------|---------|---------|---------|---------|------|
| Top 3 瓶颈 | — | high | medium | high | **medium-high** |
| τ 分项指标 | — | high | — | high | **high** |
| 优化建议 | medium | high | medium | high | **medium-high** |
| 预期 τ 压缩 | low | medium | medium | medium | **medium** |

4. **输出格式**（完整保留 tau-diagnosis v2.0 输出 + S3 交叉验证数据）：
   - HTML 报告（标准格式）
   - 增强版 JSON（含 S1-S4 追踪数据）
   - τ 基准快照更新
   - 交叉验证报告附录

### Phase 5: 反馈闭环（与 tau-diagnosis v2.0 完全兼容）

保持 tau-diagnosis v2.0 Phase 4-6 的全部反馈闭环机制不变：
- Bus 路由表自动对比与更新建议
- 反模式库自动比对与新反模式归档
- Memory 结构化写入
- τ 快照自动更新

---

## 三、多Agent分派矩阵（增强版核心）

当诊断模式为 parallel 或 full-parallel 时，启用以下 Agent 分派：

```yaml
agents:
  - id: tau-coordinator
    role: multimodal_coordinator
    task: "S1 problem decomposition + S4 synthesis"
    spawns: [l4-agent, l3-agent, l2-agent, l1-agent]
    max_retries: 2

  - id: l4-agent
    role: reasoning_engine
    task: "L4 platform layer diagnosis: τ metrics + quality measurement"
    tools: [Read, Grep, Bash]
    model: reasoning

  - id: l3-agent
    role: reasoning_engine
    task: "L3 framework layer diagnosis: Bus routing + methodology orchestration"
    tools: [Read, Grep]
    model: reasoning

  - id: l2-agent
    role: code_generator
    task: "L2 tool layer diagnosis: skill coverage + quality gate audit"
    tools: [Read, Grep, Bash]
    model: default
    parallel_agents:
      - id: l2-scanner
        role: explorer
        task: "File system scan: version/qualityGate/agent_created coverage"

  - id: l1-agent
    role: reasoning_engine
    task: "L1 foundation layer diagnosis: meta-cognition structure + card coverage"
    tools: [Read, Grep]
    model: reasoning
```

---

## 四、与标准版 tau-diagnosis 的关系

| 维度 | tau-diagnosis v2.0（标准版） | tau-diagnosis-zcode v3.0（增强版） |
|------|---------------------------|----------------------------------|
| 适用场景 | 常规诊断（≤ 5 组件） | 大规模审计 / 跨系统诊断 / 需要置信度场景 |
| 推理方式 | 四层顺序穿透 | S1 拆解 → S2 多Agent并行 → S3 交叉验证 |
| 输出 | HTML + JSON + τ快照 | 同左 + S1-S4 追踪 + 置信度矩阵 + 交叉验证报告 |
| 依赖 | 独立 | tau-diagnosis + mad-think-pipeline |
| 触发 | 标准触发词 | 增强触发词（增强诊断/zcode诊断/τ深度诊断） |
| Bus路由 | 方法论自我升级 | 重大架构决策（并行模式时） |

**共存策略：** 
- `tau-diagnosis` 保留为日常快速诊断工具
- `tau-diagnosis-zcode` 仅在以下场景激活：
  - 诊断对象 ≥ 6 组件
  - 需要多路径交叉验证
  - 用户明确要求"增强诊断"或"zcode诊断"

---

## 五、增强版 JSON 输出格式

```json
{
  "diagnosis_id": "TAU-ZCD-YYYYMMDD-R{N}",
  "engine": "tau-diagnosis-zcode v3.0",
  "mode": "parallel|full-parallel|standard|cross-verify",
  "s1_decompose": {
    "scope": {...},
    "tasks": [...],
    "dependency_graph": {...}
  },
  "s2_parallel_results": {
    "L1": {"agent": "l1-agent", "conclusions": [...], "confidence": "medium"},
    "L2": {"agent": "l2-agent", "conclusions": [...], "confidence": "high", "parallel_agent_results": [...]},
    "L3": {"agent": "l3-agent", "conclusions": [...], "confidence": "medium"},
    "L4": {"agent": "l4-agent", "conclusions": [...], "confidence": "high"}
  },
  "s3_cross_verify": {
    "consistency_score": 0.85,
    "conflicts": [...],
    "omissions": [...],
    "uncertainty_matrix": {...}
  },
  "s4_synthesis": {
    "layers": {...},           // tau-diagnosis v2.0 标准 layers 输出
    "top3_bottlenecks": [...],
    "τ_metrics": {...},        // tau-diagnosis v2.0 标准 τ 指标
    "τ_total_compression": "...",
    "actions": {"P0": [...], "P1": [...], "P2": [...]},
    "confidence_matrix": {...}  // 增强版新增
  },
  "anti_patterns_found": [...],
  "cards_recommended": [...],
  "retrospective": {           // 增强版新增：回溯记录
    "backtrack_count": 0,
    "unresolved_conflicts": 0,
    "agent_retries": 0
  }
}
```

---

## 六、部署配置

**技能激活条件：**
- 诊断对象 ≥ 6 组件 → 自动从标准版升级为增强版
- 用户关键词包含 "增强/zcode/并行/交叉验证/深度诊断" → 强制启用增强版
- 其余场景 → Bus 路由到标准版 tau-diagnosis

**与现有技能体系的兼容性：**
- 标准版 tau-diagnosis v2.0 保持不变，独立可用
- 增强版 tau-diagnosis-zcode v3.0 作为可选增强层
- 两者共享同一套 τ 指标体系、反模式库、τ 基准快照
- 增强版输出的 JSON 完全向后兼容标准版格式（新增字段为扩展字段）

---

## Reference

- `~/.workbuddy/skills/tau-diagnosis/references/tau-framework.md` — 四层诊断框架详细方法论
- `~/.workbuddy/skills/mad-think-pipeline/references/AGENTS.md` — Agent 配置模板
- `~/.workbuddy/skills/shared/feedback/feedback-loop-protocol.md` — 反馈回路协议
- `~/.workbuddy/tau-benchmark.yaml` — τ 基准快照

## Zcode 集成

### τ 角色与贡献

本技能在 Zcode 体系中承担 **integrator** 角色，遵循 `skills/shared/zcode/zcode-embedding-standard.md` 标准。

| 指标 | 方向 | 机制 | 目标压缩 |
|------|------|------|---------|
| τ_close | reduce | S3交叉验证 + 反馈缝合自动执行 | 60% |
| τ_qa | auto | 多Agent并行分派 + 置信度量化 | auto |

### 质量门禁

- **等级**: enhanced
- **依据**: `skills/shared/skill-quality-gate.md`
- **执行前**: 输入校验 + 反模式预检（`skills/shared/feedback/anti-patterns.yaml`）
- **执行后**: 输出校验 + 交付判定（三阶段门禁）

### 交叉验证

- **协同技能**: tau-diagnosis, mad-think-pipeline, first-principles-reasoning
- **校验协议**: `skills/shared/zcode/zcode-embedding-standard.md` 第 4 节

### 反馈闭环

- **输出触发**: Memory 写入 + τ 快照更新 + 反模式比对（如适用）
- **遵循协议**: `skills/shared/feedback/feedback-loop-protocol.md`

---
*Zcode 嵌入版本: 1.0 | © 版权所有：默笙夏夏の知書房 - 2026-07-09*
