---
name: financial-bp-command-center
version: 1.0.0
qualityGate: enhanced
description: >
  财务BP指挥中心，覆盖4讲22模块业财融合知识体系与8个可执行工具模型
  (量本利分析/客户盈利/供应商评估/预算监控/投资可行性/能力评估/业财融合健康度/AI场景适配)。
  支持建安行业专属参数，每个工具含完整计算逻辑、输入格式、JSON输出。
trigger_words:
  - 财务BP
  - 业财融合
  - 量本利分析
  - 盈亏平衡
  - 预算执行监控
  - 滚动预测
  - 客户盈利分析
  - 供应商评估
  - 投资可行性
  - NPV计算
  - IRR计算
  - 敏感性分析
  - 财务BP能力评估
  - 业财融合健康度
  - AI财务应用
  - 目标利润
  - 安全边际
  - 降本增效
  - 微利时代
  - 经营参谋
  - BP能力模型
  - 战略地图
  - 平衡计分卡
  - 零基预算
  - 销售预测
  - 定价策略
  - 库存周转
  - 安全库存
  - 成本中心
  - 目标成本法
  - 研发加计扣除
  - EVA价值管理
  - 波士顿矩阵
  - 经济可行性
  - financial bp
  - CVP analysis
dependencies:
  strategic-analyst: optional
  tax-risk-early-warning-engine: optional
category: finance-bp
industry: construction-installation
compatibility:
  - python3.10+
disable: false
agent_created: true
---
# 财务BP指挥中心 v1.0.0 — Financial BP Command Center

## 1. 概述

面向财务BP从业者的全维度知识体系与实战工具集，覆盖**4讲22个模块**业财融合方法论，内置**8个可执行工具模型**，每个工具含完整计算逻辑、输入参数、JSON输出。特别适配**建安行业**专属参数。

适用场景：财务BP能力建设、经营分析会准备、预算编制与执行监控、投资决策支持、客户/供应商分析、AI工具选型。

---

## 2. 建安行业专属基准参数

| 参数 | 建安基准 | 通用基准 | 说明 |
|------|---------|---------|------|
| `industry_profit_margin` | 3%-5% | 5%-10% | 利润率偏低 |
| `material_cost_ratio` | 50%-65% | 30%-45% | 材料成本占比高 |
| `labor_cost_ratio` | 20%-30% | 10%-15% | 建筑工人占比高 |
| `subcontract_ratio_limit` | ≤40% | ≤20% | 专业分包普遍 |
| `advance_receipt_cycle` | 180天 | 90天 | 工程进度款周期 |
| `inventory_turnover_target` | ≥4次/年 | ≥6次/年 | 施工周期影响 |
| `asset_liability_ratio_warn` | ≤75% | ≤60% | 垫资施工推高负债 |
| `receivable_turnover_days` | ≤120天 | ≤60天 | 工程款回收慢 |
| `gross_margin_floor` | ≥8% | ≥15% | 行业毛利偏低 |
| `rd_expense_ratio` | ≤1.5% | ≤5% | 建安研发投入低 |

**动态调整公式**:

```
调整系数 σ = Σ(factor_score[i] × weight[i]) / Σ(weight[i])
因子权重: 项目类型(房建0/基建-0.03/工业-0.02/市政0.02/装修0.05) 25%
          企业规模(大型-0.05/中型0/小型+0.05) 20%
          跨省经营(是+0.03/否0) 15%
          简易计税占比>30%(+0.05) 20%
          挂靠经营占比(>30%+0.05/10-30%+0.02/<10%0) 20%
调整后阈值 = 通用基准 × (1 + σ)
```

---

## 3. 知识体系：四讲二十二模块

### 第一讲：思维篇——微利时代与AI浪潮下的财务BP新定位

**模块1-2: 微利时代特征与应对路径**

微利三明治 = 收入天花板(竞争/价格战/需求饱和) + 利润夹心层(上下游挤压/费用刚性) + 成本地板(人工涨/材料涨/合规成本)。MPI指数 = 0.3×CR5集中度 + 0.3×价格弹性 + 0.4×行业利润率倒数；MPI>0.7为高度微利。

三条路径：(1)降本——结构性(工艺/替代/自动化)/执行性(集采/能耗/人效)/战略性(外包/轻资产)；(2)增效——资产效率(周转率/盘活)+人效(对标/技能矩阵)+流程(数字化)；(3)结构优化——产品结构(高毛利占比↑)+客户结构(优质集中度↑)+成本结构(变动弹性↑/固定压缩)。

**模块3: 财务BP核心使命** —— 从"算账"到"经营参谋"

角色进化: 记账员→报表分析师→业务财务→经营参谋→价值共创者。三支柱: 数据洞察力(建模/预警/归因)+业务理解力(行业逻辑/业务语言/痛点识别)+决策影响力(建议落地/资源推动/绩效设计)。

**模块4-5: AI在财务中的应用场景**

| 场景 | AI能力 | 效率 |
|------|--------|------|
| 财务分析报告 | 自动生成经营分析报告 | 3x-5x |
| 异常预警 | 多维度异常检测 | 实时 |
| 智能预测 | 时序预测(销售额/成本/现金流) | 准确率+15% |
| 自动化对账 | 智能匹配(金额+日期±3天+摘要模糊) | 10x |
| 费用合规检测 | 拆分/超标/重复/关联方检测 | 全量扫描 |

建安AI特化: 工程进度AI推演→收入确认优化；材料价格AI预测→投标报价辅助；工地AI巡检→安全隐患+浪费识别。

**模块6: AI不会取代财务BP，但会用AI的财务BP会取代不会用的**

AI优势区: 数据采集/清洗/标准化、常规报告/模板分析、模式识别/异常检测。人类优势区: 跨部门博弈/利益平衡、战略判断/模糊决策、信任建立/影响力建设。

**模块7: 财务BP能力模型(15项)AI时代演化**

硬技能(40%→35%): H1财务建模[8],H2管理会计[7],H3信息系统[7],H4预算管理[6],H5风控[6]
软技能(35%→35%): S1业务洞察[8],S2沟通影响[7],S3分析思维[7],S4项目推动[5],S5商业敏锐[5]
AI素养(新增0%→15%): A1工具应用[5],A2数据驱动[4],A3提示词工程[3],A4自动化[2],A5伦理[1]
综合能力(25%→15%): C1战略思维[6],C2领导力[5],C3学习进化[4]

**模块8: 财务BP四个成长阶段**

执行者(0-3年)→分析者(3-5年)→业务伙伴(5-8年)→价值共创者(8年+)。成长飞轮: 数据能力→洞察发现→建议推动→结果验证→信任积累→更大授权。

**模块9: 微利时代三项新要求** —— 快(Speed)：日报/周报替代月报，异常实时预警，AI辅助加速分析周期。准(Accuracy)：作业成本法替代传统分摊，客户/产品/渠道多维盈利分析穿透到业务真相，现金流质量分析替代账面利润分析。狠(Impact)：经营分析结论必须带行动建议+ROI测算，资源重分配有明确产出预期，跟踪闭环(建议→执行→反馈→迭代)。

**模块9补充：微利指数诊断工具**

```
企业微利压力诊断 = 0.30×(1-收入增长率) + 0.25×(1-毛利率/行业均值) + 0.25×(费用率/行业均值) + 0.20×(应收账款/经营现金流)

诊断区间:
  0.00-0.30: 正常利润区 → 维持策略
  0.30-0.55: 利润承压区 → 启动降本增效
  0.55-0.75: 微利挣扎区 → 战略调整+结构优化
  0.75-1.00: 亏损边缘区 → 激进变革或退出

建安行业快速诊断: 毛利率<6%+费用率>12%+应收/经营现金流>3 → 高度微利
```

---

### 第二讲：战略视角——财务BP如何创造企业价值

**模块10: 资本视角估值逻辑**

企业价值双引擎: PE估值法(价值=净利润×PE) + DCF估值法(价值=ΣFCF[t]/(1+WACC)^t+终值)。估值健康度 = min(PE合理性分, DCF支撑度分)。

**模块11: 经营视角可持续盈利能力**

盈利可持续性 = 盈利质量(主业利润占比/现金流比/减值比) + 成长质量(有机vs并购/新业务进度/研发占比) + 风控质量(客户集中度/供应商依赖/有息负债/EBITDA)。

**模块12: 企业盈利公式拆解**

```
盈利质量 = 资产效率 × 成本控制力 × 现金流质量
资产效率: 总资产周转率=收入/平均总资产，建安≥0.8次/年
成本控制力: 边际贡献率=(收入-变动成本)/收入，建安≥15%
现金流质量: FCF转化率=FCF/EBITDA，≥60%优秀/<40%预警
综合健康度(满分15)=周转率分(1-5)+边际分(1-5)+现金流分(1-5)
```

**模块13: 五大实战动作**

(1)构建业务敏感型财务思维: 财务数据→业务归因→行动方案；(2)动态报表识别假利润: 应收暴增+利润增长=纸面利润/存货积压未减值=隐性亏损/完工百分比激进=提前确认；(3)降本增效资源重分配: 资源倾斜指数=0.4×ROIC/WACC+0.3×毛利率趋势+0.3×市占率变化；(4)全面预算与滚动预测(见BP-TOOL-04)；(5)打破业财数据孤岛: ERP→BI→AI三层架构。

---

### 第三讲：经营视角——财务BP深入业务全流程

**模块14: 战略拆解与预算落地**

战略地图(四层: 财务/客户/流程/学习)→平衡计分卡+OKR→零基预算+滚动预测。AI预算监控: 偏差>15%自动预警/费用超前完成→突击花钱预警/收入<85%→联动成本弹性分析。

**模块15: 营销环节** —— 量本利分析(见BP-TOOL-01)、销售预测(SARIMA+XGBoost)、客户盈利分析(见BP-TOOL-02)、应收账款DSO+坏账准备金+AI智能催收。建安适配: 投标决策=量本利+竞争博弈+战略卡位。

**模块16: 采购与供应链** —— 库存优化(EOQ/安全库存/周转率)、供应商评估(见BP-TOOL-03)、采购TCO总成本=采购价+运输+仓储+质量损失+资金占用、AI异常检测(价差>15%/量异常/新供应商大额采购)。建安适配: 钢材50%+混凝土20%+砂石10%；钢材期货锁价；分包商资质审查+履约保函。

**模块17: 生产运营** —— 成本中心报告(标准vs实际差异分解为价差+量差+效率差)、效率指标(人均产值/工时利用率/设备利用率/材料损耗率)、自制or外包决策。建安适配: 项目部成本=人工25%+材料55%+机械15%+临建5%。

**模块18: 研发环节** —— 目标成本法(目标成本=可接受市价-目标利润)、研发预算里程碑控制、投入产出分析(ROI=预计成果收入×概率/研发投入，ROI<1.5中止)、AI辅助加计扣除合规。建安适配: 研发方向(施工工法/新型建材/绿色建筑/BIM)；加计扣除委托研发80%计入。

**模块19: 投资与并购** —— 波士顿矩阵+三层面分析法、投资可行性分析(见BP-TOOL-05)、AI辅助(行业可比筛选/标的异常检测/估值测算)、投后管理(里程碑监控/整合进度/价值实现vs投资IRR)、EVA=NOPAT-IC×WACC。建安适配: 投资类型(资质并购/搅拌站/BOT/PPP)；关键风险(合规/回款/政府信用)。

---

### 第四讲：成长篇——财务BP的职业发展与自我跃升

**模块20: AI时代三重升级**

能力: 账务处理→业务洞察(轮岗/跟项目/深入一线)；工具: Excel→AI+BI(每周学1个新工具/AI提问练习/自动化流程)；角色: 支持者→影响者(参加业务会议/提出财务建议/跟踪落地)。

**模块21: 财务BP成长五件事**

(1)精通财务建模与AI工具；(2)掌握信息系统(SAP/Oracle/SQL/BI)；(3)灵活运用管理会计工具；(4)发现问题并提出可执行建议(数据→根因→方案→ROI→推动)；(5)深入理解业务逻辑与行业竞争(5 Forces/价值链/竞品对标)。

**模块22: 个人成长建议** —— 构建能力仪表盘(见BP-TOOL-06)、找到BP"主场"(营销/供应链/生产/研发/投资)、持续学习(AI工具/行业知识/商业思维)。

---

## 4. 八大可执行工具模型

---

### BP-TOOL-01: 量本利分析器 (CVP Analyzer)

**公式**:

```
单位边际贡献 = 单价 - 单位变动成本
边际贡献率 = 单位边际贡献 / 单价
盈亏平衡销量 = 固定成本 / 单位边际贡献
盈亏平衡收入 = 固定成本 / 边际贡献率
目标利润销量 = (固定成本 + 目标利润) / 单位边际贡献
安全边际率 = (实际销量 - 盈亏平衡销量) / 实际销量
经营杠杆DOL = 边际贡献 / (边际贡献 - 固定成本)
多产品加权边际贡献率 = Σ(销售占比 × 边际贡献率)

建安: 项目保本产值 = 固定成本 / 0.08 (变动成本率约92%)
```

**阈值**: 安全边际率 红<20% | 黄20-40% | 绿>40%；DOL 红>5 | 黄2-5 | 绿<2；边际贡献率(建安) 红<5% | 黄5-8% | 绿>8%

**输入**:

```json
{"analysis_type": "breakeven|target_profit|safety_margin|scenario",
 "product_list": [{"name": "房建工程","price": 150000000,"unit_variable_cost": 138000000,"sales_volume": 1,"sales_mix_ratio": 0.60}],
 "fixed_cost": 5000000,"target_profit": 3000000,"actual_sales": 150000000,
 "scenarios": [{"name":"乐观","price_change":0.05,"cost_change":-0.03,"volume_change":0.10}],
 "industry": "construction"}
```

**输出**:

```json
{"tool":"BP-TOOL-01","analysis_type":"breakeven",
 "results":{"unit_contribution_margin":12000000,"contribution_margin_ratio":0.08,
  "breakeven_revenue":62500000,"target_profit_revenue":100000000,"safety_margin_ratio":0.583,
  "operating_leverage":2.4,"safety_assessment":"GREEN","assessment_detail":"安全边际率58.3%>40%"},
 "scenario_analysis":[{"scenario":"乐观","breakeven_revenue":58000000,"profit":6500000},
  {"scenario":"基准","breakeven_revenue":62500000,"profit":3000000},
  {"scenario":"悲观","breakeven_revenue":71000000,"profit":1200000}],
 "recommendation":"安全边际充足。悲观情景利润¥120万仍为正，建议锁定主要材料价格合同。"}
```

---

### BP-TOOL-02: 客户盈利分析器 (Customer Profitability Analyzer)

**公式**:

```
客户净利润 = 客户收入 - 直接成本(材料+人工+直接费用) - 分配间接费用
客户盈利率 = 净利润 / 收入
客户CLV = m × r / (1+d-r)  [m=年均边际贡献 r=留存率 d=折现率]
CAC = 销售费用 / 新获客数; CLV/CAC≥3→健康
RFM: R(最近购买)×0.3 + F(频次)×0.3 + M(金额)×0.4 → 1-5分

客户分级: 战略(利润率>20%+收入>5%)/重点(10-20%+>3%)/一般(0-10%)/亏损(<0%)
资源倾斜指数: 0.35×利润率得分 + 0.25×增长潜力 + 0.20×战略匹配 + 0.15×信用 + 0.05×合作年限
  得分>3.5→加大投入 | 2.5-3.5→维持 | <2.5→收缩
```

**输入**:

```json
{"customers": [{"id":"C001","name":"万科地产","revenue":85000000,"direct_material":45000000,
  "direct_labor":18000000,"direct_expense":5000000,"allocated_overhead":8000000,
  "receivables":25000000,"payment_days":95,"years_cooperation":8,"growth_rate":0.15,
  "strategic_fit_score":4.5,"credit_rating":"AAA"}],
 "industry":"construction","include_rfm":true,"include_clv":true}
```

**输出**:

```json
{"tool":"BP-TOOL-02",
 "summary":{"total_customers":15,"total_revenue":380000000,"avg_profit_margin":0.075,
  "strategic":3,"key":5,"general":5,"loss_making":2},
 "customer_ranking":[
  {"rank":1,"id":"C001","name":"万科地产","profit_margin":0.106,"tier":"重点客户",
   "rfm_score":4.2,"clv":42000000,"resource_index":3.8,"resource_action":"加大投入",
   "recommendation":"维持优质服务，争取更多标段。回款周期95天需缩短至80天。"},
  {"rank":15,"id":"C007","name":"XX小型开发商","profit_margin":-0.10,"tier":"亏损客户",
   "rfm_score":1.5,"resource_index":1.8,"resource_action":"收缩",
   "recommendation":"连续亏损2年，回款超180天。建议提高报价20%或逐步退出。"}],
 "pareto_analysis":{"top20_revenue_share":0.72,"top20_profit_share":0.91,
  "insight":"前20%客户贡献72%收入和91%利润，尾部5个客户亏损。"}}
```

---

### BP-TOOL-03: 供应商评估矩阵 (Vendor Evaluation Matrix)

**公式**:

```
综合评分 S = Σ(score[dim_i] × weight[dim_i])

价格(30%): price_score = 100 - (报价-最低)/(最高-最低)×100; 年报降价每1%+2分(上限10)
质量(25%): quality_score = (1-不良率)×60 + 认证×20 + 配合度×20
交期(20%): delivery_score = 准时率×80 + 周期竞争力×20; 准时率<85%→红区
服务(15%): 响应速度(40%)+售后解决率(30%)+技术支持(30%)
财务(10%): 0.3×负债率得分+0.3×流动比率+0.2×利润率+0.2×账期得分

评级: A≥85→战略供应商 | B[70,85)→合格 | C[60,70)→观察 | D<60→淘汰
TCO = 采购价 + 运输 + 仓储 + 质量损失(不良率×采购额) + 资金占用(报价×账期×资金成本/365)
```

**输入**:

```json
{"vendors": [{"id":"V001","name":"XX钢铁集团","category":"主材-钢材","quoted_price":4200,
  "annual_volume":5000,"quality_defect_rate":0.015,"on_time_delivery_rate":0.93,
  "delivery_leadtime_days":7,"asset_liability_ratio":0.62,"current_ratio":1.4,
  "operating_profit_margin":0.06,"payment_terms_days":60,"transport_cost_per_unit":50}],
 "custom_weights":{"price":0.30,"quality":0.25,"delivery":0.20,"service":0.15,"finance":0.10},
 "include_tco":true}
```

**输出**:

```json
{"tool":"BP-TOOL-03",
 "vendor_ranking":[{"rank":1,"id":"V001","name":"XX钢铁集团","composite_score":88.5,
   "grade":"A","dimension_scores":{"price":82,"quality":90,"delivery":88,"service":85,"finance":78},
   "tco":21750000,"recommendation":"A级，建议签年度框架协议锁定价格。"}],
 "comparison_matrix":{"钢材":{"lowest_price":"V003","best_overall":"V001",
   "recommendation":"建议V001(70%)+V003(30%)组合策略，避免单一依赖。"}},
 "construction_notes":{"steel_hedging":"超6个月工期项目做钢材期货套保",
   "concrete_regional":"混凝土受运距限制，按项目地分别评估"}}
```

---

### BP-TOOL-04: 预算执行监控仪表盘 (Budget Execution Dashboard)

**公式**:

```
预算执行率 = 实际额 / 预算额 × 100%
时间进度率 = 已过月数 / 12 × 100% (或按工期)
进度偏差 = 执行率 - 时间进度率

滚动预测 = 已发生实际 + 未来预测
  未来预测 = 趋势法(近3月均值×季节因子)×0.6 + 基准法(全年预算/12)×0.4
  预测偏差率 = |最新预测 - 年度预算| / 年度预算 → >15%触发预算调整

异常检测: |当月实际-12月均值|/12月标准差 > 2.5σ→红区
预算松弛: Q4松弛指数 > Q1-Q3均值×1.5 → 疑似年末突击花钱

三级预警: 🔴 偏差>20%或超预算 | 🟡 偏差10-20% | 🟢 偏差<10%
```

**输入**:

```json
{"budget_items": [{"category":"收入","sub_category":"房建业务收入","annual_budget":200000000,
  "ytd_actual":95000000,"months_elapsed":7,"last3m_actual":[13800000,14200000,15500000],
  "seasonal_factor":[0.07,0.06,0.07,0.08,0.08,0.09,0.09,0.09,0.10,0.10,0.09,0.08]}],
 "thresholds":{"red":0.20,"yellow":0.10},"industry":"construction",
 "enable_rolling_forecast":true,"detect_budget_slack":true}
```

**输出**:

```json
{"tool":"BP-TOOL-04","report_period":"2026-07 (YTD M7)",
 "summary":{"budget_execution_rate":0.475,"time_progress_rate":0.583,
  "progress_deviation":-0.108,"rolling_forecast":188500000,"forecast_vs_budget":-0.057,
  "overall_status":"YELLOW","assessment":"收入完成率47.5%，落后时间进度10.8pp。"},
 "alerts":[
  {"item":"房建业务收入","status":"YELLOW","deviation":-0.108,
   "recommendation":"重点关注已完工未结算¥3200万，推动业主签证确认。"},
  {"item":"管理费用-差旅费","status":"RED","execution_rate":0.72,"deviation":0.137,
   "recommendation":"差旅费执行超前72%，核查跨期报销。收紧Q3审批。"}],
 "rolling_forecast_detail":{"H2_forecast":93500000,"confidence_80":[85500000,102000000],
   "key_drivers":["Q4集中结算约占全年35%","3个在谈EPC项目预计¥1800万"]},
 "budget_slack":[{"category":"办公费","slack_q4_historical":0.35,"flag":"PROBABLE",
   "recommendation":"审核Q4年末采购合理性。"}]}
```

---

### BP-TOOL-05: 投资可行性分析器 (Investment Feasibility Analyzer)

**公式**:

```
NPV = Σ(CF[t]/(1+r)^t) - I0  → NPV>0可行
IRR: 使NPV=0的折现率 → IRR>WACC可行
静态回收期 = I0 / 年均现金流
动态回收期 = 累计折现现金流首次为正的年份
PI = (NPV+I0)/I0  → PI>1可行
EVA = NOPAT - (投入资本×WACC)  → EVA>0创造价值
  年EVA = EBIT×(1-T) - 年初净资产×WACC

建安WACC基准: Re=2.5%+1.2×6%=9.7%  Rd=4.5%×(1-25%)=3.375%
  WACC = 9.7%×E/V + 3.375%×D/V  → 房建8-10%/基建7-9%/PPP 6-8%
```

**输入**:

```json
{"project_name":"XX产业园EPC项目","initial_investment":85000000,"project_life_years":5,
 "annual_cashflows":[15000000,22000000,25000000,22000000,18000000],
 "terminal_value":5000000,"wacc":0.09,"tax_rate":0.25,"depreciation_annual":16000000,
 "invested_capital":85000000,
 "sensitivity_variables":[{"name":"收入变动","base":1.0,"range":[-0.20,-0.10,0.10,0.20]},
  {"name":"成本变动","base":1.0,"range":[-0.20,0.20]},{"name":"WACC","base":0.09,"range":[0.07,0.11]}],
 "industry":"construction","include_eva":true}
```

**输出**:

```json
{"tool":"BP-TOOL-05",
 "investment_summary":{"npv":4250000,"irr":0.112,"irr_vs_wacc":0.022,
  "static_payback_years":3.86,"dynamic_payback_years":4.45,"pi":1.05,
  "decision":"APPROVE_WITH_CONDITIONS","detail":"NPV为正¥425万，IRR=11.2%>WACC=9%，PI=1.05偏低需严控成本。"},
 "sensitivity_analysis":{"npv_tornado":[
  {"variable":"收入-20%","npv":-8200000,"impact":"RED"},
  {"variable":"收入-10%","npv":-1950000,"impact":"RED"},
  {"variable":"收入+10%","npv":10450000,"impact":"GREEN"},
  {"variable":"成本+20%","npv":-3300000,"impact":"RED"},
  {"variable":"WACC=11%","npv":1200000,"impact":"YELLOW"}],
  "breakeven":{"variable":"收入","change":-0.067,"note":"收入降6.7%即NPV归零"}},
 "eva_analysis":[{"year":1,"eva":3600000},{"year":2,"eva":10380000},{"year":3,"eva":14160000}],
 "construction_notes":["建安收入确认依赖完工百分比，存调差风险","主要材料做价格锁定","政府项目关注财政可承受论证"]}
```

---

### BP-TOOL-06: 财务BP能力评估仪表盘 (BP Competency Dashboard)

**公式**:

```
综合能力分 = Σ(自评分[i] × 权重[i]) / Σ(权重[i])
强项: 得分 > 综合分 + 0.5 | 弱项: 得分 < 综合分 - 0.5
差距 = 目标分 - 当前分；优先提升 = 差距最大的前3项(按权重加权)
阶段: 综合<2.5→执行者 | 2.5-3.5→分析者 | 3.5-4.25→业务伙伴 | ≥4.25→价值共创者
```

**输入**:

```json
{"self_assessment":{"H1_财务建模":3.5,"H2_管理会计":3.0,"H3_信息系统":2.5,"H4_预算管理":3.0,
  "H5_风控":2.5,"S1_业务洞察":3.5,"S2_沟通影响":3.0,"S3_分析思维":4.0,"S4_项目推动":2.5,
  "S5_商业敏锐":3.0,"A1_AI工具":2.0,"A2_数据驱动":2.5,"A3_提示词":1.5,"A4_自动化":1.0,
  "A5_AI伦理":2.0},"target_stage":"业务伙伴","years_experience":5}
```

**输出**:

```json
{"tool":"BP-TOOL-06","composite_score":2.67,
 "current_stage":"分析者","target_stage":"业务伙伴","stage_gap":"需提升至3.5+",
 "dimension_scores":{"硬技能":2.90,"软技能":3.20,"AI素养":1.80,"综合":2.90},
 "strengths":[{"competency":"S3_分析思维","score":4.0}],
 "weaknesses":[{"competency":"A4_自动化","score":1.0},{"competency":"A3_提示词","score":1.5}],
 "priority_actions":[
  {"rank":1,"competency":"A1_AI工具","gap":1.5,"action":"每周学1个AI工具场景，从DeepSeek辅助经营分析报告开始"},
  {"rank":2,"competency":"A2_数据驱动","gap":1.0,"action":"搭建个人BI看板替代Excel图表"},
  {"rank":3,"competency":"S2_沟通","gap":1.0,"action":"经营分析会上提出2-3条业务改进建议并跟踪落地"}],
 "learning_path":{"month_1_3":["AI工具: DeepSeek辅助分析","每周1个BI练习"],
  "month_4_6":["Python数据分析基础","业务端轮岗或跟项目"],
  "month_7_12":["搭建个人分析系统","主导1个跨部门改善项目"]}}
```

---

### BP-TOOL-07: 业财融合健康度检查 (Business-Finance Integration Health Check)

**公式**:

```
六大评估维度 (满分100):

D1 数据基础(17分): 主数据覆盖率×0.5+准确率×0.5→×10 + 系统集成度×7
D2 分析能力(17分): 维度覆盖(产品/客户/区域/渠道/项目各3.4分) + 工具(Excel3/BI5/AI+BI7) + 满意度×3
D3 业务嵌入度(17分): 会议频率(0-5分) + 了解环节数(每环节+2) + 业务满意度×7
D4 决策影响力(17分): 建议数×采纳率×单次价值分 归一化
D5 预算管控力(17分): 准确率×8 + BP参与度×5 + (1-红色预警率)×4
D6 工具与AI(17分): AI使用率×9 + 自动化率×8

综合健康度 = Σ(6维度) | 等级: ≥85优秀 | 70-85良好 | 55-70一般 | <55薄弱
```

**输入**:

```json
{"data_foundation":{"master_data_coverage":0.85,"data_accuracy":0.92,
  "integrated_systems":3,"total_systems":5},
 "analytical_capability":{"covered_dimensions":["产品","客户","项目"],"tool_level":"BI",
  "business_satisfaction_pct":0.72},
 "business_embedding":{"meeting_participation":"经常","understood_biz_areas":3,
  "business_satisfaction_pct":0.75},
 "decision_influence":{"proposals_p90":6,"adoption_rate":0.60,"avg_value_score":3.5},
 "budget_control":{"budget_accuracy":0.82,"bp_participation_rate":0.75,"red_alert_ratio":0.12},
 "tools_and_ai":{"ai_scenarios_used":3,"total_applicable":10,"automated_processes":2,"total_automatable":8}}
```

**输出**:

```json
{"tool":"BP-TOOL-07","composite_health_score":62.5,"grade":"一般",
 "grade_description":"部分融合，需系统提升。离\"良好\"差7.5分。",
 "dimension_scores":{"D1_数据基础":10.2,"D2_分析能力":10.8,"D3_业务嵌入":11.5,
  "D4_决策影响":12.6,"D5_预算管控":10.4,"D6_工具AI":7.0},
 "radar_benchmark":{"industry_avg_construction":55,"industry_avg_manufacturing":68,"best_practice":85},
 "improvement_plan":[
  {"priority":1,"dimension":"D6_工具与AI","gap":10,"actions":[
   "引入DeepSeek/GPT辅助经营分析报告撰写","搭建PowerBI监控看板替代Excel月报",
   "试点AI自动对账(银行流水vsERP应收账款)"]},
  {"priority":2,"dimension":"D5_预算管控","gap":6.6,"actions":[
   "建立滚动预测机制(季度滚动+月度更新)","设计预算执行预警规则(偏差>15%自动提醒)"]},
  {"priority":3,"dimension":"D1_数据基础","gap":6.8,"actions":[
   "推进ERP-BI-AI三层数据架构","统一主数据标准(客户/供应商/物料/项目编码)"]}],
 "construction_note":"建安业财融合水平普遍偏低(55分)，重点方向:项目成本实时管控+进度款预测+材料价格联动。"}
```

---

### BP-TOOL-08: AI财务应用场景适配器 (AI Finance Scenario Adapter)

**公式**:

```
场景适配分 = 0.30×痛点匹配度 + 0.25×技术成熟度 + 0.20×(6-实施难度) + 0.15×ROI预期 + 0.10×数据就绪度
各维度1-5分 → 优先推荐≥4.0立即行动 | 中等3.0-4.0三个月计划 | 待观察<3.0持续关注
```

**输入**:

```json
{"enterprise_profile":{"industry":"construction","scale":"medium","annual_revenue":5e8,
  "employee_count":800,"finance_team_size":15,"current_systems":["用友U8","Excel","金蝶"],
  "data_readiness_level":3,"it_budget":"limited"},
 "top_pain_points":["项目成本超支频繁，事后发现无法补救",
  "各项目部数据零散，汇总分析耗时5天","应收账款管理靠Excel，催收不及时"],
 "maturity_level":"beginner"}
```

**输出**:

```json
{"tool":"BP-TOOL-08",
 "enterprise_summary":{"scale":"中型建安企业","maturity":"AI初学者","data_readiness":"中等(3/5)",
  "key_bottleneck":"数据分散+预算有限，需轻量级方案"},
 "recommended_scenarios":[
  {"rank":1,"scenario":"AI辅助经营分析报告","fit_score":4.5,"priority":"立即行动",
   "pain_point":"解决汇总分析耗时5天","solution":"DeepSeek/GPT+项目数据→自动生成周/月报告",
   "effort":"1周","roi":"月节省5天人工，年化ROI 8x","risk":"低"},
  {"rank":2,"scenario":"项目成本实时预警看板","fit_score":4.2,"priority":"立即行动",
   "pain_point":"解决成本超支事后发现","solution":"PowerBI/简道云+成本偏差规则引擎",
   "effort":"4周","roi":"减少10%成本超支，年化¥200万+"},
  {"rank":3,"scenario":"智能应收催收","fit_score":3.8,"priority":"3个月计划",
   "pain_point":"解决催收不及时","solution":"应收仪表盘+AI逾期预测+自动催收邮件",
   "effort":"6周","roi":"DSO缩短15天，释放营运资金¥2000万"}],
 "quick_wins":[{"action":"注册DeepSeek，AI辅助1篇经营分析报告","time":"今天","cost":"免费"},
  {"action":"用PowerBI免费版搭收入/成本看板","time":"本周","cost":"免费"}],
 "construction_specific":[{"scenario":"材料价格预测","value":"钢材/混凝土价格波动预测辅助投标"},
  {"scenario":"工程进度AI推演","value":"基于天气/人员/材料预测完工时间","phase":"二期"}],
 "learning_roadmap":{"immediate":["AI辅助报告","Excel自动化"],"3_months":["BI看板","智能应收"],
  "6_months":["全面预算AI","材料价格预测"],"12_months":["AI驱动经营决策系统"]}}
```

---

## 5. 行业场景速查表

| 业务场景 | 推荐工具 | 关键输出 | 建安适配 |
|---------|---------|---------|---------|
| 项目投标决策 | BP-TOOL-01 + BP-TOOL-05 | 盈亏平衡+敏感性 | 材料价格联动+竞争博弈 |
| 季度经营分析 | BP-TOOL-01/02/04 | 盈利分析+预算偏差 | 完工百分比调整 |
| 客户策略调整 | BP-TOOL-02 | 客户分层+资源倾斜 | 发包方信用分级 |
| 供应商年审 | BP-TOOL-03 | 评级+TCO比拼 | 钢材/混凝土区域比价 |
| 年度预算编制 | BP-TOOL-04 + BP-TOOL-01 | 滚预测+盈亏底线 | 零基+项目制预算 |
| 投资决策 | BP-TOOL-05 | NPV/IRR/敏感性 | PPP/BOT特有风险 |
| BP团队建设 | BP-TOOL-06/07 | 能力雷达+融合度 | 项目部BP培养路径 |
| AI工具选型 | BP-TOOL-08 | 场景推荐+ROI | 轻量方案优先 |

---

## 7. 执行流程

```
触发词检测 → 意图解析
    ↓
    ├── 能力评估 → BP-TOOL-06
    ├── 工具计算 → 关键词路由:
    │   ├── 量本利/盈亏平衡/定价 → BP-TOOL-01
    │   ├── 客户分析/盈利分析 → BP-TOOL-02
    │   ├── 供应商/采购评估 → BP-TOOL-03
    │   ├── 预算执行/滚动预测 → BP-TOOL-04
    │   ├── 投资/NPV/IRR → BP-TOOL-05
    │   ├── 业财融合评估 → BP-TOOL-07
    │   └── AI工具选型 → BP-TOOL-08
    ├── 建安行业 → 加载专属参数+调整系数
    └── 知识咨询 → 从22模块知识库检索
    ↓
工具执行: 参数校验 → 计算引擎 → 结果生成
    ↓
格式化输出: JSON结构化 + 行动建议
    ↓
可选联动: strategic-analyst(战略分析) / tax-risk-early-warning-engine(税务风险)
```

## 8. 工具间联动关系

```
BP-TOOL-01 量本利 → 支撑 BP-TOOL-04 预算编制(盈亏平衡为预算底线)
BP-TOOL-02 客户盈利 → 联动 BP-TOOL-01 客户层面量本利
BP-TOOL-03 供应商评估 → 影响 BP-TOOL-01 变动成本参数
BP-TOOL-04 预算监控 → 触发 BP-TOOL-01 重新量本利分析
BP-TOOL-05 投资分析 → 联动 BP-TOOL-04 将投资项目纳入滚预测
BP-TOOL-06 能力评估 → 识别弱项→联动 BP-TOOL-08 工具匹配
BP-TOOL-07 融合健康度 → 识别薄弱→联动 BP-TOOL-06/08 定向提升
BP-TOOL-08 场景适配 → AI工具落地→反馈到 BP-TOOL-07 D6评分
```

## 9. 调用示例

```bash
# 自然语言触发
"帮我做万科项目的量本利分析，固定成本500万，单价1.5亿，变动成本1.38亿"
  → BP-TOOL-01 盈亏平衡+安全边际+敏感性分析

"评估季度预算执行，7月已结束，收入预算2亿完成9500万"
  → BP-TOOL-04 预算仪表盘+滚预测+异常预警

"我是5年经验的财务BP，想做能力自评"
  → BP-TOOL-06 引导输入→雷达图+成长建议

"我们公司业财融合做得怎么样，做个健康度检查"
  → BP-TOOL-07 6维度输入→综合评分+改进计划

"建安企业适合用什么AI工具"
  → BP-TOOL-08 按企业画像推荐场景

# 命令行
python scripts/bp_tools.py --tool cvp --price 1.5e8 --vc 1.38e8 --fc 5e6 --target-profit 3e6
python scripts/bp_tools.py --tool budget --input budget_2026Q3.csv --industry construction
python scripts/bp_tools.py --tool competency --self-assess self_scores.json
```

## 10. 脚本结构（如实现）

```
financial_bp/
├── bp_tools.py                  # 主入口
├── tools/
│   ├── cvp_analyzer.py          # BP-TOOL-01
│   ├── customer_profit.py       # BP-TOOL-02
│   ├── vendor_matrix.py         # BP-TOOL-03
│   ├── budget_dashboard.py      # BP-TOOL-04
│   ├── investment_feasibility.py # BP-TOOL-05
│   ├── competency_dashboard.py  # BP-TOOL-06
│   ├── integration_health.py    # BP-TOOL-07
│   └── ai_scenario_adapter.py   # BP-TOOL-08
├── knowledge/
│   ├── module_01_09.py          # 第一讲
│   ├── module_10_13.py          # 第二讲
│   ├── module_14_19.py          # 第三讲
│   └── module_20_22.py          # 第四讲
├── industry/construction.py     # 建安专属参数
└── config.py                    # 全局配置与阈值
```

**关键函数签名**:

```python
def calc_breakeven(price: float, unit_vc: float, fixed_cost: float,
                   industry: str = "construction") -> BreakevenResult: ...

def analyze_customer_profitability(customers: list[dict],
                                   industry: str = "construction") -> CustomerReport: ...

def evaluate_vendor(vendors: list[dict], weights: dict = None,
                    include_tco: bool = True) -> VendorRanking: ...

def monitor_budget(budget_items: list[dict], enable_forecast: bool = True,
                   detect_slack: bool = True) -> BudgetReport: ...

def analyze_investment(cashflows: list[float], initial: float, wacc: float,
                       sensitivity: bool = True, include_eva: bool = True) -> InvestmentResult: ...

def assess_competency(self_scores: dict, target_stage: str = None) -> CompetencyReport: ...

def check_integration_health(data: dict,
                             industry: str = "construction") -> HealthReport: ...

def recommend_ai_scenarios(profile: dict,
                           pain_points: list[str]) -> ScenarioRecommendation: ...
```

**最小输入数据集模板**:

```csv
# cvp_input.csv
product,price,unit_vc,fixed_cost,volume,target_profit
房建工程,1.5e8,1.38e8,5e6,1,3e6

# customer_input.csv
id,name,revenue,direct_material,direct_labor,direct_expense,allocated_overhead,receivables,payment_days
C001,万科,85000000,45000000,18000000,5000000,8000000,25000000,95

# vendor_input.csv
id,name,category,quoted_price,annual_volume,defect_rate,on_time_rate,leadtime_days,asset_liability,current_ratio
V001,XX钢铁,钢材,4200,5000,0.015,0.93,7,0.62,1.4

# budget_input.csv
category,sub_category,annual_budget,ytd_actual,months_elapsed
收入,房建业务收入,200000000,95000000,7
成本,直接材料,110000000,52000000,7
费用,管理费用,15000000,10800000,7

# investment_input.csv
project,year0,year1,year2,year3,year4,year5,terminal,wacc
XX产业园EPC,-85000000,15000000,22000000,25000000,22000000,18000000,5000000,0.09
```

## 11. 法规与标准参考

| 标准/框架 | 适用模块 |
|-----------|---------|
| COSO企业风险管理框架 | 模块5/14 |
| 管理会计应用指引(财会[2017]24号) | 模块15-19 |
| 企业会计准则第14号—收入 | 模块15(建安) |
| 全面预算管理指引 | 模块14 |
| EVA价值管理(国资委考核) | 模块19 |
| 研发费用加计扣除(财税[2015]119号) | 模块18 |

## 12. 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.0.0 | 2026-07-02 | 初始版本：4讲22模块 + 8工具模型 + 建安行业参数 |

---

## Zcode 集成

### 兼容性声明

- **等级**: compatible
- **τ_role**: cognizer
- **状态**: 此技能为非 `agent_created` 技能，遵循 `transparent` 兼容协议
- **Bus 兼容**: 可通过 `trigger_recommended` 匹配路由，不修改内部逻辑
- **参考标准**: `skills/shared/zcode/zcode-embedding-standard.md`

---
*Zcode 兼容声明 v1.0 | © 版权所有：默笙夏夏の知書房 - 2026-07-09*
