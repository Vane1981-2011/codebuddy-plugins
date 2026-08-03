---
name: picture-book-pipeline
description: >
  全流程 AI 绘本生产线。覆盖7种作品类型（对话解经/漫画冒险/单图叙事/诗歌独白/段落叙事/自然悟道/儿童绘本）、
  4种角色系统、5种版面模式。Full-stack AI picture book production line.
version: 3.5.0
agent_created: true
qualityGate: enhanced
trigger_recommended:
  - 绘本生成
  - 画册
  - 国风绘本
  - picture book
  - Seedream 生图
  - 漫画生成
  - 儿童绘本
  - 双语绘本
  - 家训绘本
  - 道德经绘本
trigger_exclusive:
  - AI绘本生产线
  - 全流程绘本
anti_triggers:
  - 普通图片生成
  - 视频制作
  - 股票分析
dependencies:
  - spa-engineering-guard
  - top-tier-designer (optional)
  - quality-assessment-expert-system (optional)
supersedes: null
zcode:
  version: "1.0"
  τ_role: executor
  τ_impact:
    - metric: τ_execute
      direction: reduce
      target: 40%
      mechanism: 7种作品类型x5种版面的模板矩阵
    - metric: τ_qa
      direction: auto
      target: auto
      mechanism: 角色一致性自动校验
  bus_compatible: true
  cross_validate_with:
    - multimodal-bridge
    - video-production-pipeline
disable: true
last_updated: 2026-07-01
---

# Picture Book Pipeline — AI 绘本生产线

## 概览

全流程 AI 绘本生产系统，覆盖 7 种作品类型、4 种角色系统、5 种版面模式。V3.4 新增 HTML→PDF 标准化管道+分龄文字密度表+系列化设计器+读者互动引擎+结尾分层模板+文件优化指南（五作横评驱动）。

### V3.4 新增能力（2026-06-24 · 五作横评竞品分析）

> 基于5本不同大模型+工具生成的绘本 PDF 深度横向对比，提取可复用生产模式。完整分析报告：项目目录下 `五作横评_AI绘本竞品深度分析报告.md`

| 新增模块 | 来源 | 功能 |
|---------|------|------|
| **HTML→PDF 标准化管道** | 《石猴出世》+《一只特立独行的猪》 | Chrome/Skia HTML渲染→PDF 作为默认输出格式，保留完整文字层+图片层 |
| **分龄文字密度表** | 五作综合 | 按0-2/2-4/3-6/5-8/8+岁推荐字数/字号/行数 |
| **系列化设计器** | 《石猴出世》 | 系列标识+末页预告+角色跨册延续模板 |
| **读者互动引擎** | 《石猴出世》 | 猜测/邀请/共情/挑战四模式打破第四面墙 |
| **结尾分层模板** | 《石猴出世》+《猴子捞月》 | 收束→主题升华→系列钩子三层结尾结构 |
| **文件优化指南** | 五作综合 | 按场景目标文件大小+压缩策略+图片格式选择 |
| **生产工具决策树** | 五作综合 | HTML→PDF vs 图片拼合 路线选择决策框架 |
| **角色命名公式** | 《猴子捞月》 | [排行]+[族属]+[特征词] 标准化命名模板 |

### V3.3 新增能力（2026-06-21 · 三作深度分析）

| 新增模块 | 来源 | 功能 |
|---------|------|------|
| 三页一课段落叙事 | 《恒·曾国藩家训》 | 每课3页弧线：情境→教导→行动 |
| 意象锚定物系统 | 《恒·曾国藩家训》 | 1个固定视觉元素贯穿全书作为记忆锚点 |
| 现代场景适配 | 《恒·曾国藩家训》 | 古典智慧+当代生活场景融合叙事 |
| 三代传承角色系统 | 《恒·曾国藩家训》 | 爷爷+少年+意象物 非说教成长模型 |
| 自然为师教学法 | 《道可道》《天下皆知》 | 山水为师，人物退为观察者 |
| 经文尾页分离式 | 《道可道》《天下皆知》 | 故事与经文不互相干扰的排版策略 |

### V3.2 新增能力（2026-06-21 · 质量管控专题）

### 🔴 Seedream 5.0 生图强制约束（每次调用无条件执行）

> **画面中禁止出现任何文字、字母、数字、Logo、水印及边框，无一例外。**
> 所有 ImageGen / Seedream 调用场景中必须严格遵守此约束。
> 违反此规则的图片必须重新生成或裁剪处理。

```
禁止清单:
  ✗ 任何中文/英文/数字文字
  ✗ "图片由 AI 生成" / "AI Generated" 水印（ImageGen 默认水印）
  ✗ 商标/Logo/品牌标识
  ✗ 水印/版权标记
  ✗ 边框/装饰性框架
  ✗ 任何非图像内容的符号标记
```

**ImageGen 水印规避（关键）：**
- ImageGen 工具生成图片时默认添加 "图片由 AI 生成" 水印
- 调用时必须设置 `footnote` 参数为空字符串：`"footnote": ""`
- 如 footnote 设为空后仍出现水印，生成后立即裁剪底部 80px 去除

### V3.2 新增能力（2026-06-21 · 质量管控专题）

| 新增模块 | 功能 |
|---------|------|
| 七维质检SOP | 角色规范/镜头衔接/图文对应/元素连续/声画同步/品质统一/像素审查 |
| 双检机制 | 初审(自动化) → 复审(AI审查) → 签批交付 |
| Seedream 无文字强制约束 | 画面绝对禁止任何文字/水印/Logo/边框 |

### V3.1 新增能力（2026-06-21 · 儿童绘本专题）

基于《鸟的语言 · 儿童绘本》深度分析提炼：

| 新增模块 | 来源 | 功能 |
|---------|------|------|
| children-a4 版面 | 《鸟的语言》 | 儿童专属：83/17图文比、12-14pt大字、粉彩暖色 |
| 民间故事三幕模板 | 《鸟的语言》 | 获得→试炼→和解+道德升华结构 |
| 双语排版系统 | 《鸟的语言》 | 中文上/英文下同区域对照排版 |
| 亮度-情感映射 | 《鸟的语言》 | 亮度区间精确映射故事情感节点 |
| 对话引号系统 | 《鸟的语言》 | 弃用角色标签，统一引号包裹+说话者后置 |
| 质量评估标准 | 四作综合 | 5维25项评分标准+S/A/B/C/D评级 |

### V3.0 新增能力（2026-06-21）

基于同学AI绘本作品深度分析提炼：

| 新增模块 | 来源 | 功能 |
|---------|------|------|
| 多格式版面系统 | 《道德经》+《冒姓琅琊》 | 3种排版模式：禅意正方/漫画A4/经典A4 |
| 叙事结构模板库 | 两部作品 | 师生对话式、五幕式网文等叙事框架 |
| 情感-字号联动 | 《冒姓琅琊》 | 场景情绪自动映射字号缩放 |
| 信息密度节奏控制 | 《冒姓琅琊》 | 每页文字行数/分镜数/字号三维调控 |
| 角色系统设计器 | 两部作品 | 双人对话/群像钩子/独角旅程模式 |
| 反转折页钩子 | 《冒姓琅琊》 | 章节结尾悬念制造技法 |
| 体验式教学叙事 | 《道德经》 | 引导读者主动体验的认知转折法 |

## 触发条件

- 用户提到"生成绘本""画册""国风绘本""picture book"
- 用户提供绘本分镜脚本和画面描述
- 用户需要批量生成统一风格的插图
- 用户需要将图片排版为可打印的绘本网页

## 环境前提

开始前必须验证以下条件：

1. ARK API Key 已配置在 `~/.workbuddy/models.json` 中
2. Seedream 5.0 模型 (`doubao-seedream-5-0-260128`) 已在火山引擎控制台开通
3. Python 3 可用，`urllib.request` 标准库无需额外安装
4. macOS 系统已安装 `sips` 命令行工具（系统内置）

验证命令：
```bash
curl -s -X POST "https://ark.cn-beijing.volces.com/api/v3/images/generations" \
  -H "Authorization: Bearer <API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{"model":"doubao-seedream-5-0-260128","prompt":"A simple test image","size":"1920x1920","response_format":"b64_json"}' \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print('OK' if 'data' in d else d)"
```

## 执行流程

### Phase 0: 叙事规划（新增）

在开始生图前，先确定叙事结构、情感曲线和版面模式。

#### Step 0.1: 选择叙事模板

参考 `references/narratives/` 中的模板：

| 模板 | 文件 | 适用场景 |
|------|------|---------|
| 师生对话式 | `dialogue_mentor.md` | 经典解读、知识绘本、哲学绘本 |
| 五幕式网文 | `five_act_webnovel.md` | 漫画、剧情绘本、连载故事 |
| **民间故事三幕式** | **`folktale_three_act.md`** | **儿童故事、民间传说、道德寓言** |
| 三幕式经典 | (待补充) | 通用故事绘本 |
| **三页一课段落叙事** | **`three_page_lesson.md`** | **家训/教育类、品格培养** |
| **自然为师教学法** | **`nature_teacher.md`** | **哲学经典、道德经系列** |

#### Step 0.2: 选择版面模式

参考 `references/layout_systems.md`：

| 模式 | ID | 图文比 | 字号 | 适用 |
|------|-----|--------|------|------|
| 禅意正方 | `square-zen` | 75/25 | 9pt | 哲学、诗歌、留白美学 |
| 漫画A4 | `comic-a4` | >90%画面 | 8-12pt | 漫画、剧情类 |
| 经典A4 | `classic-a4` | 56/44 | 10pt | 默认通用 |
| **儿童A4** | **`children-a4`** | **83/17** | **12-14pt** | **3-8岁儿童绘本** |

#### Step 0.3: 设计情感曲线

参考 `references/rhythm_controller.md`，为每个页面分配：
- `emotion_level` (calm/curious/tense/climax/twist)
- `target_lines` (目标文字行数)
- `font_multiplier` (字号倍率 0.80-1.15)

#### Step 0.4: 设计角色系统

参考 `references/character_system_designer.md`：
- 选择模式：`dual_dialogue` / `ensemble_cast` / `solo_journey`
- 为每个角色定义钩子（identity/skill/culture/action/voice）
- 确定对话比例和出场节奏

### Phase 1: 角色设定与锁定

根据用户提供的角色描述，生成**英文角色锁定词**。锁定词必须在后续所有生图 prompt 中保持一致。

规则：
- 每角色 3-5 句，覆盖外貌、衣着、年龄、气质
- 颜色必须精确（如 `pure WHITE` 而非 `cream-white` 以避免漂移）
- 关键特征用大写强调（如 `must be pure white, not gray not brown`）
- 双人同框场景追加关系描述 + 比例对比词

参考 `references/character_locks.md` 中的标准化模板。

### Phase 2: 角色参考图集生成

生成多角度多表情的角色参考表，作为后续生图的视觉锚点。

生图 prompt 结构：
```
[6 panels of same character, clean background]
+ [panel 1: front view, expression A]
+ [panel 2: 3/4 view, expression B]
+ ... (6 panels total)
+ [Character lock: ...]
+ [Style lock]
+ [Negative constraints]
```

调用 API 方式见 `references/seedream_api.md`。

### Phase 3: 批量场景生图

使用 `scripts/batch_generate.py` 进行批量生图。

使用方式：
```bash
python3 <SKILL_DIR>/scripts/batch_generate.py <scenes.json> \
  --api-key <KEY> \
  --output <DIR> \
  --prefix "page"
```

参数说明：
- `<scenes.json>` — 位置参数，场景描述 JSON 文件路径
- `--api-key` — Seedream 5.0 ARK API Key
- `--output` — 输出目录（创建后存放生成的图片）
- `--prefix` — 文件名前缀，默认 "page"

脚本特性：
- 每个 prompt 自动追加角色锁 + 画风锁 + 负向约束
- 串行调用，间隔 2 秒防限流
- 失败自动重试一次
- 输出 JPEG 格式 (b64_json → 本地解码)

批量生成脚本文档见 `references/seedream_api.md` 的 "批量生成" 章节。

### Phase 4: 格式转换

JPEG → PNG 转换（macOS）：

```bash
for f in output_dir/*.jpg; do
  sips -s format png "$f" --out "images/book-name/page-XX.png"
done
```

### Phase 5: HTML 排版

使用 `assets/page_template.html` 作为排版基础模板，或选用 `assets/layouts/` 中的专用模板。

#### 版面模式选择

| 模式 | 模板路径 | CSS变量文件 |
|------|---------|------------|
| 禅意正方 | `assets/layouts/square-zen.html` | `references/layout_systems.md` § 模式一 |
| 漫画A4 | `assets/layouts/comic-a4.html` | `references/layout_systems.md` § 模式二 |
| 经典A4 | `assets/page_template.html` | 现有默认 |

#### 经典A4（默认）

关键参数：
- `@page { size: A4 portrait; margin: 0; }` — 打印 A4 无页边距
- `.page { width: 210mm; min-height: 297mm; }` — 每页 A4 尺寸
- `.page-img { height: 56%; }` — 图片占上部 56%
- 正文在 `.page-content` 中，与图片完全分离

封面页：全幅背景图 + 标题/副标题文本
正文页：上图下文，`.zen-text` 用左边框突出禅意金句
封底页：全幅图 + 底部结语

#### 禅意正方 `square-zen`（新增）

- 画幅 595×595px 正方形
- 画面区 75% + 文字区 25%（固定145px高）
- 文字区固定底部，透明背景蒙层
- 字号 9.5pt（对话）/ 8.5pt（旁白）/ 11pt（经文）
- 页码固定在右下角

#### 漫画A4 `comic-a4`（新增）

- A4 595×842px 纵向
- 多分镜网格布局
- 对话气泡式文字（`.speech-bubble`）
- 情绪字号联动 CSS class（`.emotion-calm` ~ `.emotion-climax`）
- 角色标签系统（`.character-tag`）

#### 儿童A4 `children-a4`（新增）

- A4 595×842px 纵向
- 图像区 83% + 文字区 17%（固定140px高）
- 大字号 12-14pt，适合儿童/亲子共读
- 文字区可分上（中文）下（英文）双语排列
- 对话用引号包裹 + 说话者后置，不使用角色标签
- 暖色粉彩基调（亮度200-234），情感低谷可降至145-170
- CSS 变量：`--text-zone-height: 140px; --font-size-base: 13pt;`

### Phase 6: 预览交付

使用本地 HTTP 服务器预览：
```bash
cd <project-dir> && python3 -m http.server 18890 &
```

通过 `present_files` 打开 `http://localhost:18890/<book>.html`。

关闭服务器：`kill $(lsof -ti:18890)`

## 画风锁定（默认值）

```
Traditional Chinese ink wash watercolor illustration style
for a printed picture book.
Soft warm low-saturation color palette:
warm cream paper background, pine green, ochre brown,
light brown, mist blue, warm beige.
Gentle rounded brushstrokes throughout,
absolutely no sharp or angular lines.
East Asian Zen aesthetic, serene warm golden ambient lighting.
Clean spacious composition with intentional negative space.
The illustration should look like hand-painted watercolor on textured rice paper.
```

## 负向约束（默认值）

```
NO text, NO letters, NO numbers, NO labels,
NO logos, NO watermarks, NO borders, NO frames,
NO Buddha statues, NO religious symbols, NO ritual objects,
NO sharp angular lines, NO high saturation colors,
NO cluttered busy composition,
NO inconsistent character designs,
NO realistic photo style, NO digital art style
```

## 踩坑速查

| 问题 | 原因 | 解决 |
|------|------|------|
| `ModelNotOpen` | ARK 账号未激活 Seedream | 在火山引擎控制台开通模型 |
| `size` 错误 | 分辨率 < 3,686,400px | 最小用 1920×1920 |
| 图片不显示 | JPEG 文件 .png 扩展名 | 用 `sips -s format png` 真转换 |
| 角色漂移 | prompt 未含锁定词 | 每 prompt 强行追加角色锁 |
| 画风不统一 | 场景描述缺全局锚点 | 固定 STYLE 常量全文不变 |
| 429 限流 | ImageGen 内置工具 | 改为直连 ARK API |
| 白袍变灰 | prompt 中 `cream-white` | 改为 `pure WHITE (not gray)` |
| **场景索引漂移** | `chapters` 数组与 `SCENES` 条目数不一致 | 每次改面板后 `assert sum(chapters)==len(SCENES)` |
| **分批次画风漂移** | 多个独立 fix 脚本不同时段调 API | 需跨帧一致的系列必须在同一次进程串行生成 |
| **prompt 过度发挥** | 添加了文字未描述的动作/道具 | prompt=文字描述+角色锁+风格锁+负向锁，不额外添加 |
| **屏幕截断** | `.page` 有 `max-height: 297mm; overflow: hidden` | 仅 `@media print` 应用，屏幕模式移除 |
| **多面板打印断开** | 4-5面板页内容超 A4 | 打印 `break-inside: avoid` + `max-height: 18vh !important` |
| **行内样式覆盖** | `style="font-size:..."` 覆盖 CSS | 改用 CSS class（`.panel-text.compact`） |
| **硬编码颜色** | body 中有 `#xxxxxx` | 全部收敛至 `:root` 变量 |
| **非原文元素** | 如水龙头、地板、帽子、木鱼 | 负向锁显式排除 `NO modern fixtures/flooring/hats` |
| **图文姿态不符** | "躺/趴"→图片站/坐 | 每 prompt 加 `NOT standing, NOT sitting` |
| **积木/道具颜色跨帧不一致** | 分帧 prompt 描述不同 | 同章道具颜色在 SHARED 块中硬编码 |
| **经文引用非原文** | "放下""不嗔不怒"非金刚经原文 | 全部替换为鸠摩罗什译本正宗原文 |
| **文本区高度漂移** | square-zen模式文字区浮动 | 固定`.page-text { height: 145px; }` |
| **漫画页字号杂乱** | 情绪变化用inline style | 统一用`.emotion-*` CSS class |
| **角色钩子失效** | 角色有标签但剧情未用 | 检查每个钩子是否在剧情中触发≥1次 |
| **结尾反转无伏笔** | P15反转在前14页无铺垫 | 反转触发点必须在P1-P5中埋设 |

## V3 升级规则（2026-06-21 跨作品分析复盘）

### 叙事规划铁律
1. **模板先行**：任何绘本项目必须先选择叙事模板和版面模式（Phase 0），再进入角色设定
2. **情感曲线预设计**：为每页预设 emotion_level 和 font_multiplier，避免后期临时调整破坏风格一致性
3. **密度黄金3页**：每连续3页必须有一次节奏变化，禁止超过3页同一密度

### 多格式版面铁律
4. **固定分屏**：`square-zen` 模式的文字区高度固定为145px，全册不得浮动
5. **情绪字号联动**：`comic-a4` 模式字号必须通过 CSS class 控制，禁止 inline style
6. **图文比锁定**：选定模式后全册图文面积比必须保持一致

### 角色系统铁律
7. **一角色一钩子**：群像模式中每个角色必须有且仅有一个核心记忆钩子
8. **钩子须有剧情作用**：禁止为角色添加与剧情无关的特征标签
9. **出场节奏控制**：主要角色必须在开篇3页内全部亮相

### 终局设计铁律
10. **反转折页**：章节最后2页必须遵循"假性安全→意外反转"模式
11. **悬念闭环**：每章反转必须在本章内给出伏笔（前5页内埋设）

完整分析报告：`references/analysis-report-cross-works.md`

### 批次管理铁律
1. **单进程原则**：任何需跨帧画风一致的系列，必须在同一次 Python 进程中串行生成
2. **索引校验**：修改面板拆分后必须 `assert sum(chapters) == len(SCENES)`
3. **跨帧共享块**：同章多帧使用 SHARED_SETTING 块锁定背景/道具/位置
4. **锁不漂移**：全册使用同一套 LOCK_DICT，不跨批次修改

### 图文对齐铁律
5. **零添加原则**：prompt = 文字描述 + 角色锁 + 风格锁 + 负向锁，不添加文字未提及的任何元素
6. **姿态锁定**：文字"躺/趴/蹲/坐/站" → prompt 显式锁定对应姿态 + `NOT [错误姿态]`
7. **数量核对**：文字中物品数量与 prompt 一致，多帧间颜色/形状锁定

### 排版铁律
8. **屏幕不截断**：`.page` 不加 `max-height`/`overflow:hidden`
9. **打印不拆分**：`@media print` 中全面 `break-inside:avoid`
10. **CSS 变量优先**：颜色、字号、间距统一用 `:root` 变量，0 行内覆盖

完整复盘文档：项目目录下 `picture-book-pitfalls.md`

## 出版级质检流程

执行 `references/qa-sop-picture-book.md` 中定义的五轮质检标准操作规程：

| 轮次 | 内容 | 方法 |
|------|------|------|
| 第一轮 | 结构完整性 | 程序化审计：章节连续性、Q&A对数、面板文件、版权、CSS变量 |
| 第二轮 | 经文校队 | 逐条与《金刚经》鸠摩罗什译本原文比对 |
| 第三轮 | 图文映射 | 场景/姿态/数量/道具/情感 八维逐帧检查表 |
| 第四轮 | 风格统一 | 角色锁一致性、画风漂移检测、色彩光影品质 |
| 第五轮 | 排版完整性 | 屏幕截断/打印拆分/字号/颜色/字体五维检查 |

角色标准视觉规范：`references/character-visual-spec.md` |

### 新增参考文档（V3.0）
- 多格式版面系统：`references/layout_systems.md`
- 叙事结构模板库：`references/narratives/`
  - 师生对话式：`references/narratives/dialogue_mentor.md`
  - 五幕式网文：`references/narratives/five_act_webnovel.md`
- 信息密度节奏控制器：`references/rhythm_controller.md`
- 角色系统设计器：`references/character_system_designer.md`
- 跨作品分析报告：项目目录下 `绘本作品深度分析报告.md`

### 新增参考文档（V3.1）
- 儿童A4版面CSS模板：`assets/layouts/children-a4.html`
- 民间故事三幕叙事：`references/narratives/folktale_three_act.md`
- 绘本质量评估标准：`references/quality_checklist.md`
- 双语排版系统规范：`references/bilingual_support.md`
- 儿童绘本分析报告：项目目录下 `鸟的语言_深度分析报告.md`

### 新增参考文档（V3.2）
- 七维质检标准化SOP：`references/qa-seven-dimensions.md`（7大维度×36条检查标准+双检机制+签批流程）

## V3.1 升级规则（2026-06-21 · 儿童绘本专题）

### 儿童绘本铁律
12. **大字号优先**：儿童绘本字号不得低于12pt，亲子共读模式建议13-14pt
13. **单图单页**：儿童绘本每页只放一个场景/一个事件节点，禁止多分镜
14. **情感安全**：负面情绪不得超过连续2页，必须3页内回升
15. **暖色主导**：儿童绘本禁止全册冷色调，最低亮度不低于140
16. **字数控制**：儿童绘本每页中文不超过50字（不含英文翻译）

### 双语排版铁律
17. **中上英下**：双语模式下中文在上为主语言，英文在下为辅助语言
18. **字号统一**：中英文字号必须一致，不可一大一小
19. **同区排布**：中英文必须在同一文字区域内，不可分列两个独立区域

### 对话处理铁律
20. **引号包裹**：故事叙事型绘本使用引号标记对话，弃用「角色名：」格式
21. **说话者后置**：对话后的归属统一「XXX说/问」格式

### 叙事结构铁律
22. **三幕比例**：民间故事型绘本严格保持25%-55%-20%篇幅分配
23. **道德页独立**：道德提炼放在故事结束后独立一页，不嵌入叙事

### 质量交付铁律
24. **交付前评分**：每本绘本交付前使用 `references/quality_checklist.md` 自评，得分≥80方可交付
25. **四作交叉验证**：新作完成前须与同类模板的标杆作品做结构对比

## V3.2 升级规则（2026-06-21 · 质量管控专题）

### Seedream 5.0 生图硬约束
26. **零文字零水印**：每张生成图片画面内绝对禁止文字/字母/数字/Logo/水印/边框，违反立即重新生成
27. **生图后自检**：每批次图片生成后执行自动化文字检测脚本，不通过不进入下阶段

### 七维质检体系（新增）
28. **角色视觉规范**：同一角色跨页面部/体型/服装/发型/肤色一致，偏差>5%=不合格
29. **镜头衔接逻辑**：无空间/时间/情感断层，不连续3页同景别
30. **图文精准对应**：文字提及的所有人物/物品/动作/情绪均在图中呈现，禁止遗漏或添加
31. **视觉元素连续**：同一道具/服装/场景跨页颜色/形态/位置一致
32. **声画同步**：对话语气-角色表情匹配，情感语调-画面氛围匹配
33. **整体品质统一**：全册色调/光影/构图风格一致，亮度变化须有叙事逻辑
34. **像素级审查**：主体裁切安全>5%边缘、水平线偏差<1°、标点全册统一

### 双检交付铁律
35. **双检不通过不交付**：初审(自动化)通过率≥70% + 复审(AI审查)通过率≥80% 方可交付
36. **三连不过复盘**：同一维度连续3次不通过，触发全流程复盘

完整质检SOP：`references/qa-seven-dimensions.md`

## V3.3 升级规则（2026-06-21 · 叙事模式拓展）

### 段落叙事铁律
37. **三页一课**：家训/教育型绘本每课固定3页结构（情境→教导→行动），不可压缩或扩展
38. **行动页前置**：每课最后一页必须是主角的主动行动，不依赖外力催促

### 意象锚定物铁律
39. **一书一锚定物**：每本绘本必须有且仅有一个贯穿全书的核心视觉意象
40. **锚定物闭环**：首次和最后一次出现必须形成从"外物"到"内化"的叙事闭环
41. **间隔≥3页**：锚定物每次出现之间必须间隔至少3页

### 现代场景铁律
42. **古典+当代融合**：改编古典素材时，场景必须根植当代日常（手机/考试/拖地），人物关系现代化
43. **精神内核不变**：场景可现代，但原文核心思想不可简化或歪曲

### 经文展示铁律
44. **二选一策略**：经文展示要么嵌入式（每页一行），要么尾页分离式（最后一页集中），不可混用

### 角色系统铁律
45. **类型匹配**：哲学经典→单字名（生/师），日常成长→双字名（少年/爷爷/明心）

### 新增参考文档（V3.3）
- 三页一课段落叙事：`references/narratives/three_page_lesson.md`
- 三本新绘本分析报告：项目目录下 `三本新绘本_深度分析报告.md`

## V3.4 升级规则（2026-06-24 · 五作横评驱动）

### HTML→PDF 生产铁律
46. **HTML→PDF 为默认输出格式**：所有绘本必须使用 Chrome/Skia HTML→PDF 渲染，禁止纯扫描件输出。文字层+图片层混合型 PDF 是唯一交付格式
47. **每页必须有完整文字层**：禁止纯图片PDF——文字层使绘本可检索/可复制/可朗读/无障碍访问

### 分龄控制铁律
48. **文字密度分龄**：2-4岁≤24字/页，3-6岁≤50字/页，5-8岁≤120字/页，8+/成人≤150字/页
49. **行数分龄**：2-4岁1-2行，3-6岁2-3行，5-8岁4-8行，成人不限

### 文件效率铁律
50. **文件大小上限**：儿童绘本(≤30页)≤15MB，成人绘本(≤30页)≤50MB。超出需JPG 75%压缩
51. **单页嵌入图数**：儿童绘本=1张满幅，成人绘本≤5张分镜，封面除外

### 系列化铁律
52. **系列化从第一本开始**：首本即标注系列名+序号（"西游记绘本·第一本"），末页必须包含下一本标题+一句话预告
53. **系列品牌统一**：全系列封面/字体/排版位置保持一致，角色跨册延续

### 交互铁律
54. **交互提问必有答案**：对读者的提问（"你猜..."）必须在下一页立即揭晓，悬念→满足≤1页
55. **拟声词节奏**：儿童绘本适当使用拟声词（砰/嗖/哗——/扑通）增强听觉参与感

### 结尾铁律
56. **绘本结尾三层结构**：故事收束（1-2页正文）→ 主题升华（独立页金句）→ 系列钩子（如有续集）
57. **道德页独立**：主题/道德提炼置于故事结束后独立页，不嵌入最后一页叙事中（延续V3.1铁律23）

### 角色命名铁律
58. **群像角色命名公式**：多角色故事使用 [排行]+[族属]+[特征词] 公式（如大猴哥/二猴姐/三猴弟/四猴小胖）

### 新增参考文档（V3.4）
- HTML→PDF 标准化管道：`references/production_pipeline_html2pdf.md`
- 分龄文字密度表：`references/age_text_density.md`
- 系列化设计器：`references/serialization_designer.md`
- 读者互动引擎：`references/reader_engagement.md`
- 结尾分层模板：`references/ending_patterns.md`
- 角色命名公式：`references/character_naming.md`
- 文件优化指南：`references/file_size_optimization.md`
- 生产工具决策树：`references/tool_decision_tree.md`
- 五作横评深度分析报告：项目目录下 `五作横评_AI绘本竞品深度分析报告.md`

## Zcode 集成

### τ 角色与贡献

本技能在 Zcode 体系中承担 **executor** 角色，遵循 `skills/shared/zcode/zcode-embedding-standard.md` 标准。

| 指标 | 方向 | 机制 | 目标压缩 |
|------|------|------|---------|
| τ_execute | reduce | 7种作品类型x5种版面的模板矩阵 | 40% |
| τ_qa | auto | 角色一致性自动校验 | auto |

### 质量门禁

- **等级**: enhanced
- **依据**: `skills/shared/skill-quality-gate.md`
- **执行前**: 输入校验 + 反模式预检（`skills/shared/feedback/anti-patterns.yaml`）
- **执行后**: 输出校验 + 交付判定（三阶段门禁）

### 交叉验证

- **协同技能**: multimodal-bridge, video-production-pipeline
- **校验协议**: `skills/shared/zcode/zcode-embedding-standard.md` 第 4 节

### 反馈闭环

- **输出触发**: Memory 写入 + τ 快照更新 + 反模式比对（如适用）
- **遵循协议**: `skills/shared/feedback/feedback-loop-protocol.md`

---
*Zcode 嵌入版本: 1.0 | © 版权所有：默笙夏夏の知書房 - 2026-07-09*
