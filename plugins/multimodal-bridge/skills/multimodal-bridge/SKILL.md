---
name: multimodal-bridge
description: |
  DeepSeek V4 Pro 多模态桥接层——弥补纯文本LLM在图像/视频处理上的能力缺口。提供五条桥接路径：OCR桥(图片→文本)、生图桥(文本→图片)、搜索桥(图片元数据搜索)、3D/特效桥(文本→3D模型/视频特效)、🆕视频桥(视频→文本)。触发词：识别图片、OCR、提取图片文字、生成图片、生成插图、文生图、搜索参考图、生成3D模型、视频特效、图片分析、分析视频、mp4、视频理解、提取视频内容。This skill should be used whenever the user needs image recognition, text extraction from images, AI image generation, image search, 3D/vfx generation, or video content analysis through a text-only LLM.
version: 1.1.0
agent_created: true
qualityGate: standard
zcode:
  version: "1.0"
  τ_role: executor
  τ_impact:
    - metric: τ_execute
      direction: reduce
      target: 20%
      mechanism: 5条桥接路径消除模态转换摩擦力
    - metric: τ_cognize
      direction: reduce
      target: 10%
      mechanism: 自动路由到最优桥接路径
  bus_compatible: true
  cross_validate_with:
    - frontend-dev
    - video-production-pipeline
disable: true
---

# 多模态桥接层 — Multimodal Bridge

## Purpose

为 DeepSeek V4 Pro（纯文本 LLM）提供多模态处理能力的桥接层。所有图像任务通过四条路径在"进入 DeepSeek 前"完成格式转换，或"在 DeepSeek 输出后"由外部工具执行。

## Core Constraint

**DeepSeek V4 Pro API 无视觉输入通道。** 无法通过 Read 工具或任何中间件"让模型看见图片"。所有桥接路径的本质是：
- 图像 → 文本路径：外部工具提取文字 → 传入 DeepSeek 分析
- 文本 → 图像路径：DeepSeek 写 Prompt → 外部 API 生成

## Four Bridge Paths

### Bridge A: OCR Bridge（图片 → 文本）

When the user provides an image and needs text extraction or analysis.

**Workflow:**
1. Detect input type (image file path or base64)
2. Call `scripts/ocr_bridge.py` to extract text via pytesseract
3. Pass extracted text to DeepSeek with context prefix: "以下是从图像中提取的文字，请分析：\n{text}"
4. DeepSeek analyzes the text content

**Supported formats:** PNG, JPG, JPEG, TIFF, BMP, PDF (first page), MP4, MOV, AVI, WebM, MKV (via Video Bridge)
**Languages:** Chinese (chi_sim) + English (eng) by default

### Bridge B: Image Generation Bridge（文本 → 图片）

When the user requests image generation.

**Workflow:**
1. DeepSeek optimizes user's description into a professional prompt
2. Route to the best available API:
   - Route 1: MiniMax image-01 (`scripts/imagen_bridge.py --backend minimax`)
   - Route 2: Seedream 5.0 ARK (`scripts/imagen_bridge.py --backend seedream`)
   - Route 3: buddy-cloud.py (`scripts/imagen_bridge.py --backend buddy`)
3. Save generated images to local path
4. Return image paths and metadata to user

**Prompt enhancement rules:**
- Always append "NO text, NO watermark, NO AI Generated" to every prompt
- For character art: specify hair color, eye color, expression, element theme, background style
- For scenes: specify lighting, composition, mood, color palette
- Always append quality keywords: "high quality, sharp details, clear facial features, no distortion"

**Image Quality Constraints (mandatory negative prompts):**

Every image generation prompt must include the following negative constraints:

| Category | Negative Prompt Keywords | Applies To |
|----------|-------------------------|------------|
| Sharpness | `blurry, soft focus, out of focus, motion blur, smeared, smudged` | All |
| Face Quality | `distorted face, deformed face, asymmetric eyes, bad anatomy, extra fingers, fused fingers, poorly drawn face` | Characters |
| Style Deformation | `chibi, Q-style, cartoon deformation, exaggerated proportions, SD style` | Characters |
| Noise/Artifacts | `noise, grain, JPEG artifacts, compression artifacts, pixelation` | All |
| Resolution | `low resolution, low quality, stretched, 720p, 480p, pixelated upscale` | All |
| Text/Watermark | `text, watermark, signature, logo, copyright mark, branding, lettering` | All |
| Lighting | `overexposed, underexposed, harsh lighting, flat lighting` | Scenes |
| Multi-Character | `cloned face, duplicated character, multiple copies, mirror reflection twin` | Characters |

**Full negative prompt template (append to every generation):**
```
NO text, NO watermark, NO AI Generated, NO blur, NO noise, NO distortion, 
NO smudging, NO Q-style deformation, NO low resolution, NO stretched image, 
sharp facial features, natural skin texture, high detail, crisp lines
```

### Bridge C: Image Search Bridge（查询 → 图片元数据）

When the user needs reference images or visual inspiration.

**Workflow:**
1. DeepSeek formulates search query
2. Call `mcp__serper-search__search_images` with query
3. Return image URLs, titles, and source domains
4. DeepSeek analyzes search results for trends/patterns

### Bridge D: 3D/VFX Bridge（文本 → 3D/特效）

When the user needs 3D model generation or video effects.

**Workflow:**
1. DeepSeek processes user's 3D/vfx request
2. Route to `scripts/buddy_bridge.py`:
   - 3D generation: `buddy-cloud.py 3d --prompt "description"`
   - Video effects: `buddy-cloud.py video-fx --template TID --image input.jpg`
3. Save output files to local path

### 🆕 Bridge E: Video Bridge（视频 → 文本）

When the user provides a video file (.mp4, .mov, .avi, .webm) and needs content analysis, frame extraction, or scene description.

**Supported formats:** MP4, MOV, AVI, WebM, MKV

**Workflow:**
1. Detect input type (video file path)
2. Extract key frames using ffmpeg:
   ```bash
   ffmpeg -i input.mp4 -vf "fps=1" -q:v 2 frames/frame_%04d.jpg
   ```
3. Send each extracted frame to Ollama minicpm-v:8b via local proxy for description
4. Compile frame descriptions into a timeline narrative
5. Pass the compiled narrative to DeepSeek for final analysis

**Dependencies:** ffmpeg (brew install ffmpeg), Ollama with minicpm-v:8b

## API Configuration

Required API keys (check before routing):
- MiniMax API: `~/.workbuddy/skills/frontend-dev/scripts/minimax_image.py` (uses env vars)
- Seedream ARK: `~/.workbuddy/skills/picture-book-pipeline/scripts/batch_generate.py`
- buddy-cloud: `connect_cloud_service` tool for token

## Limitations (Honest Disclosure)

The following capabilities are NOT achievable through this bridge:
- **Semantic image understanding**: "What breed is this cat?" — requires a vision model
- **UI screenshot analysis**: "Is this button well-positioned?" — requires visual understanding
- **Style transfer / image editing**: Requires pixel-level operations
- **Real-time video frame understanding**: OCR too slow for real-time

For these, consider deploying a local vision model (MiniCPM-V-2.6, ~8GB) or using GPT-4V/Claude Vision API.

## Output Format

After bridging, always clearly indicate:
```
[多模态桥接] 路径: OCR桥 | 耗时: 1.2s | 提取文字: 234字符
```

## Reference

Load `references/ocr-pipeline.md` for full OCR pipeline documentation.
Load `references/image-gen-api.md` for registered image generation API details.

## Zcode 集成

### τ 角色与贡献

本技能在 Zcode 体系中承担 **executor** 角色，遵循 `skills/shared/zcode/zcode-embedding-standard.md` 标准。

| 指标 | 方向 | 机制 | 目标压缩 |
|------|------|------|---------|
| τ_execute | reduce | 5条桥接路径消除模态转换摩擦力 | 20% |
| τ_cognize | reduce | 自动路由到最优桥接路径 | 10% |

### 质量门禁

- **等级**: standard
- **依据**: `skills/shared/skill-quality-gate.md`
- **执行前**: 输入校验 + 反模式预检（`skills/shared/feedback/anti-patterns.yaml`）
- **执行后**: 输出校验 + 交付判定（三阶段门禁）

### 交叉验证

- **协同技能**: frontend-dev, video-production-pipeline
- **校验协议**: `skills/shared/zcode/zcode-embedding-standard.md` 第 4 节

### 反馈闭环

- **输出触发**: Memory 写入 + τ 快照更新 + 反模式比对（如适用）
- **遵循协议**: `skills/shared/feedback/feedback-loop-protocol.md`

---
*Zcode 嵌入版本: 1.0 | © 版权所有：默笙夏夏の知書房 - 2026-07-09*
