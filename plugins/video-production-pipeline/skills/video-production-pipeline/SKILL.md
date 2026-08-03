---
name: video-production-pipeline
description: >
  Remotion-based declarative video production pipeline with 认识→模仿→创新→超越
  methodology. Covers reference video reverse-engineering, React component-based
  pipeline, cover design engine, intelligent BGM, multi-resolution output
  matrix, spring animation DSL, and 小红书-ready formatting.
  视频全流程生产线——四阶段方法论驱动：认识(逆向工程)→模仿(能力复刻)→创新(差异化突破)→超越(建立范式)。
version: 4.0.0
agent_created: true
qualityGate: enhanced
trigger_recommended:
  - 生成视频
  - 视频制作
  - 参考视频分析
  - 视频逆向工程
  - 添加背景音乐
  - 封面设计
  - 配乐
  - 替换图片
  - 视频质检
  - build video
  - create video
  - add bgm
  - Remotion
  - redign cover
  - analyze video
  - reverse engineer
trigger_exclusive:
  - 视频全流程生产
  - 小红书视频
  - 视频方法论
anti_triggers:
  - 音频转录
  - 语音转文字
  - 股票分析
dependencies:
  - remotion-video (project template at remotion-video/)
  - 视频制作方法论体系_认识模仿创新超越.md (methodology framework)
supersedes:
  - video-production-method
zcode:
  version: "1.0"
  τ_role: executor
  τ_impact:
    - metric: τ_execute
      direction: reduce
      target: 35%
      mechanism: Remotion组件模板 + 批量渲染管线
    - metric: τ_qa
      direction: auto
      target: auto
      mechanism: 自动内容合规检查清单
  bus_compatible: true
  cross_validate_with:
    - multimodal-bridge
    - picture-book-pipeline
disable: true
last_updated: 2026-07-05
---

# Video Production Pipeline v4.0

> **核心升级**：集成「认识→模仿→创新→超越」四阶段方法论，每次视频项目从逆向工程参考视频开始。

## 四阶段总览

```
认识(Analyze) → 模仿(Replicate) → 创新(Innovate) → 超越(Transcend)
    │                │                │                │
解构参考视频      1:1能力复刻      差异化突破        建立新范式
建立技术画像      掌握核心技法      注入个人风格      引领制作标准
```

**铁律**：任何新视频项目启动，必须先执行 Stage -1（认识阶段），完成参考视频分析后方可进入制作。

## When to Use

This skill is triggered when the user requests:
- "分析参考视频" / "analyze video" / "reverse engineer video" — **Stage -1**: 参考视频逆向工程
- "生成视频" / "build video" / "create video" — full pipeline (Remotion primary)
- "Remotion 视频" / "声明式视频" — Remotion-based rendering
- "模仿这个视频" / "参考这个视频制作" — **Stage -1 + Stage 0-6**: 完整四阶段流程
- "修复视频" / "fix video rendering" — targeted fix
- "添加背景音乐" / "add bgm" / "配乐" — BGM only
- "封面设计" / "redesign cover" / "cover page" — cover only
- "替换图片" / "replace images" — frame replacement
- "质检" / "quality check" / "test video" — QA only
- "对比视频" / "compare videos" — reference-based optimization
- "多分辨率渲染" / "multi format" — 3-format output matrix

---

## Stage -1: 认识 — 参考视频逆向工程（v4.0 新增，必须先执行）

### 目的

在开始任何制作之前，对参考视频进行全面技术解构，建立可量化的模仿基准。

### 自动化技术分析脚本

```bash
# 一键分析参考视频
analyze_reference() {
  local VIDEO="$1"
  echo "=== 参考视频技术画像 ==="
  echo ""

  # 1. 基础参数
  echo "## 基础参数"
  ffprobe -v quiet -print_format json -show_format -show_streams "$VIDEO" | \
    python3 -c "
import json, sys
d = json.load(sys.stdin)
fmt = d['format']
for s in d['streams']:
    if s['codec_type'] == 'video':
        print(f'分辨率: {s[\"width\"]}×{s[\"height\"]} ({s[\"display_aspect_ratio\"]})')
        print(f'帧率: {s[\"r_frame_rate\"]}')
        print(f'编码: {s[\"codec_name\"]} {s.get(\"profile\",\"\")} {s.get(\"pix_fmt\",\"\")}')
        print(f'时长: {float(s[\"duration\"]):.1f}秒')
        print(f'视频码率: {int(s.get(\"bit_rate\",0))/1000:.0f}kbps')
    if s['codec_type'] == 'audio':
        print(f'音频: {s[\"codec_name\"]} {s[\"sample_rate\"]}Hz {s[\"channels\"]}ch {int(s.get(\"bit_rate\",0))/1000:.0f}kbps')
print(f'文件体积: {int(fmt[\"size\"])/1024/1024:.1f}MB')
print(f'编码器: {fmt[\"tags\"].get(\"encoder\",\"unknown\")}')
"
  echo ""

  # 2. 音频电平分析
  echo "## 音频电平"
  ffmpeg -i "$VIDEO" -af "volumedetect" -f null /dev/null 2>&1 | \
    grep -E "mean_volume|max_volume" | sed 's/.*mean_volume/  均值/' | sed 's/.*max_volume/  峰值/'
  echo ""

  # 3. GOP结构
  echo "## GOP结构"
  ffprobe -v quiet -show_entries frame=pict_type -of csv "$VIDEO" 2>/dev/null | sort | uniq -c | \
    sed 's/I/  I帧(关键帧)/' | sed 's/P/  P帧(预测帧)/' | sed 's/B/  B帧(双向帧)/' | sed 's/,//g'
  echo ""

  # 4. 场景切换检测
  echo "## 场景切换时间点"
  ffmpeg -i "$VIDEO" -vf "select='gt(scene,0.3)',showinfo" -f null - 2>&1 | \
    grep "pts_time:" | sed 's/.*pts_time:/  /' | sed 's/ .*//' | \
    awk '{printf "  %s%.1fs\n", ($1>0 ? "├─ " : ""), $1}'
  echo ""

  # 5. 响度标准化分析
  echo "## EBU R128 响度"
  ffmpeg -i "$VIDEO" -af "loudnorm=I=-23:LRA=7:TP=-1:print_format=json" -f null /dev/null 2>&1 | \
    grep -E '"input_|"target_|"norm_' | sed 's/[",]//g' | sed 's/^/  /'
}

# 使用
analyze_reference "path/to/reference.mp4"
```

### 参考视频认识记录模板

分析完成后，必须填写以下模板：

```markdown
## 参考视频认识记录：[视频名称/标识]

### 技术画像

| 维度 | 参数 | 对标评估 |
|------|------|:------:|
| 分辨率 | {w}×{h} ({aspect}) | ★★★★★ |
| 帧率 | {fps}fps | — |
| 时长 | {duration}秒 | — |
| 编码效率 | {I/P/B帧分布} | — |
| 音频电平 | 均值{dB}，峰值{dB} | — |
| 场景切换 | {count}次，平均间隔{avg}s | — |
| 文件体积 | {size}MB | — |

### 可借鉴点（按优先级排序）

1. **[最优先模仿]** — 具体描述 + 为什么重要
2. **[次要参考]** — 具体描述
3. **[可选参考]** — 具体描述

### 需规避的不足

- 具体问题描述

### 模仿达标矩阵

| 维度 | 参考基准 | 目标值 | 达标条件 |
|------|---------|--------|---------|
| 音频 | -25.9dB均值 | -26~-20dB | volumedetect 验证 |
| 视觉 | 720p 30fps | ≥1080p 30fps | ffprobe 验证 |
| 编码 | B+P混合 | B+P混合 | GOP结构检查 |
| 节奏 | 8-15s/场景 | 同类内容对标 | 场景切换时间 |
```

### 模仿阶段硬性达标指标

| 指标 | 红线 | 理想值 | 检查方法 |
|------|:----:|:------:|---------|
| 分辨率 | ≥720p | 1080p (1920×1080 或 1080×1080) | ffprobe |
| 帧率 | 25-30fps | 30fps | ffprobe |
| 音频码率 | ≥96kbps | 128-192kbps AAC | ffprobe |
| 音频均值 | -30~-16dB | -26~-20dB | volumedetect |
| 音频峰值 | ≤0dB | ≤-3dB | volumedetect |
| I帧间隔 | ≤10秒 | 5-8秒 | frame=pict_type |
| 无黑场 | 亮度>10 | 亮度>20 | 帧采样 |
| 无花屏 | 无损坏帧 | 无损坏帧 | 逐帧扫描 |

---

## ⚡ Pipeline Selection Matrix

| Scenario | Pipeline | Tool |
|----------|----------|------|
| 先分析参考视频 | **Stage -1 必执行** | `analyze_reference()` |
| 新项目、需要动画和灵感 | **Remotion (推荐)** | `remotion-video/` 项目模板 |
| 已有大量 Python 素材、快速出片 | FFmpeg (传统) | Python `build_video.py` |
| 需要 Studio 实时预览 | **Remotion** | `npm start` |
| 需要逐帧精确控制转场 | **Remotion** | Spring + Interpolate |
| 已有完整 BGM/音频 | 两种均可 | — |

---

## 🎯 创新维度矩阵（Stage +2：创新阶段）

### 创新方向与难度评估

| 创新维度 | 参考基准（模仿阶段） | 创新方向 | 难度 | 实现方式 |
|----------|-------------------|---------|:--:|---------|
| **配音** | 单一AI TTS | 多角色配音 + 情感标注 + 音效点缀 | ★★★ | TTS角色库 + 音效资产 |
| **文案** | 线性叙事 | 悬念前置 + 反转 + 互动式提问 | ★★★ | 脚本模板库 |
| **画面** | 静态图+文字 | 声明式动画（Remotion Spring） | ★★★★ | useAnimations Hooks |
| **转场** | 简单切/淡入淡出 | 亮度自适应溶解 + 动态蒙版 | ★★★★ | brightness.ts + interpolate |
| **配乐** | 固定音量BGM | 自动Ducking（旁白时BGM降至30%） | ★★★ | useAutoDucking Hook |
| **字幕** | 底部居中 | 动态高亮 + 关键词弹出 | ★★★ | React组件动画 |
| **格式** | 单分辨率 | 三格式矩阵（1:1/16:9/9:16） | ★★★★ | render-all.ts |
| **交互** | 纯单向 | 章节标记 + 快速跳转 | ★★ | ChapterMarkers组件 |

### 创新自检清单（每个视频完成后必答）

1. 这个视频与我模仿的参考视频有何不同？（至少3点）
2. 观众看完后会记住哪个独特元素？
3. 技术上使用了哪些参考视频没有的能力？
4. 如果只保留一个创新点，哪个最有价值？
5. 这个创新是否可以复用到下一个视频？

---

## 🏆 超越评判标准（Stage +3：超越阶段）

### 超越的六个标志

- [ ] 产出视频的**所有技术指标**不低于参考视频
- [ ] 形成**3-5个标志性视觉/听觉元素**，观众一眼认出
- [ ] 制作流程**全自动化**（素材→成片 ≤10分钟人工介入）
- [ ] 建立**个人视频资产库**（封面模板、转场预设、BGM库、配音角色库）
- [ ] 方法论**可传授**（有文档、有模板、有案例）
- [ ] 范式可**跨项目迁移**（非一次性作品）

### 超越公式

```
范式 = 独特风格 × 技术壁垒 × 效率优势 × 可复制性
```

---

## 🚦 四道质量门禁（发布前强制通过）

```
素材准备 → [门禁1: 版权检查] → 制作完成 → [门禁2: 技术质检]
    → 人工审阅 → [门禁3: 内容审阅] → [门禁4: 平台合规] → 发布
```

### 门禁1：版权检查
- [ ] 图片来源（AI生成/自有/已授权）
- [ ] BGM为CC0或自有
- [ ] 字体为系统字体或开源字体
- [ ] 无第三方品牌Logo

### 门禁2：技术质检
- [ ] 分辨率 ≥1080p，帧率 30fps
- [ ] 无黑场/花屏/破损帧
- [ ] 音频均值 -26~-20dB，峰值 ≤-3dB
- [ ] 音频码率 ≥128kbps，采样率 ≥44.1kHz
- [ ] 像素格式 yuv420p，无长时间静音(>3s)
- [ ] 文件可正常播放

### 门禁3：内容审阅
- [ ] Hook有吸引力，逻辑结构完整
- [ ] 信息密度适中（2-5信息点/分钟）
- [ ] 情绪曲线有起伏
- [ ] CTA明确，无常识性错误

### 门禁4：平台合规（小红书专项）
- [ ] 无敏感话题，无不适用语
- [ ] 时长 1-5分钟
- [ ] AI使用诚实说明

---

## 🚀 Remotion Pipeline (v3.0 新增，推荐)

### 项目结构

```
remotion-video/
├── src/
│   ├── index.ts              # registerRoot 入口
│   ├── Root.tsx              # Composition 注册 (3种分辨率)
│   ├── data/qaData.ts        # 30组问答数据
│   ├── compositions/
│   │   ├── MainVideo.tsx     # 完整视频主组件
│   │   ├── CoverOnly.tsx     # 封面独立预览
│   │   └── QASingle.tsx      # 单页Q&A预览
│   ├── components/
│   │   ├── Cover.tsx         # 封面组件 (Spring动画)
│   │   ├── QAFrame.tsx       # Q&A帧组件 (自适应布局)
│   │   ├── StaticPage.tsx    # 静态页面 (Intro/Ending/Credits)
│   │   └── AudioTrack.tsx    # 多轨音频管理器 (Ducking)
│   ├── hooks/
│   │   ├── useAnimations.ts  # 8个动画Hook预设库
│   │   └── useAutoDucking.ts # BGM自动Ducking
│   └── utils/
│       ├── pageMap.ts        # 页码映射
│       └── brightness.ts     # 亮度自适应溶解
├── scripts/
│   └── render-all.ts         # 多分辨率一键渲染
└── public/
    ├── images/               # 页面图片
    └── audio/                # 旁白 + BGM
```

### 快速命令

```bash
cd remotion-video/
npm install                # 安装依赖
npm start                  # 启动 Remotion Studio (实时预览)
npm run build              # 渲染 1080×1080
npm run render             # 三格式一键渲染
npm run render:square      # 仅 小红书 1:1
npm run render:landscape   # 仅 B站 16:9
npm run render:portrait    # 仅 抖音 9:16
```

### Remotion 管线各阶段

```
0. Cover → <Cover /> React组件 + Spring入场动画
1. Frame  → <QAFrame /> React组件 + CSS排版 + 自适应缩放
2. ~~YUV~~ → 消除 (Remotion Headless Browser 直接渲染)
3. Encode → renderMedia() h264 AAC 并发7x
4. Audio  → <Sequence><Audio/> 帧精确同步
5. BGM    → 多<Audio/>轨 + volume(f)=> 自动Ducking
6. Mux    → Remotion 内部一步完成
```

### 创新功能 (超越 FFmpeg)

| 创新点 | 实现 | FFmpeg 管线无法做到 |
|--------|------|-------------------|
| **声明式动画DSL** | `useFadeIn()`, `useSlideUp()`, `useTypewriter()` 等8个Hook | ❌ |
| **5种预设动画曲线** | gentle/smooth/bouncy/snappy/slow | ❌ |
| **BGM自动Ducking** | 旁白时BGM自动降至30%音量 | ⚠️ 需手动 ffmpeg filter |
| **亮度自适应溶解** | delta>120→24帧, >80→18帧, else→14帧 | ⚠️ 需 Python 预计算 |
| **Remotion Studio** | 时间轴拖拽预览 + 逐帧审阅 | ❌ |
| **组件化复用** | Cover/QAFrame/AudioTrack 跨项目复用 | ❌ |
| **多分辨率矩阵** | 一种代码 → 1080² / 1920×1080 / 1080×1920 | ❌ 需分别渲染 |
| **Git友好** | 视频工程 = 纯文本 React 代码 | ❌ |
| **零中间文件** | Headless Browser 直接渲染 | ❌ YUV 需2GB暂存 |

---

## 📐 FFmpeg Pipeline (传统，保留)

---

## ⚠️ 强制规则：生成后自动测试 + 合规检查（每次执行，无例外）

视频生成完毕后，**必须**依次执行：

1. `open <视频文件路径>` — 自动打开视频供用户审阅
2. 执行下方「小红书合规检查清单」逐项自检
3. 如任一项不通过，标记问题并修复后重新生成

---

## 小红书平台合规检查清单（Stage 7）

### 内容合规

| 检查项 | 红线 | 检查方法 |
|--------|------|---------|
| 敏感话题 | 禁止政治、宗教极端、社会敏感、未核实传闻 | 逐帧文案审阅 |
| 不当用语 | 禁止低俗、歧视性、攻击性词汇 | 全文正则扫描 |
| 医疗健康 | 禁止未认证的医疗建议、疗效承诺 | 关键词过滤 |
| 金融理财 | 禁止投资建议、收益承诺 | 关键词过滤 |
| 未成年保护 | 禁止未成年人危险行为展示 | 逐帧画面审阅 |

### 素材合规

| 检查项 | 红线 | 检查方法 |
|--------|------|---------|
| BGM 版权 | 禁止使用未授权商业音乐 | 确认来源为 CC0/免费授权/自有 |
| 字体版权 | 禁止使用未授权商业字体 | 确认使用系统字体或开源字体 |
| 图片版权 | 禁止使用他人版权图片 | 确认全部为自有生成 |
| 品牌 Logo | 禁止未经授权展示第三方商标 | 逐帧画面检查 |

### 技术合规

| 检查项 | 标准 | 检查方法 |
|--------|------|---------|
| 分辨率 | ≥720p，推荐 1080p | ffprobe 验证 |
| 时长 | 图文翻页视频建议 1-5 分钟 | ffprobe 验证 |
| 文件大小 | 手机端上传 ≤ 4GB | ls 验证 |
| 画面完整 | 无黑场、无花屏、无破损帧 | 间隔采样检查 |
| 音频连续 | 无爆破音、无长时间静音 | 波形检查 |

### AI 内容声明

| 检查项 | 标准 |
|--------|------|
| 封面/视频内 AI 标识 | 不强制标注「AI 生成」，但避免误导性表述 |
| 发布文案描述 | 诚实说明人机协作方式，不虚假宣称手绘 |

### 合规评分卡

```
小红书合规检查: [通过/不通过]
  ├─ 内容合规: ✓/✗
  ├─ 素材合规: ✓/✗
  ├─ 技术合规: ✓/✗
  ├─ AI声明: ✓/✗
  └─ 综合判定: ✓/✗
```

**不通过 → 停止发布，修复后重检。**

---

## Pipeline Overview (6 stages + optional Cover Engine)

```
0. Cover Design     → Build 小红书-quality cover with calligraphy typography
1. Frame Assembly   → Build Q&A pages with text overlays from images + data
2. YUV Stream       → Write all frames into a single raw YUV stream (AVOID concat!)
3. Video Encode     → Encode YUV → H.264 with x264 -preset fast -crf 20
4. Audio Concat     → Concatenate per-page MP3 narrations into one file
5. BGM Mixing       → Mix background music at calibrated volume (use weights=1 x)
6. Final Mux        → Mux video + audio into final MP4
```

---

## Stage 0: Cover Design Engine (小红书 1080×1080 Standard)

### Golden Reference Geometry

After 28 iterations, these are the **battle-tested** exact values:

```python
CANVAS = (1080, 1080)
CX = 540  # horizontal center
CY_CIRCLE = 315  # circle center Y
R_INNER = 221   # inner circle radius (⭐ verified against reference)
R_OUTER = 311   # outer circle radius (⭐ verified against reference)

# Circle spans:
# Inner: Y=94 to Y=536 (442px)
# Outer: Y=4 to Y=626 (622px)
```

### Font Specifications

```python
# Title font: Ma Shan Zheng (马山正) — Chinese calligraphy
# Download from: cdn.jsdelivr.net/gh/google/fonts@main/ofl/mashanzheng/MaShanZheng-Regular.ttf
font_title  = ImageFont.truetype('/tmp/ma.ttf', 100)   # "慧安师傅" — WHITE #FFFFFF
font_sub    = ImageFont.truetype('/tmp/ma.ttf', 46)    # "金刚经问答" — GOLD #c4a96a
font_tag    = ImageFont.truetype('/tmp/ma.ttf', 40)    # tagline — DIM GOLD #9a8362
font_credit = Songti 20px                              # credits — rgba(150,135,120,85)
```

### Cover Layout (Precise Positions)

```
Y=79  → "慧"  (title char 1, 100px)
Y=203 → "安"  (title char 2, 100px, gap=24px)
Y=327 → "师"  (title char 3)
Y=451 → "傅"  (title char 4)
         ⬇ inner circle bottom (Y=536)
         ⬇ outer circle bottom (Y=626)
Y=656 → "金刚经问答" (46px gold, OUTSIDE outer circle +30px)
Y=716 → "三十把打开心窗的小钥匙" (40px dim gold, NO dividing line!)
Y=772 → "改编自《金刚般若波罗蜜经》" (20px muted)
Y=798 → "慧安师父与小和尚的对话"
Y=830 → "#佛学智慧 #治愈系 #心灵成长 #冥想入门" (55% alpha)
```

### Cover Construction Rule

**DO NOT add**: top/bottom border lines, dot decorations, extra horizontal lines, or any element beyond the two concentric circles. Pure zen minimalism = higher visual quality.

**DO add**: Only the dual circles + typography + credits + hashtags.

### Background Color

```python
background = '#1B1612'  # Deep zen near-black (RGB ~27, 22, 18)
```

---

## Stage 1: Frame Assembly

### Data Source

Q&A text MUST come from the original web page's `qaData` JavaScript array. Each entry: `{id, q, a, s, kw}` where `s` is the UNIQUE sutra reference per page.

**NEVER** use "金刚般若波罗蜜经" for all pages — each page has a unique `s` field.

### Page Mapping

```
Q&A 1→30 → video pages [4,5,6,7,9,10,11,12,13,14,16,17,18,19,20,21,22,23,25,26,27,28,30,31,32,33,34,35,36,38]
Full pages: [1,2,4-7,9-14,16-23,25-28,30-36,38-41]  (35 total)
Non-Q&A: [1,2,39,40,41] (cover, intro, ending, credits)
```

### Content Frame Layout

```python
frame = Image.new('RGB', (1080, 1080), '#1a1510')
# Image zone: top 58%
# Text zone: bottom 42%

# "问" label: 42px Songti, #a68b5b
# Q text: 22px Songti, #d4c9b8, width=22 chars
# 160px short gold separator
# "慧安师父" label: 38px Songti, #c4a96a
# A text: 24px Songti, #f0e8d8, width=22 chars
# Sutra ref: 17px Songti, RIGHT-ALIGNED, format "—— {s}"
```

### Critical Font Rule

```python
# ALWAYS use index=0 for .ttc fonts:
ImageFont.truetype('/System/Library/Fonts/Supplemental/Songti.ttc', size, index=0)
# NEVER omit index= for PingFang.ttc — text will be invisible
```

---

## Stage 2: YUV Stream

**CRITICAL**: Single stream ONLY. Never concat video segments.

```python
with open('all.yuv', 'wb') as yf:
    for each page:
        for each frame (duration * fps):
            yf.write(frame.tobytes())
```

### Adaptive Dissolve

```python
delta = abs(brightness_current - brightness_next)
FADE = 24 if delta > 120 else 18 if delta > 80 else 14
# Use smoothstep: t*t*(3-2*t) for alpha interpolation
```

### Zoom Policy

- Illustration pages: zoom = 1.0 (NO zoom, prevents jitter)
- Text-heavy pages: zoom = 1.001 (0.1%, subtle motion)
- Cover/intro/ending: zoom = 1.0 (static)

---

## Stage 3: Video Encode

```bash
ffmpeg -y -f rawvideo -vcodec rawvideo \
  -s 1080x1080 -pix_fmt rgb24 -r 25 -i all.yuv \
  -c:v libx264 -preset fast -crf 20 -pix_fmt yuv420p \
  -an -vsync passthrough video.mp4
```

Expected output: ~23MB for 526s @ 1080p.

---

## Stage 4: Audio Concat

```bash
for pn in sorted_pages: echo "file page_NN.mp3" >> list.txt
ffmpeg -f concat -safe 0 -i list.txt -c:a libmp3lame -b:a 128k audio.mp3
```

---

## Stage 5: BGM Intelligence

### Source Priority (ranked by success rate)

| # | Source | Success Rate | Approach |
|---|--------|:-----------:|----------|
| 1 | User-provided reference video | 100% | Direct `-vn -c:a libmp3lame` extraction |
| 2 | Pre-downloaded track | 100% | Trim to duration, loop if needed |
| 3 | foyinwang.com | 60% | agent-browser → find audio.src |
| 4 | yueting.net / fjdh.org.cn | 40% | agent-browser → extract CDN URL |
| 5 | Pixabay | 20% | CDN URL patterns unreliable |
| 6 | Generated ambient (last resort) | 10% | Solfeggio drone — usually too quiet |

### BGM Handling by Source Type

```python
# Case A: Reference video with environmental audio (water, birds)
bgm = extract_audio(reference_video)  # -vn -c:a libmp3lame
bgm_loop = concat_loop(bgm, target_duration // bgm_duration + 1)
mix_volume = 0.13  # 13% for environmental

# Case B: Downloaded pure music track (清净法身佛)
bgm = pre_downloaded_file
bgm_trim = trim(bgm, 0, target_duration)  # trim if longer, no loop needed
mix_volume = 0.12  # 12% for Buddhist music

# Case C: Generated ambient (ONLY if nothing else works)
bgm = generate_solfeggio(174, 285, 396, 432)  # frequencies
mix_volume = 0.25  # needs higher volume — likely still too quiet
# ⚠️ This approach succeeded 0/3 times in testing
```

### FFmpeg Mix Command (weights=1 x format)

```bash
# Mix BGM at x% volume with narrator
ffmpeg -y -i narrator.mp3 -i bgm.mp3 \
  -filter_complex "[0:a][1:a]amix=inputs=2:duration=first:dropout_transition=2:weights=1 x[out]" \
  -map "[out]" -c:a libmp3lame -b:a 192k mixed.mp3
```

Where `x` = BGM volume fraction (0.12 = 12%).

### BGM Download Strategies

**foyinwang.com pattern:**
```python
agent-browser open "https://foyinwang.com/dance/play-XXXX.html"
url = agent-browser eval("document.querySelector('audio')?.src || document.querySelector('source')?.src")
curl -sL -o bgm.mp3 "{url}"
```

**Reference video extraction (best approach):**
```bash
# Extract directly — cleanest audio
ffmpeg -y -i reference.mp4 -vn -c:a libmp3lame -b:a 128k bgm.mp3
```

### Volume Calibration Reference

| BGM Type | mean_volume | Recommended mix |
|----------|:-----------:|:---------------:|
| Temple ambient (参考视频环境音) | -25 dB | 14% |
| Buddhist music (清净法身佛) | -18 dB | 12% |
| Rich ambient (39 reference) | -17.6 dB | 12% |
| Generated drone | -53 dB | ❌ Skip |

---

## Stage 6: Quality Testing

### Quick QA Checklist (4 items, 30 seconds)

```python
# 1. All frames exist at correct size
for pn in all_pages:
    assert os.path.exists(f'page_{n}.png')
    assert Image.open(f).size == (1080, 1080)

# 2. No AI watermarks
import pytesseract
txt = pytesseract.image_to_string(frame, lang='chi_sim+eng')
assert 'AI' not in txt and '生成' not in txt

# 3. Audio-video sync
assert abs(total_audio_dur - video_dur) < 1.0

# 4. Render quality (9 timepoints)
for t in linspace(0, video_dur, 9):
    frame_brightness = extract_frame_at(t).mean()
    assert 10 < frame_brightness < 250  # not black/white
```

---

## 🎵 音频制作标准（v4.0 新增）

### 配音质量分级

| 等级 | 描述 | 技术指标 |
|:----:|------|---------|
| S | 专业真人配音 | 多角色、情感丰富、呼吸自然 |
| A | 高级TTS+后期 | 语速2-4字/秒、情感标注、降噪 |
| B | 标准TTS | 语速恒定、无情感变化 |
| C | 基础TTS | 仅测试用 |

### 配音后期处理流水线

```
原始音频 → 降噪 → 均衡(EQ) → 压缩(Compressor) → 限幅(≤-3dB)
    → 归一化(-23 LUFS) → 淡入淡出(10-50ms) → 输出
```

### 音频质量标准

| 指标 | 标准 | 检查方法 |
|------|------|---------|
| 采样率 | ≥44.1kHz | ffprobe |
| 位深 | ≥16bit | ffprobe |
| 平均响度 | -23 LUFS (±2 LU) | loudnorm |
| 真实峰值 | ≤-1 dBTP | loudnorm |
| 底噪 | ≤-60dB | 静音段分析 |
| 爆破音/削波 | 无 | 波形检视 |

---

## 🎨 视觉呈现标准（v4.0 新增）

### 画面质量分级

| 等级 | 分辨率 | 帧率 | 编码 |
|:----:|--------|:----:|------|
| S | 4K | 30/60fps | H.265 10bit |
| A | 1080p | 30fps | H.264 High |
| B | 720p | 25-30fps | H.264 Main |

### 色彩规范

```
主色调：1-2种（占画面60-70%）
辅助色：1-2种（占画面20-30%）
点缀色：1种（占画面5-10%，强调用）

色温选择：
- 暖色调 (3200K-4500K)：温情、治愈、人文
- 中性调 (4500K-5500K)：专业、科技、教育
- 冷色调 (5500K-7500K)：冷静、深邃、禅意
```

### 字体规范

| 用途 | 推荐字体 | 最小字号@1080p |
|------|---------|:------------:|
| 封面标题 | 马山正/站酷文艺体 | 72px |
| 封面副标题 | 马山正/思源宋体 | 36px |
| 正文 | 思源宋体/宋体 | 22px |
| 字幕 | PingFang SC/思源黑体 | 28px |
| 注释/引用 | 宋体/KaiTi | 17px |

**铁律**：禁止使用未授权商业字体。

---

## 📐 叙事结构模板（v4.0 新增）

### 短内容（<3分钟）—— 三段式

```
Hook (5-10秒) → 主体 (70-80%) → CTA (5-10秒)
    │               │                │
  制造悬念       信息传递          引导行动
```

### 中等内容（3-10分钟）—— 五段式

```
Hook → 引入 → 展开① → 展开② → 高潮 → 收尾+CTA
 5%     10%     25%      25%     25%     10%
```

### 信息密度标准

| 时长 | 信息点 | 每信息点时长 |
|:----:|:------:|:----------:|
| 1分钟 | 3-5个 | 12-20秒 |
| 3分钟 | 8-12个 | 15-22秒 |
| 5分钟 | 15-20个 | 15-20秒 |

---

## 🎬 叙事节奏设计（v4.0 新增）

### 节奏类型

| 类型 | 场景切换间隔 | 适用内容 |
|------|:----------:|---------|
| 慢节奏 | 15-30秒 | 禅意、深度讲解 |
| 中节奏 | 8-15秒 | 知识科普、教程 |
| 快节奏 | 3-8秒 | 产品展示、高能混剪 |
| 爆发节奏 | <3秒 | 预告片、高潮段落 |

### 节奏原则

1. **开篇快**：前5秒抓住注意力
2. **中段稳**：匀速+转场过渡
3. **高潮爆发**：关键信息加速
4. **收尾缓**：给观众消化空间
5. **转折明显**：节奏变化处加信号（音效/画面切换）

---

## Common Bugs (18 verified)

| # | Symptom | Root Cause | Fix |
|---|---------|-----------|-----|
| 1 | Text invisible | PingFang.ttc missing `index=` | `Songti.ttc, index=0` |
| 2 | AI watermark | Seedream service embeds text | OCR detect → neighbor fill |
| 3 | Page flicker | Brightness delta too large | Adaptive dissolve: 14/18/24 |
| 4 | Frozen frames at boundaries | FFmpeg concat of video segments | Single YUV stream |
| 5 | BGM inaudible | Generated drone -53dB | Use real music, volume ≥12% |
| 6 | BGM has human speech | Extracted from narrated video | Band-reject 200-4000Hz |
| 7 | Wrong page mapping | Offset in page_map array | Verify: Q&A#1→page#4 |
| 8 | Generic sutra ref everywhere | Hardcoded "金刚般若波罗蜜经" | Read `s` field from qaData |
| 9 | Channel count mismatch | Mono narration + stereo BGM | ffmpeg auto-handles |
| 10 | BGM trim fails with cover art | MP3 has embedded image | Add `-vn` flag to ffmpeg |
| 11 | BGM loop discontinuities | `-c copy` on different formats | Re-encode with libmp3lame |
| 12 | Output larger than expected | CRF too low, preset=slow | preset=fast, crf=20 (~23MB) |
| 13 | QuickTime won't open | yuv444p pixel format | Force yuv420p |
| 14 | Hanging subtitle line | Design has dividing line | Remove ALL decorative lines |
| 15 | Title not centered | Estimated positions | Use EXACT center formulas |
| 16 | "金刚经问答" inside circles | Wrong Y position | Y = CY_CIRCLE + R_OUTER + 30 |
| 17 | BGM extraction 404 | Wrong CDN URL pattern | Use agent-browser to find real URL |
| 18 | Font download blocked | GitHub rate limit | Use jsDelivr CDN instead |

---

## Build Recipes (Ready-to-Use Templates)

### Recipe 1: Full Build from Scratch

```python
# Given: 30 story illustrations + per-page MP3s + qaData + BGM
pages = [1,2,4,5,6,7,9,10,11,12,13,14,16,17,18,19,20,21,22,23,25,26,27,28,30,31,32,33,34,35,36,38,39,40,41]
page_map = [4,5,6,7,9,10,11,12,13,14,16,17,18,19,20,21,22,23,25,26,27,28,30,31,32,33,34,35,36,38]

# 1. Download calligraphy font
subprocess.run(['curl','-sL','-o','/tmp/ma.ttf',
    'https://cdn.jsdelivr.net/gh/google/fonts@main/ofl/mashanzheng/MaShanZheng-Regular.ttf'])

# 2. Build cover (Stage 0)
# 3. Build content frames (Stage 1)
# 4. Encode video (Stages 2-3)
# 5. Mix audio + BGM (Stages 4-5)
# 6. Final mux (Stage 6)
```

### Recipe 2: Cover-Only Redesign

```python
# Use when user asks to redesign COVER only (keep everything else unchanged)
# Step 1: Generate new cover frame (Stage 0 code)
# Step 2: Replace page_01 in existing video (re-encode first segment)
# Step 3: Mux with original unchanged audio
```

### Recipe 3: BGM-Only Swap

```python
# Use when user provides a reference video with desired BGM
# Step 1: Extract audio from reference
subprocess.run(['ffmpeg','-y','-i',ref_video,'-vn','-c:a','libmp3lame','-b:a','128k','bgm.mp3'])
# Step 2: Loop if shorter than target
# Step 3: Mix into existing video at calibrated volume
subprocess.run(['ffmpeg','-y','-i',video,'-i','bgm_looped.mp3',
    '-filter_complex','[0:a][1:a]amix=inputs=2:duration=first:dropout_transition=2:weights=1 0.12[out]',
    '-map','0:v:0','-map','[out]','-c:v','copy','-c:a','aac','-b:a','192k','output.mp4'])
```

### Recipe 4: Reference Video Optimization

```python
# Use when user provides 2+ reference videos and wants best-of-both
# Step 1: Analyze both references
#   - Check cover design quality (pixel analysis)
#   - Check BGM volume and characteristics (volumedetect)
# Step 2: Choose strategy
#   - Plan A: Better BGM + Better Cover = optimized output
#   - Plan B: Fix one reference's weakness using the other
# Step 3: Execute merge and present comparison table
```

---

## Scripts

- `scripts/build_video.py`: Complete pipeline with all 6 stages.
  Provides `build_video()` function plus `build_cover()` and `mix_bgm()` utilities.

---

## v4.0 Changelog (2026-07-05 — 认识→模仿→创新→超越方法论集成)

### 新增
- **Stage -1: 认识阶段** — 参考视频逆向工程，含一键分析脚本 + 认识记录模板
- **模仿达标矩阵** — 9项硬性技术指标 + 自动化检查方法
- **创新维度矩阵** — 8个创新方向 + 难度评估 + 创新自检清单（5问）
- **超越评判标准** — 6个标志 + 超越公式
- **四道质量门禁** — 版权→技术→内容→平台合规，逐项通过
- **音频制作标准** — 配音质量分级（S/A/B/C）+ 后期处理流水线 + 质量标准
- **视觉呈现标准** — 画面质量分级 + 色彩规范 + 字体规范（含铁律）
- **叙事结构模板** — 三段式/五段式 + 信息密度标准
- **叙事节奏设计** — 4种节奏类型 + 5条设计原则

### 变更
- 版本号 3.0 → 4.0
- 描述更新，增加「四阶段方法论驱动」定位
- 触发词增加：分析参考视频、视频逆向工程、模仿视频、视频方法论

---

## v3.0 Changelog (distilled from v1→v28 iterations)

- Remotion-based declarative pipeline
- Stage 0: Cover Design Engine with pixel-verified geometry
- BGM source priority ranked by real-world success rate
- Volume calibration table from actual reference comparisons
- 10 new bug fixes (9→18)
- 4 ready-to-use Build Recipes
- Reference video optimization workflow
- Xiaohongshu 1080×1080 standard specification
- Exhaustive "what NOT to add" design constraint list

## Zcode 集成

### τ 角色与贡献

本技能在 Zcode 体系中承担 **executor** 角色，遵循 `skills/shared/zcode/zcode-embedding-standard.md` 标准。

| 指标 | 方向 | 机制 | 目标压缩 |
|------|------|------|---------|
| τ_execute | reduce | Remotion组件模板 + 批量渲染管线 | 35% |
| τ_qa | auto | 自动内容合规检查清单 | auto |

### 质量门禁

- **等级**: enhanced
- **依据**: `skills/shared/skill-quality-gate.md`
- **执行前**: 输入校验 + 反模式预检（`skills/shared/feedback/anti-patterns.yaml`）
- **执行后**: 输出校验 + 交付判定（三阶段门禁）

### 交叉验证

- **协同技能**: multimodal-bridge, picture-book-pipeline
- **校验协议**: `skills/shared/zcode/zcode-embedding-standard.md` 第 4 节

### 反馈闭环

- **输出触发**: Memory 写入 + τ 快照更新 + 反模式比对（如适用）
- **遵循协议**: `skills/shared/feedback/feedback-loop-protocol.md`

---
*Zcode 嵌入版本: 1.0 | © 版权所有：默笙夏夏の知書房 - 2026-07-09*
