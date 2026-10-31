---
description: 投资分析与风险量化引擎 — 基于 quantstats (7.4K⭐) + Riskfolio-Lib (4.3K⭐) 提供投资组合绩效分析、风险指标计算、投资组合优化、HTML报告生成。触发词：投资分析、投资组合、风险量化、夏普比率、最大回撤、资产配置、组合优化、Python分析报告
description_en: ''
description_zh: ''
name: investment-risk-engine
version: 1.0.0
disable: false
---
# 📈 投资分析与风险量化引擎 v1.0

> **计算层** — 为财务/风险/项目分析 Skill 提供量化计算与可视化输出。
> 底层库：`quantstats` (7,439⭐) + `Riskfolio-Lib` (4,340⭐)
> **依赖**: `financial-data-access` (akshare) 提供y数据输入

---

## 🚫 何时不使用本技能

| 场景 | 原因 | 替代方案 |
|------|------|---------|
| 数据完全缺失 | 分析缺乏基础 | 告知用户，建议先收集数据 |
| 问题有唯一正确答案 | 分析框架不适用 | 直接给出确定性答案 |
| 用户已有既定结论只想确认 | 分析会引入不必要的复杂性 | 直接确认或质疑 |
| 纯执行类任务 | 无需分析 | 使用专门的执行 Skill |

## ⛔ HARD-GATE (安全护栏)

| Gate ID | 规则 | 触发条件 | 动作 |
|---------|------|---------|------|
| **HG-STR-001** | 禁止单一方案推荐 | 分析只给出一个选项 | 🚫 强制输出 ≥2 个备选方案 |
| **HG-STR-002** | 强制标注置信度 | 每次输出结论 | ⚠️ 每个结论必须标注 H/M/L 置信度 |
| **HG-STR-003** | 禁止无数据支撑的断言 | 检测到无引用/无数据的结论 | 🚫 拒绝输出，要求补充依据 |
| **HG-STR-004** | 假设必须显式声明 | 分析中隐含假设 | ⚠️ 自动提取并展示关键假设 |
| **HG-STR-005** v1.0 | 透明化推理链 | 每次分析 | 📋 展示从数据到结论的推理步骤 |

## 🛡️ Safety & Guardrails

### 强制规则
1. **NEVER** 只给出一个方案 — 必须提供 ≥2 个备选方案并标注优劣
2. **NEVER** 隐藏推理过程中的关键假设 — 所有假设必须显式声明
3. **NEVER** 使用绝对化语言描述概率性结论

### 分析质量控制
- 每个结论必须标注置信度（H=高置信/M=中/L=低）
- 数值类输出必须说明数据来源
- 存在矛盾的分析结果必须标注并解释

### 偏误防范
- 主动识别并标注可能的确认偏误
- 对用户已有观点进行批判性审视
- 提供反方观点（Devil's Advocate）

## 🔧 Failure Modes & Recovery

| 症状 | 可能原因 | 恢复策略 |
|------|---------|---------|
| 分析结论过于表面 | 未深入追问"为什么" | 对关键结论追加 2 层"为什么"追问 |
| 备选方案质量不均 | 只认真分析了偏好方案 | 强制对每个方案分配均等分析时间 |
| 置信度标注过于保守 | 避免出错的防御性行为 | 校准：H≥80%确定，M=50-80%，L<50% |
| 维度遗漏 | 分析框架未覆盖特定场景 | 补充"其他考虑因素"章节 |
| 数据矛盾未解决 | 多源数据不一致 | 标注矛盾点，建议优先信任哪个来源 |

## ✅ Completion Criteria（完成标准）

任务完成前逐项验证：

- [ ] ≥2 个备选方案已列出并对比
- [ ] 每个结论标注了置信度（H/M/L）
- [ ] 关键假设已显式声明（≥2 条）
- [ ] 数据来源已标注（如有数值）
- [ ] 推理链清晰可见（从数据→分析→结论）
- [ ] 反方观点已呈现
- [ ] 输出长度适中（≤2500 字）


## 🔄 Self-Review Loop（自审查循环）

每次输出前执行自审查：Review → Fix → Re-Review

1. **Review**: 逐项对照 Completion Criteria 检查
2. **Fix**: 修复所有未通过项（CRITICAL 阻塞输出）
3. **Re-Review**: 修复后重新检查，直到全部通过
4. **Proceed**: 全部通过后输出最终结果

| 审查项 | 严重度 | 动作 |
|--------|:--:|------|
| 缺少关键输出模块 | CRITICAL | 🚫 阻塞输出 |
| 置信度未标注 | CRITICAL | 🚫 补充标注 |
| 数据无来源 | WARNING | ⚠️ 标注"基于公开信息" |
| 格式不完整 | WARNING | ⚠️ 补充缺失字段 |



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



## 💾 Checkpoint & Resume（检查点与恢复）

对于超过 2 分钟的任务，采用检查点模式确保可靠性：

- **自动保存**: 每完成一个子任务自动保存检查点
- **断点续传**: 任务中断后可从最近检查点恢复
- **检查点文件**: `{task_name}_checkpoint.json` 记录当前进度
- **恢复策略**: 读取检查点 → 跳过已完成步骤 → 继续未完成步骤

| 检查点时机 | 保存内容 |
|-----------|---------|
| 输入验证后 | 已验证的输入参数 |
| 核心逻辑完成后 | 中间结果 |
| 自审查通过后 | 最终待交付结果 |


## 前置条件

```python
import quantstats as qs       # 投资组合绩效分析
import riskfolio as rp         # 投资组合优化与风险量化
import pandas as pd
import numpy as np
```

---

## 一、quantstats：投资组合绩效分析

### 核心能力
| 指标 | 函数 | 说明 |
|:----|:-----|:-----|
| 夏普比率 | `qs.stats.sharpe(returns)` | 风险调整后收益 |
| 最大回撤 | `qs.stats.max_drawdown(returns)` | 最大跌幅 |
| 年化收益 | `qs.stats.cagr(returns)` | 复合年增长率 |
| 年化波动 | `qs.stats.volatility(returns)` | 年化标准差 |
| Calmar 比率 | `qs.stats.calmar(returns)` | 收益/最大回撤 |
| Sortino 比率 | `qs.stats.sortino(returns)` | 下行风险调整 |
| 胜率 | `qs.stats.win_rate(returns)` | 正收益天数占比 |
| VaR (95%) | `qs.stats.var(returns)` | 在险价值 |
| CVaR | `qs.stats.cvar(returns)` | 条件在险价值 |
| 信息比率 | `qs.stats.information_ratio(returns, benchmark)` | 超额收益/跟踪误差 |

### 模式 1：一键生成 HTML 投资报告
```python
import akshare as ak
import quantstats as qs

# 1. 用 akshare 拉数据
df = ak.stock_zh_a_hist(symbol="600519", period="daily",
                        start_date="20240101", end_date="20260712")

# 2. 计算日收益率
returns = df['收盘'].pct_change().dropna()

# 3. 可选：基准指数
benchmark_df = ak.index_zh_a_hist(symbol="000300", period="daily",
                                  start_date="20240101", end_date="20260712")
benchmark = benchmark_df['收盘'].pct_change().dropna()

# 4. 生成完整 HTML 报告
qs.reports.html(
    returns,
    benchmark=benchmark,
    title="贵州茅台 投资分析报告",
    output="maotai_report.html",
    download_filename="maotai_report.html"
)
```

### 模式 2：快速输出关键指标
```python
returns = df['收盘'].pct_change().dropna()

summary = {
    '年化收益': f"{qs.stats.cagr(returns)*100:.2f}%",
    '年化波动': f"{qs.stats.volatility(returns)*100:.2f}%",
    '夏普比率': f"{qs.stats.sharpe(returns):.2f}",
    '最大回撤': f"{qs.stats.max_drawdown(returns)*100:.2f}%",
    'Calmar': f"{qs.stats.calmar(returns):.2f}",
    '胜率': f"{qs.stats.win_rate(returns)*100:.1f}%",
    'VaR(95%)': f"{qs.stats.var(returns)*100:.2f}%",
}
```

### 模式 3：月度/年度热力图
```python
# ✨ 返回收益热力图(DataFrame)
# 行=年份, 列=月份
qs.reports.metrics(returns, mode='full')

# 或直接获取
qs.stats.monthly_returns(returns)     # 各月收益
qs.stats.yearly_returns(returns)      # 各年收益
```

---

## 二、Riskfolio-Lib：投资组合优化

### 核心能力

| 功能 | 类/方法 | 说明 |
|:----|:--------|:-----|
| 均值方差优化 | `rp.Portfolio()` + `.optimization()` | 经典 MPT 模型 |
| 风险平价 | `rp.RiskParity()` | 等风险贡献分配 |
| Black-Litterman | `rp.BLViews()` + `rp.BL()` | 主观观点+市场均衡 |
| 层次风险平价 | `rp.HCPortfolio()` | 树状聚类风险分配 |
| 条件风险价值优化 | `.optimization(model='CVaR')` | 尾部风险优化 |

### 模式 4：构建最优投资组合
```python
import riskfolio as rp

# 假设有多个资产的收益率数据
# prices: DataFrame, 列=资产代码, 行=日期价格
returns = prices.pct_change().dropna()

# 构建组合
port = rp.Portfolio(returns=returns)

# 设置方法
port.assets_stats(method='hist')  # 使用历史数据估计

# 均值方差优化 - 最大化夏普比率
w = port.optimization(
    model='Classic',        # 经典均值方差
    rm='MV',                # 风险度量: 方差(MV)
    obj='Sharpe',           # 优化目标: 最大化夏普
    rf=0.02,                # 无风险利率
)

print(w)  # 各资产的最优权重
```

### 模式 5：风险预算配置
```python
# 风险平价（等风险贡献）
risk_parity = rp.RiskParity(
    cov=cov_matrix,       # 协方差矩阵
    returns=asset_returns  # 收益率
)

# 层次风险平价
hrp = rp.HCPortfolio(
    returns=returns,
    codependence='pearson',
    linkage='ward'
)
w_hrp = hrp.optimization()
```

### 模式 6：有效前沿可视化
```python
port = rp.Portfolio(returns=returns)
port.assets_stats(method='hist')

# 绘制有效前沿
rp.plotting.plot_frontier(
    w_frontier=port.frontier,
    mu=port.mu,
    cov=port.cov,
    returns=returns,
    rm='MV',
    rf=0.02
)
```

---

## 三、完整工作流：数据→分析→报告

```python
import akshare as ak
import quantstats as qs
import pandas as pd

# Step 1: 拉数据（financial-data-access）
stocks = {
    '茅台': '600519',
    '五粮液': '000858',
    '宁德时代': '300750',
}
price_data = {}
for name, code in stocks.items():
    df = ak.stock_zh_a_hist(symbol=code, period="daily",
                            start_date="20240101", end_date="20260712")
    price_data[name] = df['收盘']

prices = pd.DataFrame(price_data)

# Step 2: 计算收益率
returns = prices.pct_change().dropna()

# Step 3: quantstats 绩效分析
qs.reports.html(
    returns,
    title="消费板块投资组合分析",
    output="portfolio_report.html"
)
# 打开 portfolio_report.html 即可看到完整分析

# Step 4: Riskfolio 组合优化
import riskfolio as rp
port = rp.Portfolio(returns=returns)
port.assets_stats(method='hist')
opt_weights = port.optimization(model='Classic', rm='MV',
                                 obj='Sharpe', rf=0.02)
```

---


## 📋 Methodology Log（审计链）

每次分析的核心步骤，记录到 `methodology_log`：

```json
{
  "step": "{step_name}",
  "inputs": {"{input_name}": "{input_value}"},
  "reasoning": "{推理过程概要}",
  "confidence": "H/M/L",
  "source": "{信息来源}"
}
```

**必录步骤**：
1. **输入验证**：记录输入参数的来源和完整度
2. **分析决策**：记录每个核心判断的依据和备选方案
3. **结论合成**：记录最终结论如何从分析中推导

> 审计链原则：任何人可以追溯任何一个判断的来源和推理过程。


## 🔄 Fallback Chain（降级链）

当主要分析路径失败时，自动降级到备用方案：

| 优先级 | 方案 | 触发条件 |
|:--:|------|---------|
| 🥇 主方案 | 标准分析流程 | 默认执行 |
| 🥈 降级 1 | 使用简化框架，标注"信息受限" | 关键数据缺失 |
| 🥉 降级 2 | 输出部分分析 + 标注"待补充" | 多项数据不可用 |
| 🏁 兜底 | 清晰告知用户"当前数据不足以完成分析" | 全部路径失败 |

> **永不崩溃原则**：任何时候都不是"分析失败"——而是"在当前信息下输出最佳可用结果"。


## ⚖️ Rule Engine（评分引擎）

采用权重 + 自定义规则的量化评分体系：

| 规则 ID | 检查项 | 权重 | 通过条件 | 通过消息 | 失败消息 |
|---------|------|:--:|---------|---------|---------|
| FIN-ACC | 数据完整性 | 5 | 所有关键指标可获取 | ✅ 数据完整 | ❌ 数据缺失 {gap_count} 项 |
| FIN-CONSIST | 逻辑一致性 | 4 | 各维度数值无矛盾 | ✅ 数据一致 | ❌ 维度 {dim} 存在矛盾 |
| FIN-SOURCE | 数据溯源 | 3 | 所有数据有来源标注 | ✅ 来源完整 | ❌ 来源标注缺失 |

**评分公式**：`分数 = 通过权重 / 总权重 × 100`

> 每条规则完全可审计——知道为什么通过、为什么失败，以及具体数值。


## 🏗️ Schema-First（模式优先）

分析前声明数据的 Schema：

```yaml
# 输入 Schema
