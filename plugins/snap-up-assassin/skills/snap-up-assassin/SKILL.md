---
name: snap-up-assassin
description: >
  浏览器自动化抢购系统 v4.1 — Zcode优化版。双通道并行 + 时钟校准+RTT测量 + 拟人化MouseEvent点击 +
  阶段自适应循环(5ms→30ms) + 五层守护。覆盖自动抢购全流程。
version: 2.1.0
agent_created: true
qualityGate: enhanced
category: 工程规范
trigger_recommended:
  - 抢购
  - 抢单
  - snap-up
  - 秒杀
  - 帮我抢
trigger_exclusive:
  - GLM.*抢
  - 套餐.*抢
  - 抢购.*优化
dependencies:
  - first-principles-reasoning
  - spa-engineering-guard
supersedes: null
zcode:
  version: "1.0"
  τ_role: executor
  τ_impact:
    - metric: τ_execute
      direction: reduce
      target: 50%
      mechanism: 双通道并行 + 5ms级周期自适应轮询
    - metric: τ_qa
      direction: auto
      target: auto
      mechanism: 五层守护自动容错
  bus_compatible: true
  cross_validate_with:
    - agent-browser
summary: 浏览器自动化抢购系统 v4.1 — Zcode优化：双通道+校准+拟人化+自适应循环
disable: false
assets:
  - snap_up.py (Zcode优化版主文件, 1729行, 45函数/36async)
  - config.json (简洁配置文件)
  - selectors.json (按钮探测输出)
  - calibration.json (时钟校准+RTT数据)
---
# Snap-Up Assassin v4 — 多Tab并行抢购系统

## 版本演进

| 版本 | 日期 | 核心变化 |
|------|------|----------|
| v1 | 06-29 | 基础Playwright自动化 |
| v2 | 06-30 | SPA适配 + JS evaluate点击 |
| v3 | 07-02 | 五层守护 + 三层点击 + 自适应循环 |
| **v4** | **07-07** | **多Tab并行 + NTP校准 + 分层恢复 + 资源拦截** |

## v4 架构概览

```
┌─────────────────────────────────────────────────────────┐
│  Timing Controller (NTP校准 + busy-wait)                 │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐        │
│  │Tab #1│ │Tab #2│ │Tab #3│ │Tab #4│ │Tab #5│        │
│  │click │ │click │ │click │ │click │ │click │        │
│  └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘        │
│     │       │       │       │       │                  │
│     └───────┴───────┴───────┴───────┘                  │
│                      │                                  │
│              Result Aggregator                          │
│           (首成功 → STOP ALL)                           │
└─────────────────────────────────────────────────────────┘
```

## v4 五大核心升级

### 1. 多Tab并行引擎 (`TabPoolManager`)

- 配置 `tab_count` (默认5) 个独立Tab并行抢购
- 共享BrowserContext = 共享cookies/登录态
- 首成功即全局停止（`GlobalState.signal_success()`）
- 异步创建+预热，失败Tab不影响其他Tab

### 2. NTP式时钟校准 (`ClockCalibrator`)

- HTTP HEAD请求提取 `Date` 响应头 → 计算本地偏移
- 中位数过滤极端值，多服务器冗余
- `server_time_ms()` 返回校准后的服务器毫秒戳

### 3. 精准定时触发

- T-45s: 创建并预热所有Tab
- T-150ms: 进入busy-wait（50μs精度）
- T-20ms: 纯CPU循环零sleep

### 4. 网络优化层 (`NetworkOptimizer`)

- DNS预热（`socket.getaddrinfo`）
- 资源拦截（`context.route` 拦截 image/font/media等）

### 5. 分层恢复机制 (`RecoveryManager`)

| 层级 | 操作 | 触发条件 |
|------|------|----------|
| L1 | JS点击重试 | 默认15ms间隔, 300次/循环 |
| L2 | 刷新页面 | 连续25次失败 |
| L3 | 关闭重开 | L2失败 |
| L4 | 标记退出 | L3失败 |

## 部署清单

### 前置条件
```bash
pip install playwright aiohttp && playwright install chromium
```

### 每日操作流程 (v4)
```
08:50  pkill -f "Google Chrome"
	09:00  python snap_up.py --warmup   # 扫码登录 + 自动探测按钮
	09:05  验证 selectors.json 完整性
	09:55  python snap_up.py --auto     # 多Tab并行抢购 (5个Tab)
10:00  NTP校准 → busy-wait → 并行触发 → 首成功即停
```

### v4 配置关键参数 (`config.json`)

```json
{
  "tab_count": 5,              // 并行Tab数 (1-8)
  "fast_loop_interval_ms": 15, // Tab内点击间隔 (10-30ms)
  "busy_wait_ms": 150,         // 最后精确等待窗口
  "block_resources": true,     // 拦截图片/字体/媒体资源
  "retry_backoff_base": 1.5,   // 指数退避基数
  "retry_jitter": true,        // 抖动防惊群
  "start_early_seconds": 45    // 提前启动预热
}
```

## v3 保留的实战教训

以下经验已沉淀为 v4 中的JS点击代码和Tab恢复逻辑：

1. **Vue SPA 渲染延迟** → `domcontentloaded` + `wait_for_function` 而非 `networkidle`
2. **el-tooltip 焦点陷阱** → JS evaluate 直接点击，绕过焦点管理
3. **服务器限流锁按钮** → 多Tab并行确保至少一个Tab命中
4. **Chrome profile 锁** → 启动前 pkill
5. **点击间隔不可过大** → 15ms v4 默认值（v3 为30ms）

## 适配新目标页

修改 `config.json` 中 `target_url`，然后运行 `--warmup` 自动探测按钮。生成的 JS 点击代码会保存到 `selectors.json`。

## Zcode 集成

### τ 角色与贡献

本技能在 Zcode 体系中承担 **executor** 角色，遵循 `skills/shared/zcode/zcode-embedding-standard.md` 标准。

| 指标 | 方向 | 机制 | 目标压缩 |
|------|------|------|---------|
| τ_execute | reduce | 双通道并行 + 5ms级周期自适应轮询 | 50% |
| τ_qa | auto | 五层守护自动容错 | auto |

### 质量门禁

- **等级**: enhanced
- **依据**: `skills/shared/skill-quality-gate.md`
- **执行前**: 输入校验 + 反模式预检（`skills/shared/feedback/anti-patterns.yaml`）
- **执行后**: 输出校验 + 交付判定（三阶段门禁）

### 交叉验证

- **协同技能**: agent-browser
- **校验协议**: `skills/shared/zcode/zcode-embedding-standard.md` 第 4 节

### 反馈闭环

- **输出触发**: Memory 写入 + τ 快照更新 + 反模式比对（如适用）
- **遵循协议**: `skills/shared/feedback/feedback-loop-protocol.md`

---
*Zcode 嵌入版本: 1.0 | © 版权所有：默笙夏夏の知書房 - 2026-07-09*
