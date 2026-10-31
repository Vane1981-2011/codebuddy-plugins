---
name: "tax-risk-early-warning-engine"
description: >
  建安企业税务风险预警引擎，覆盖发票/特殊业务/收入/成本费用4大类15个预警指标， 含数学公式、三区阈值、建安专属调整系数、JSON输出，适配金税四期稽查逻辑。
version: "1.0.0"
agent_created: true
qualityGate: "enhanced"
category: "finance-tax"
dependencies:
  strategic-analyst: "optional"
zcode:
  version: "1.0"
  τ_role: "executor"
  τ_impact:
    - {'metric': 'τ_execute', 'direction': 'reduce', 'target': '20%', 'mechanism': '15个预警指标的自动化扫描管线'}
    - {'metric': 'τ_qa', 'direction': 'auto', 'target': 'auto', 'mechanism': '金税四期规则自动匹配校验'}
  bus_compatible: true
  cross_validate_with:
    - contract-risk-scanner
    - financial-bp-command-center
trigger_words:
  - 税务风险预警
  - 建安税务风险
  - 税收风险扫描
  - 税务预警指标
  - 金税预警
  - 发票风险
  - 收入风险
  - 成本费用风险
  - tax risk scan
  - 税务稽查
industry: "construction-installation"
compatibility:
  - python3.10+
disable: false
---
# 建安企业税务风险预警引擎 v1.0.0

## 1. 概述

专为建安企业设计的金税四期风险预警引擎，覆盖 **4大类15个预警指标**，支持多源数据接入、三区预警（红/黄/绿）、建安行业专属系数自动校准、JSON结构化输出。

适用场景：月度自查、稽查应对、并购尽调、年终审计。

## 2. 建安行业专属调整参数

建安行业与制造业存在系统性差异，全局应用以下基准参数：

| 参数 | 建安基准 | 通用基准 | 说明 |
|------|---------|---------|------|
| `profit_margin` | 3%-5% | 5%-10% | 利润率偏低是行业常态 |
| `expense_ratio` | 8%-12% | 5%-8% | 异地施工推高费用 |
| `material_cost_ratio` | 50%-65% | 30%-45% | 材料成本占比高 |
| `labor_cost_ratio` | 20%-30% | 10%-15% | 建筑工人工资占比高 |
| `vat_rate` | 9%/3% | 13%/6% | 建安服务低税率 |
| `advance_receipt_max_days` | 180天 | 90天 | 工程进度款周期长 |
| `subcontract_ratio` | ≤40% | ≤20% | 专业分包普遍 |
| `no_invoice_cost_limit` | ≤5% | ≤2% | 零星采购场景特殊 |

**动态调整公式**：

```
调整后阈值 = 通用阈值 × (1 + σ)

σ = Σ(score[i] × weight[i]) / Σweight[i]

因子权重: 企业规模 20% | 施工类型 25% | 跨省经营 15% | 简易计税占比>30% 20% | 挂靠经营 20%
规模系数: 大型(-0.05) / 中型(0) / 小型(+0.05)
```

---

## 3. 十五大预警指标体系

### 3.1 发票类风险预警 (INV)

---

#### INV-01 进销项发票背离度

**公式**：

```
S_category = 1 - |销项主品类 ∩ 进项主品类| / |销项主品类|
S_qty = |销项总量 - 预期投料量| / max(销项总量, 0.01)
背离度 = 0.6 × S_category + 0.4 × S_qty
```

**阈值**: 红≥0.70 | 黄[0.40,0.70) | 绿<0.40

**数据源**: 金税系统发票查询导出

**JSON输出**:

```json
{"indicator_id":"INV-01","risk_level":"RED","score":0.82,"period":"2026-06",
 "detail":{"sales_categories":["建筑服务"],"purchase_categories":["钢材","矿产品"],
 "category_overlap_ratio":0.33,"deviation_ratio":0.55},
 "recommendation":"进项钢材/矿产品为主，销项建筑服务，背离度高。核查：(1)未开票材料销售 (2)虚开进项冲抵人工。"}
```

---

#### INV-02 发票开具与接收异常

**公式**：

```
集中开票度 C = 开票最多连续3日金额 / 月开票总额
顶格开票率 A = 单张≥限额×95%的张数 / 总张数
作废异常率 V = (当月作废额 - 12月月均作废额) / 12月月均作废额
红字发票率 R = 红字金额 / 开票总额
综合分 = max(C, A×1.2, max(V,0)×0.8, R×1.5)
```

**阈值**:

| 指标 | 红区 | 黄区 | 绿区 |
|------|------|------|------|
| C | ≥0.60 | [0.40,0.60) | <0.40 |
| A | ≥0.10 | [0.05,0.10) | <0.05 |
| V | ≥1.50 | [0.50,1.50) | <0.50 |
| R | ≥0.05 | [0.02,0.05) | <0.02 |

**数据源**: 金税系统发票统计报表

```json
{"indicator_id":"INV-02","risk_level":"YELLOW","score":0.55,"period":"2026-06",
 "detail":{"concentration":0.52,"top_amount_ratio":0.03,"void_anomaly":1.20,"red_invoice_ratio":0.01},
 "recommendation":"月底集中开票度偏高，作废率略超正常波动。核实是否对应实际工程进度。"}
```

---

#### INV-03 进项税额抵扣异常

**公式**：

```
简易计税占比 S = 简易计税销售额 / 总销售额
混抵风险 = 简易项目进项税额 / (总进项×S)        -- >0.10 红区
不得抵扣占比 = 六类不得抵扣进项合计 / 总进项      -- >0.02 红区(建安应极少)
抵扣偏离度 = |实际抵扣率 - 理论抵扣率| / 理论抵扣率
  理论抵扣率 = (材料成本率×13% + 分包成本率×3%) / 9%
```

**阈值**: 红：混抵>0.10 / 不得抵扣占比>0.02 / 偏离度>0.30 | 黄：混抵(0.03,0.10] / 占比(0.01,0.02] / 偏离度(0.15,0.30] | 绿：≤对应下界

**数据源**: 增值税申报表附表二 + 简易计税项目清单

```json
{"indicator_id":"INV-03","risk_level":"RED","score":0.91,"period":"2026-06",
 "detail":{"simple_tax_ratio":0.35,"mix_risk":0.18,"prohibited_ratio":0.03,"deviation":0.42,"actual_rate":0.30,"expected_rate":0.21},
 "recommendation":"简易项目混抵风险明显，实际抵扣率高9个百分点。立即排查并做进项转出。","urgency":"立即处理"}
```

---

#### INV-04 虚开发票关联预警

**公式**：

```
关联标记 = 上游企业同控制人/同地址/同联系人 → 1
资金回流速 = 对上游付款后 N 日内等额回流金额 / 付款金额
三流不一致度 = 0.33×(合同≠发票) + 0.33×(付款方≠受票方) + 0.33×(金额≠发票额)
综合风险 = max(关联标记×0.6, 资金回流速×0.9, 三流不一致度×0.8)
```

**阈值**: 红：资金回流速≥0.80且≤7日 / 三流不一致度≥0.80 / 关联标记=1 | 黄：回流速≥0.50 / 不一致度≥0.60 | 绿：低于黄区下界

**数据源**: 金税股东/高管信息 + 银行流水 + 合同台账 + 发票台账

```json
{"indicator_id":"INV-04","risk_level":"RED","score":0.95,"period":"2026-06",
 "detail":{"related_flag":1,"related_detail":"上游A公司与项目经理同一人",
 "fund_flowback":{"amount":5000000,"flowback":4850000,"ratio":0.97,"days":3},
 "three_flow_mismatch":0.33},
 "recommendation":"关联方+付款后3日97%回流，严重虚开嫌疑。停止交易，保全证据，咨询税务律师。","urgency":"最高优先级"}
```

---

### 3.2 特殊业务与优惠类风险预警 (SPEC)

---

#### SPEC-05 简易计税与差额计税涉税风险

**公式**：

```
简易合规分 = 1 - (不合规项目数 / 简易项目总数)
  不合规判定：清包工合同缺甲供材条款 | 甲供工程缺清单 | 老项目缺开工证明 | 兼营未分别核算

差额合规分 = 1 - (差额扣除不合规笔数 / 总扣除笔数)
  不合规判定：缺合同/发票/付款三件套 | 超出合同金额 | 已抵扣进项又差额扣除 | 非分包支出纳入
```

**阈值**: 红<0.85(简易)/<0.90(差额) | 黄[0.85,0.95)/[0.90,0.95) | 绿≥0.95

**数据源**: 简易计税备案台账 + 差额扣除明细 + 分包合同档案

```json
{"indicator_id":"SPEC-05","risk_level":"YELLOW","score":0.65,"period":"2026-06",
 "detail":{"simple_tax_projects":8,"noncompliant":1,"reason":"清包工合同缺甲供材条款",
 "differential_items":35,"noncompliant_deduct":2,"reasons":["缺付款凭证¥380K","管理费¥65K错误扣除"]},
 "recommendation":"补充甲供材条款或变更一般计税；转出错误扣除管理费。"}
```

---

#### SPEC-06 免征增值税项目涉税风险

**公式**：

```
免税合规分 = 1 - (不合规免税项目数 / 免税项目总数)
应转出进项 = 免税收入 / (免税+应税收入) × 全部进项税额
转出充足率 = 实际转出 / 应转出进项
转出偏差率 = |转出充足率 - 1|
```

**阈值**: 红<0.90/偏差率>0.20 | 黄[0.90,0.95)/偏差率(0.10,0.20] | 绿≥0.95/偏差率≤0.10

**数据源**: 免税项目备案表 + 增值税申报表附表二

```json
{"indicator_id":"SPEC-06","risk_level":"YELLOW","score":0.60,"period":"2026-06",
 "detail":{"free_revenue":8500000,"taxable_revenue":42000000,"required_transfer":520000,"actual_transfer":390000,"deviation":0.25},
 "recommendation":"进项转出不足¥13万，需补转并补缴增值税。"}
```

---

#### SPEC-07 不征税收入与免税收入混淆

**公式**：

```
不征税合规分: 未单独核算→-0.3 | 对应支出税前扣除→-0.4 | 不满足财税[2011]70号三条件→-0.3
免税合规分: 含不应免税项目→-0.5 | 股息持有未满12月→-0.5
混淆标记: 不征税填入免税行或相反 → 直接红区
```

**阈值**: 红<0.70(不征税)/<0.80(免税)/混淆=是 | 黄[0.70,0.90)/[0.80,0.90) | 绿≥0.90

**数据源**: 企税申报表A101010+A107010+A105000+政府补贴文件

```json
{"indicator_id":"SPEC-07","risk_level":"RED","score":0.88,"period":"2026-06",
 "detail":{"non_taxable":2000000,"source":"住建局补贴","confusion":true,
 "issue":"应税补贴错误填列不征税，对应支出¥120万未调增","estimated_underpayment":312000},
 "recommendation":"更正申报，调增应纳税所得额，预计补税¥31.2万。"}
```

---

### 3.3 收入类风险预警 (INC)

---

#### INC-08 增值税与所得税申报收入差异

**公式**：

```
差异额 = 增值税全年销售额 - 企业所得税营业收入
调整后差异 = 差异额 - 跨期结算差异 - 未开票已确认所得税 - 质保金差异
差异率 = |调整后差异| / max(增值税销售额, 企税收入, 1)
建安系数 = 1 + 简易占比×0.3 + 跨省标记×0.15
最终差异率 = 差异率 / 建安系数
```

**阈值**: 红>0.10 | 黄(0.05,0.10] | 绿≤0.05

**数据源**: 增值税申报主表 + 企税年度申报A100000

```json
{"indicator_id":"INC-08","risk_level":"YELLOW","score":0.62,"period":"2026-06",
 "detail":{"vat_revenue":287000000,"cit_revenue":274500000,"adjusted_diff":2500000,"adjusted_rate":0.067},
 "recommendation":"调整后差异率6.7%略超绿区，核查剩余差异是否漏记收入。"}
```

---

#### INC-09 预收账款与应收账款异常

**公式**：

```
预收异常 P = 超期预收(>180天)金额 / 总预收余额
应收异常 R = 0.5×(应收增长率-收入增长率)/max(收入增长率,0.05) 
           + 0.3×(应收周转天数/180-1) + 0.2×(坏账准备率/0.05)
综合 = max(P, R)
```

**阈值**: 红：P>0.30 / R>0.80 | 黄：P(0.15,0.30] / R(0.40,0.80] | 绿：P≤0.15 / R≤0.40

**数据源**: 资产负债表 + 预收/应收辅助核算 + 工程结算台账

```json
{"indicator_id":"INC-09","risk_level":"RED","score":0.86,"period":"2026-06",
 "detail":{"advance":{"balance":18500000,"aged_180d":12300000,"ratio":0.665,
 "top":[{"project":"海悦府二期","amount":5800000,"days":320,"progress":"已封顶"}]},
 "ar":{"growth":0.449,"revenue_growth":0.18,"score":0.68}},
 "recommendation":"预收¥1230万超180天未转收入，海悦府已封顶320天。立即核实纳税义务发生时间。"}
```

---

#### INC-10 资金流与收入不匹配

**公式**：

```
收入覆盖比 = 月度银行经营性流入 / 同期增值税月均销售额
背离度 = |覆盖比 - 1|
季度偏差 Q = |Σ季度经营性流入 - Σ季度销售额| / max(Σ流入, 1)
```

**阈值**: 红：覆盖比<0.60或>1.60 / Q>0.30 | 黄：覆盖比[0.60,0.80)或(1.30,1.60] / Q(0.15,0.30] | 绿：[0.80,1.30]/Q≤0.15

**数据源**: 银行流水 + 增值税申报表

```json
{"indicator_id":"INC-10","risk_level":"YELLOW","score":0.58,"period":"2026-Q2",
 "detail":{"inflow":82000000,"vat_revenue":68500000,"coverage":1.20,"deviation":0.165,
 "suspicious":[{"date":"2026-05-15","amount":6200000,"remitter":"XX劳务公司"}]},
 "recommendation":"银行流入高13%，关注不明大额转账是否属未开票收入。"}
```

---

#### INC-11 不征税/免税收入违规

**公式**：

```
不征税正确性: 不符合财税[2011]70号三条件→违规 | 支出未调增→违规 | 5年未支出未缴回→违规
免税正确性: 含不应免税项目→违规 | 投资方与被投资方税负差未调整→违规
违规分 = 违规项目累计金额 / (不征税+免税收入)总额
```

**阈值**: 红>0.15 | 黄(0.05,0.15] | 绿≤0.05

**数据源**: 企税汇算表 + A105000 + A107010

```json
{"indicator_id":"INC-11","risk_level":"YELLOW","score":0.52,"period":"2026",
 "detail":{"violations":[{"amount":500000,"type":"不征税","reason":"缺资金拨付文件"}],"ratio":0.116,"estimated_tax":125000},
 "recommendation":"¥50万财政拨款不满足不征税条件，应调增应纳税所得额。"}
```

---

### 3.4 成本费用类风险预警 (COST)

---

#### COST-12 费用占比异常

**公式**：

```
费用率 = (销售+管理+财务费用-研发) / 营业收入
行业基准: 大型(>100亿)6%-9% | 中型(10-100亿)8%-12% | 小型(<10亿)10%-15%
行业偏离度 = |费用率 - 行业中位数| / 行业标准差
历史波动率 = |当月费率 - 12月均费率| / 12月费率标准差
综合 = 0.6×min(偏离度/3, 1) + 0.4×min(波动率/3, 1)
```

**阈值**: 红>0.70 | 黄(0.45,0.70] | 绿≤0.45

**数据源**: 利润表 + 费用明细表 + 同规模对标数据

```json
{"indicator_id":"COST-12","risk_level":"RED","score":0.78,"period":"2026-06",
 "detail":{"current_ratio":0.185,"benchmark_median":0.10,"deviation":3.20,"volatility":4.87,
 "suspicious":[{"item":"咨询费","amount":3200000,"yoy":"+320%，无合同"},{"item":"利息支出","amount":14800000,"yoy":"+180%，短债余额降"}]},
 "recommendation":"费率18.5%远超中位数10%，历史波动4.87σ。重点查无合同咨询费和异常利息。"}
```

---

#### COST-13 工资薪金与社保联动异常

**公式**：

```
人数匹配度 = |个税月均人数 - 社保月均人数| / max(个税人数, 1)
基数一致性 = |(工资总额/12/人数) - (社保基数之和/人数)| / 基数范围
社保合规度 = 0.4×(按实缴费人数/总参保) + 0.3×(全员参保) + 0.3×(工伤覆盖率≥95%)
建安扣分项: 临时工>30天未参保 -0.2 | 劳务派遣与自有混同 -0.2
```

**阈值**: 红：人数匹配度>0.20 / 一致性>0.30 / 合规度<0.70 | 黄：(0.10,0.20]/(0.15,0.30]/[0.70,0.85) | 绿：≤黄区下界

**数据源**: 个税扣缴端 + 社保申报表 + 分人员工资表

```json
{"indicator_id":"COST-13","risk_level":"RED","score":0.89,"period":"2026-06",
 "detail":{"tax_headcount":320,"si_headcount":185,"mismatch":0.422,
 "avg_wage":6800,"avg_si_base":4200,"consistency":0.38,"compliance":0.52,
 "issues":["135人未参保","82人工地工伤保险未覆盖"]},
 "recommendation":"人数差42%合规度52%重大违规。立即补缴社保，评估社保入税成本。","urgency":"最高优先级"}
```

---

#### COST-14 固定资产与折旧异常

**公式**：

```
一次性扣除违规: 房屋建筑采用→违规 | 同一资产重复扣→违规 | 会计折旧未调增→违规
折旧超速比率 = 会计年限 / 税法最低年限，<0.80→违规加速
风险分 = max(一次扣除违规×0.9, max(超速率-1,0)×0.7)

建安专属: 塔吊/施工电梯税法最低10年 | 临时设施与永久设施区分 | 维修费资本化误一次扣除
```

**阈值**: 红：一次扣除违规 / 超速率<0.80 | 黄：超速率[0.80,0.90) | 绿：≥0.90

**数据源**: 固定资产台账 + 折旧明细表 + A105080

```json
{"indicator_id":"COST-14","risk_level":"YELLOW","score":0.55,"period":"2026-06",
 "detail":{"one_time":[{"asset":"活动板房","amount":450000,"status":"需核查"}],
 "depreciation":[{"asset":"塔吊","min_years":10,"actual":8,"ratio":0.80},{"asset":"施工电梯","min_years":10,"actual":6,"ratio":0.60,"status":"RED"}]},
 "recommendation":"施工电梯折旧年限6年<10年，调增差额应纳税所得额；活动板房改分期摊销。"}
```

---

#### COST-15 无票支出异常

**公式**：

```
无票成本占比 = 无合规发票的成本费用 / 营业总成本
建安阈值 = 通用阈值(2%) × 建安系数(2.5) = 5%
白票风险 = 0.3×(无票材料/5%) + 0.3×(无票人工/5%) + 0.2×(无票机械/5%) + 0.2×(白条笔数/20)
```

**阈值**: 红≥8% | 黄(5%,8%] | 绿≤5% | 白票风险: 红>0.80 / 黄(0.50,0.80] / 绿≤0.50

**替代凭证要求**: 小额零星(<¥500/次)→收款人姓名+身份证号+项目+金额收据 | 自然人代开→完税证明+代开点盖章 | 农副产品→收购发票或自产证明

**数据源**: 成本费用明细账 + 发票台账 + 白条登记簿

```json
{"indicator_id":"COST-15","risk_level":"YELLOW","score":0.68,"period":"2026-06",
 "detail":{"total_cost":215000000,"no_invoice":{"material":8200000,"labor":5500000,"equipment":1800000,"others":3000000},
 "total_ratio":0.086,"white_strip_score":0.72,"unqualified_vouchers":23},
 "recommendation":"无票占比8.6%略超红线。砂石料必取发票，包工头结算需税务代开。"}
```

---

## 4. 综合评分与输出

### 4.1 加权评分

```
综合风险分 = Σ(指标分[i] × 权重[i]) / Σ权重[i]

权重矩阵: 发票类30%(INV-01:8,02:6,03:8,04:8) | 特殊20%(SPEC-05:7,06:6,07:7)
          收入类25%(INC-08:6,09:7,10:6,11:6) | 成本费用25%(COST-12:6,13:7,14:6,15:6)

等级: 红≥70 | 黄[40,70) | 绿<40
```

### 4.2 完整输出结构

```json
{
  "report_metadata": {"report_id":"TER-2026-Q2-001","generated_at":"2026-07-02T10:30:00+08:00",
    "enterprise":"XX建工集团","tax_id":"91110000XXXXXXXXXX","period":"2026-Q2",
    "industry":"house_building","scale":"large","adjustment_coefficient":1.12,"version":"1.0.0"},
  "summary": {"total":15,"red":5,"yellow":6,"green":4,"composite_score":72.5,
    "composite_level":"RED","estimated_exposure":8450000,
    "top3":[{"id":"INV-04","name":"虚开发票","score":0.95},
            {"id":"INV-03","name":"抵扣异常","score":0.91},
            {"id":"COST-13","name":"社保异常","score":0.89}]},
  "indicators": [{  }],
  "action_plan": {
    "immediate": ["INV-04:停止交易·保全证据·咨询律师","COST-13:启动补缴·评估处罚"],
    "within_7d": ["INV-01:核实材料销售","INC-09:确认纳税义务"],
    "within_15d": ["SPEC-07:更正申报","COST-15:补齐凭证"],
    "within_30d": ["INC-08:逐项比对","COST-14:调增所得额"]
  }
}
```

---

## 5. 调用示例

### 5.1 命令行

```bash
# 全量扫描
python scripts/risk_scanner.py \
    --input ./sample_data/jianan_q2_2026.xlsx \
    --output ./reports/risk_report_2026Q2.json \
    --industry house_building --scale large --period 2026-Q2

# 定向扫描
python scripts/risk_scanner.py --input data.csv --category invoice

# 交互模式
python scripts/risk_scanner.py --input data.csv --interactive
```

### 5.2 最小输入数据 (CSV)

```csv
period,vat_sales_total,vat_simple_sales,cit_revenue,cost_total,admin_expense,selling_expense,finance_expense,salary_total,social_insurance_headcount,tax_headcount,advance_receipts_balance,advance_receipts_aged_180d,ar_balance,ar_balance_prior,bank_inflow_operating,fixed_asset_original,depreciation_accounting,depreciation_tax,one_time_deduction_amount,no_invoice_cost_material,no_invoice_cost_labor,no_invoice_cost_equipment,non_taxable_income,tax_free_income,sales_invoice_categories,purchase_invoice_categories,simple_tax_project_count,simple_tax_noncompliant_count,differential_deduction_count,differential_noncompliant_count,tax_free_revenue,tax_free_noncompliant,transfer_out_required,transfer_out_actual,related_enterprise_flag,fund_flowback_ratio,fund_flowback_days,concentration_index,top_amount_ratio,void_anomaly,red_invoice_ratio
2026-06,287000000,35,274500000,215000000,18500000,4200000,14800000,26112000,185,320,18500000,12300000,142000000,98000000,82000000,82000000,12500000,9800000,3250000,8200000,5500000,1800000,3500000,800000,建筑服务;工程勘察,黑色金属冶炼压延品;非金属矿物制品;电线电缆,8,1,35,2,8500000,0,520000,390000,1,0.97,3,0.52,0.03,1.2,0.01
```

### 5.3 运行结果摘要

| 指标 | 级别 | 得分 | 核心发现 |
|------|------|------|---------|
| INV-01 进销背离 | **红** | 0.82 | 进项钢材/矿品为主，销项建筑服务 |
| INV-02 发票异常 | 黄 | 0.55 | 月底集中开票+作废率偏高 |
| INV-03 抵扣异常 | **红** | 0.91 | 简易项目进项混抵，抵扣率高9pp |
| INV-04 虚开关联 | **红** | 0.95 | 关联方+3日97%资金回流 |
| SPEC-05 简易/差额 | 黄 | 0.65 | 清包工条款缺失+管理费误扣除 |
| SPEC-06 免税风险 | 黄 | 0.60 | 进项转出缺口¥13万 |
| SPEC-07 收入混淆 | **红** | 0.88 | 补贴误填不征税，应调增¥120万 |
| INC-08 申报差异 | 黄 | 0.62 | 两税差异¥250万 |
| INC-09 预收/应收 | **红** | 0.86 | 预收¥1230万>180天不转收入 |
| INC-10 资金背离 | 黄 | 0.58 | 流入高于申报13% |
| INC-11 收入违规 | 黄 | 0.52 | ¥50万不征税条件不满足 |
| COST-12 费用异常 | **红** | 0.78 | 费率18.5% vs 中位数10%，波动4.87σ |
| COST-13 社保联动 | **红** | 0.89 | 人数差42%+合规度52% |
| COST-14 折旧异常 | 黄 | 0.55 | 施工电梯折旧6年<税法10年 |
| COST-15 无票支出 | 黄 | 0.68 | 无票8.6%略超红线 |

> 综合风险分 **72.5 (红区)**，预估税务敞口 **¥845万**

---

## 6. Python 脚本结构

脚本实现位于 `scripts/risk_scanner.py`，模块结构：

```
risk_scanner/
├── data_loader.py        # CSV/Excel 读取与校验
├── indicators/
│   ├── invoice.py        # INV-01~04
│   ├── special.py        # SPEC-05~07
│   ├── income.py         # INC-08~11
│   └── cost.py           # COST-12~15
├── thresholds.py         # 三区阈值 + 建安系数
├── scorer.py             # 综合评分排序
├── reporter.py           # JSON/Markdown/Excel 输出
└── cli.py                # 命令行入口
```

**关键函数签名**：

```python
def calc_divergence(sales_cat: list[str], sales_amt: list[float],
                    purch_cat: list[str], purch_amt: list[float]) -> DivergenceResult: ...

def calc_advance_abnormal(balance: float, aged_180d: float,
                          progress: dict, industry: str = "construction") -> AbnormalResult: ...

def generate_report(indicators: list, info: EnterpriseInfo,
                    fmt: str = "json") -> str: ...
```

---

## 7. 法规依据

| 法规 | 相关指标 |
|------|---------|
| 《增值税暂行条例》及实施细则 | INV-01~04, SPEC-05~06 |
| 财税[2016]36号 营改增试点通知 | SPEC-05, INV-03 |
| 财税[2011]70号 专项用途财政性资金 | SPEC-07, INC-11 |
| 国家税务总局公告2018年第28号 扣除凭证 | COST-15 |
| 财税[2018]54号 设备器具扣除 | COST-14 |
| 国税发[2009]31号 房地产开发企业所得税 | INC-09 |
| 《社会保险法》+社保入税规定 | COST-13 |
| 国家税务总局公告2016年第17号 跨县建筑服务 | SPEC-05 |

---

## 8. 执行流程

```
触发词检测 → 意图解析(全量/定向/调参)
    ↓
数据接入: 识别格式→完整性校验→识别企业规模/施工类型
    ↓
系数计算: 规模×施工类型×跨省×简易占比×挂靠 → 综合调整系数
    ↓
并行扫描: 发票4项 | 特殊3项 | 收入4项 | 成本4项
    ↓
综合评分: 加权计算→红黄绿等级→预估敞口
    ↓
输出: JSON主报告 + 可选Markdown/Excel + 按紧急度排序的行动计划
```

---

## 9. FAQ

**Q: 数据不完整能否运行？** A: 缺失字段对应指标标记 `INSUFFICIENT_DATA`，综合评分仅基于可用指标。建议至少覆盖80%。

**Q: 阈值与规模的关系？** A: 小型企业(<10亿)阈值更宽松(挂靠/白条/临时工普遍)，大型(>100亿)更严格。见第2节。

**Q: 如何判断三流一致合同流？** A: 合同主体 vs 开票方 vs 收付款方三者一致性。不一致需核实挂靠/转包/授权收款等合法情形。

**Q: 与strategic-analyst协作？** A: 本技能提供定量指标，strategic-analyst 补充政策环境/竞争格局等定性分析，协同完成尽调报告。

---

> **免责声明**：本引擎仅供企业内部自查参考，不构成税务合规意见。重大事项请咨询持牌税务师/律师。阈值应结合实际稽查口径调整。

## Zcode 集成

### τ 角色与贡献

本技能在 Zcode 体系中承担 **executor** 角色，遵循 `skills/shared/zcode/zcode-embedding-standard.md` 标准。

| 指标 | 方向 | 机制 | 目标压缩 |
|------|------|------|---------|
| τ_execute | reduce | 15个预警指标的自动化扫描管线 | 20% |
| τ_qa | auto | 金税四期规则自动匹配校验 | auto |

### 质量门禁

- **等级**: enhanced
- **依据**: `skills/shared/skill-quality-gate.md`
- **执行前**: 输入校验 + 反模式预检（`skills/shared/feedback/anti-patterns.yaml`）
- **执行后**: 输出校验 + 交付判定（三阶段门禁）

### 交叉验证

- **协同技能**: contract-risk-scanner, financial-bp-command-center
- **校验协议**: `skills/shared/zcode/zcode-embedding-standard.md` 第 4 节

### 反馈闭环

- **输出触发**: Memory 写入 + τ 快照更新 + 反模式比对（如适用）
- **遵循协议**: `skills/shared/feedback/feedback-loop-protocol.md`

---
*Zcode 嵌入版本: 1.0 | © 版权所有：默笙夏夏の知書房 - 2026-07-09*
