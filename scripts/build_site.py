#!/usr/bin/env python3
"""Generate the static showcase and 28 plugin detail pages."""

from __future__ import annotations

import html
import json
import re
import subprocess
from pathlib import Path

from build_catalog import (
    DOCS,
    PAGES_URL,
    REPO_URL,
    ROOT,
    load_catalog,
    plugin_metadata,
)


PLUGIN_DOCS = DOCS / "plugins"
DOMAIN_ORDER = {d["id"]: i for i, d in enumerate(load_catalog()["domains"])}


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def head(
    title: str,
    description: str,
    canonical: str,
    depth: int = 0,
    page_type: str = "website",
) -> str:
    prefix = "../" * depth
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <link rel="canonical" href="{esc(canonical)}">
  <meta name="theme-color" content="#0a0e17">
  <meta property="og:type" content="{page_type}">
  <meta property="og:site_name" content="CodeBuddy Skills">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(description)}">
  <meta property="og:url" content="{esc(canonical)}">
  <meta property="og:image" content="{PAGES_URL}assets/social-preview.png">
  <meta property="og:image:width" content="1280">
  <meta property="og:image:height" content="640">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(description)}">
  <meta name="twitter:image" content="{PAGES_URL}assets/social-preview.png">
  <link rel="icon" href="{prefix}assets/mark.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{prefix}styles.css">
</head>"""


def header(depth: int = 0, active: str = "") -> str:
    prefix = "../" * depth
    links = [
        ("domains", f"{prefix}#domains", "能力领域"),
        ("plugins", f"{prefix}#plugins", "28 个技能"),
        ("architecture", f"{prefix}#architecture", "架构"),
        ("install", f"{prefix}#install", "安装"),
        ("catalog", f"{prefix}SKILL-CATALOG.html", "完整目录"),
    ]
    nav = "\n".join(
        f'<a class="nav-link{" is-active" if key == active else ""}" href="{href}">{label}</a>'
        for key, href, label in links
    )
    return f"""<a class="skip-link" href="#main">跳到主要内容</a>
<header class="site-header" data-header>
  <div class="shell header-inner">
    <a class="brand" href="{prefix}index.html" aria-label="CodeBuddy Skills 首页">
      <img src="{prefix}assets/mark.svg" alt="" width="34" height="34">
      <span class="brand-copy"><strong>CodeBuddy</strong><span>Skills</span></span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" data-nav-toggle>
      <span></span><span></span><span></span><span class="sr-only">打开菜单</span>
    </button>
    <nav class="site-nav" id="site-nav" data-nav>
      {nav}
      <a class="nav-github" href="{REPO_URL}" target="_blank" rel="noopener">
        <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82A7.4 7.4 0 0 1 8 3.8c.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>
        <span>GitHub</span>
      </a>
    </nav>
  </div>
</header>"""


def footer(depth: int = 0) -> str:
    prefix = "../" * depth
    return f"""<footer class="site-footer">
  <div class="shell footer-grid">
    <div class="footer-brand">
      <a class="brand" href="{prefix}index.html">
        <img src="{prefix}assets/mark.svg" alt="" width="30" height="30">
        <span class="brand-copy"><strong>CodeBuddy</strong><span>Skills</span></span>
      </a>
      <p>不是更多提示词，而是可发现、可安装、可验证的专业工作流。</p>
      <p class="muted">28 个插件 · 7 大领域 · MIT / Apache-2.0</p>
    </div>
    <div>
      <h3>产品</h3>
      <a href="{prefix}#domains">能力领域</a>
      <a href="{prefix}#plugins">技能目录</a>
      <a href="{prefix}SKILL-CATALOG.html">完整索引</a>
      <a href="{prefix}INSTALL.html">安装指南</a>
    </div>
    <div>
      <h3>工程</h3>
      <a href="{prefix}ARCHITECTURE.html">架构设计</a>
      <a href="{prefix}BENCHMARK.html">高星项目对标</a>
      <a href="{prefix}QUALITY.html">质量门禁</a>
      <a href="{prefix}#install">30 秒安装</a>
    </div>
    <div>
      <h3>社区</h3>
      <a href="{REPO_URL}" target="_blank" rel="noopener">GitHub 仓库</a>
      <a href="{REPO_URL}/issues" target="_blank" rel="noopener">问题反馈</a>
      <a href="{REPO_URL}/blob/main/CONTRIBUTING.md" target="_blank" rel="noopener">贡献指南</a>
      <a href="{REPO_URL}/releases" target="_blank" rel="noopener">版本发布</a>
    </div>
  </div>
  <div class="shell footer-bottom">
    <span>© 2026 Vane · CodeBuddy Skills</span>
    <span>Built as an open, auditable Agent Skills catalog.</span>
  </div>
</footer>
<script src="{prefix}app.js" defer></script>
</body>
</html>"""


def plugin_card(plugin: dict, domain: dict) -> str:
    tags = "".join(f'<span class="tag">{esc(t)}</span>' for t in plugin["tags"][:3])
    return f"""<article class="plugin-card reveal" data-plugin data-domain="{plugin['domain']}" data-search="{esc((plugin['title'] + ' ' + plugin['name'] + ' ' + plugin['tagline'] + ' ' + plugin['summary'] + ' ' + ' '.join(plugin['tags'])).lower())}">
  <div class="plugin-card-top">
    <span class="domain-mark" style="--domain:{domain['color']}">{domain['icon']}</span>
    <span class="plugin-domain">{esc(domain['name'])}</span>
    <span class="plugin-arrow" aria-hidden="true">↗</span>
  </div>
  <h3><a href="plugins/{plugin['name']}.html">{esc(plugin['title'])}</a></h3>
  <p class="plugin-tagline">{esc(plugin['tagline'])}</p>
  <p class="plugin-summary">{esc(plugin['summary'])}</p>
  <div class="tag-row">{tags}</div>
  <div class="plugin-card-foot">
    <code>{esc(plugin['name'])}</code>
    <a href="plugins/{plugin['name']}.html" aria-label="查看 {esc(plugin['title'])} 详情">查看详情</a>
  </div>
</article>"""


def home(data: dict, metadata: dict[str, dict]) -> str:
    domains = data["domains"]
    plugins = data["plugins"]
    domain_by_id = {d["id"]: d for d in domains}

    domain_cards = "\n".join(
        f"""<a class="domain-card reveal" href="#plugins" data-domain-jump="{d['id']}" style="--domain:{d['color']}">
  <span class="domain-symbol">{d['icon']}</span>
  <span class="domain-count">{d['count']:02d}</span>
  <h3>{esc(d['name'])}</h3>
  <p>{esc(d['description'])}</p>
  <span class="domain-link">查看该领域 →</span>
</a>"""
        for d in domains
    )

    chips = '<button class="chip is-active" type="button" data-filter="all">全部 <span>28</span></button>\n' + "\n".join(
        f'<button class="chip" type="button" data-filter="{d["id"]}">{d["icon"]} {esc(d["name"])} <span>{d["count"]}</span></button>'
        for d in domains
    )

    cards = "\n".join(plugin_card(p, domain_by_id[p["domain"]]) for p in plugins)

    domain_rows = "\n".join(
        f"""<div class="map-row">
  <div class="map-label"><span style="--domain:{d['color']}">{d['icon']}</span><strong>{esc(d['name'])}</strong><em>{d['count']} 个</em></div>
  <p>{esc(d['description'])}</p>
  <div class="map-names">{' '.join(f'<span>{esc(p["title"])}</span>' for p in plugins if p['domain']==d['id'])}</div>
</div>"""
        for d in domains
    )

    body = f"""{head("CodeBuddy Skills · 28 个可安装的 AI Agent 技能", "把专业工作交给可验证的 Agent。28 个可安装技能，覆盖财务 BP、税务风控、合同审查、知识蒸馏、内容生产与工程护栏。", PAGES_URL, 0)}
<body class="page-home">
{header(0, "domains")}
<main id="main">
  <section class="hero">
    <div class="hero-grid-bg" aria-hidden="true"></div>
    <div class="hero-glow hero-glow-a" aria-hidden="true"></div>
    <div class="hero-glow hero-glow-b" aria-hidden="true"></div>
    <div class="shell hero-inner">
      <div class="hero-copy">
        <p class="eyebrow reveal"><span class="pulse"></span> OPEN AGENT SKILLS · 2026</p>
        <h1 class="reveal">把专业工作<br><span class="gradient-text">交给可验证的 Agent。</span></h1>
        <p class="hero-lede reveal">28 个可安装技能，把财务 BP、税务风控、合同审查、知识蒸馏、内容生产与工程护栏，变成有输入、有流程、有交付物的专业工作流。</p>
        <div class="hero-actions reveal">
          <a class="button button-primary" href="#install"><span>30 秒安装</span><span aria-hidden="true">→</span></a>
          <a class="button button-ghost" href="#plugins">浏览 28 个技能</a>
        </div>
        <ul class="hero-proof reveal">
          <li><span>28</span> 独立插件</li>
          <li><span>7</span> 能力领域</li>
          <li><span>5</span> 层架构</li>
          <li><span>100%</span> 文档覆盖</li>
        </ul>
      </div>
      <div class="hero-visual reveal">
        <div class="terminal-card">
          <div class="terminal-bar"><i></i><i></i><i></i><span>codebuddy — skills</span></div>
          <div class="terminal-body">
            <p><span class="prompt">$</span> /plugin marketplace add Vane1981-2011/codebuddy-plugins</p>
            <p class="dim">→ marketplace synced · 28 plugins</p>
            <p><span class="prompt">$</span> /plugin install financial-bp-command-center</p>
            <p class="dim">→ skill enabled · README + contract loaded</p>
            <p class="success">✓ ready · 描述任务，或输入 /financial-bp-command-center</p>
          </div>
        </div>
        <div class="hero-note">
          <span class="note-icon">✦</span>
          <div><strong>一个插件 = 一个可交付工作流</strong><p>不是提示词集合。每个插件都说明问题、输入、输出、执行步骤和不适用边界。</p></div>
        </div>
        <div class="orbit orbit-a" aria-hidden="true"></div>
        <div class="orbit orbit-b" aria-hidden="true"></div>
      </div>
    </div>
    <div class="shell scroll-cue"><span></span>向下查看能力地图</div>
  </section>

  <section class="section section-tight" id="domains">
    <div class="shell">
      <div class="section-head reveal">
        <p class="eyebrow">THE CAPABILITY MAP</p>
        <h2>7 个领域，覆盖从思考到交付的完整链路。</h2>
        <p>先选择工作场景，再选择插件。每个领域都能独立使用，也能组合成端到端工作流。</p>
      </div>
      <div class="domain-grid">{domain_cards}</div>
      <div class="map-panel reveal">
        <div class="map-panel-head"><span>领域 → 插件</span><span>7 DOMAINS / 28 PLUGINS</span></div>
        {domain_rows}
      </div>
    </div>
  </section>

  <section class="section" id="why">
    <div class="shell">
      <div class="split-head">
        <div class="section-head reveal">
          <p class="eyebrow">WHY THIS REPO</p>
          <h2>不是更多提示词。<br>是更少但更完整的交付单元。</h2>
        </div>
        <p class="split-aside reveal">大多数技能仓库给你一堆 Markdown。这里给你 28 个可以被发现、被安装、被验证、被复用的工作流产品。</p>
      </div>
      <div class="value-grid">
        <article class="value-card reveal"><span class="value-num">01</span><h3>可发现</h3><p>按领域、问题、输入和输出来组织，而不是按文件名字母排序。你能在 30 秒内判断一个插件是否适合当前任务。</p></article>
        <article class="value-card reveal"><span class="value-num">02</span><h3>可安装</h3><p>统一市场清单、插件清单与技能目录。一条命令添加市场，一条命令安装插件，不依赖手工复制文件。</p></article>
        <article class="value-card reveal"><span class="value-num">03</span><h3>可验证</h3><p>每个插件都有独立 README、执行契约、质量边界和版本记录。CI 校验 28/28 一致性与技能可加载状态。</p></article>
      </div>
    </div>
  </section>

  <section class="section section-contrast" id="plugins">
    <div class="shell">
      <div class="section-head reveal">
        <p class="eyebrow">THE CATALOG</p>
        <h2>28 个技能，按 7 大领域组织。</h2>
        <p>搜索任务、技术或场景关键词，或按领域筛选。每个卡片都指向独立详情页。</p>
      </div>
      <div class="catalog-tools reveal">
        <div class="search-box">
          <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><path d="m20 20-3.5-3.5"></path></svg>
          <input type="search" placeholder="搜索技能、场景或关键词…" aria-label="搜索技能" data-search-input>
          <kbd>/</kbd>
        </div>
        <div class="chip-row" data-filter-row>{chips}</div>
      </div>
      <p class="result-line" data-result-line>显示全部 28 个技能</p>
      <div class="plugin-grid" data-plugin-grid>{cards}</div>
      <div class="empty-state" data-empty hidden><strong>没有匹配的技能</strong><p>换个关键词，或点击“全部”查看 28 个插件。</p></div>
    </div>
  </section>

  <section class="section" id="architecture">
    <div class="shell">
      <div class="split-head">
        <div class="section-head reveal">
          <p class="eyebrow">SYSTEM ARCHITECTURE</p>
          <h2>五层架构，把“技能”变成可运营的产品。</h2>
        </div>
        <p class="split-aside reveal">从市场发现到执行契约，再到质量证据与分发快照，每一层都有明确的职责和可检查的产物。</p>
      </div>
      <div class="architecture reveal">
        <div class="arch-layer" style="--layer:#8fb0ff"><span class="arch-index">L0</span><div><h3>市场与发现层</h3><p>README、领域地图、搜索、独立详情页、SEO / OG / Sitemap。</p></div><span class="arch-out">被看见</span></div>
        <div class="arch-layer" style="--layer:#67d6c4"><span class="arch-index">L1</span><div><h3>能力目录层</h3><p>catalog/plugins.json 作为单一事实源，统一 7 领域、28 插件、标签与许可。</p></div><span class="arch-out">被理解</span></div>
        <div class="arch-layer" style="--layer:#f4b860"><span class="arch-index">L2</span><div><h3>执行契约层</h3><p>SKILL.md 定义触发、输入、流程、输出与不适用边界；plugin.json 定义安装单元。</p></div><span class="arch-out">被使用</span></div>
        <div class="arch-layer" style="--layer:#f472b6"><span class="arch-index">L3</span><div><h3>质量与证据层</h3><p>质量门禁、专业边界、来源说明、版本记录和 CI 一致性检查。</p></div><span class="arch-out">被信任</span></div>
        <div class="arch-layer" style="--layer:#a78bfa"><span class="arch-index">L4</span><div><h3>分发与快照层</h3><p>marketplace、Release 包、Pages 展示站、变更日志和可迁移的目录快照。</p></div><span class="arch-out">被分发</span></div>
      </div>
      <div class="arch-foot reveal"><span>单一事实源</span><span class="arch-arrow">→</span><span>自动生成</span><span class="arch-arrow">→</span><span>自动校验</span><span class="arch-arrow">→</span><span>一次发布</span></div>
    </div>
  </section>

  <section class="section section-tight" id="delivery">
    <div class="shell">
      <div class="section-head reveal"><p class="eyebrow">EXECUTION CONTRACT</p><h2>每次调用，都走同一条交付路径。</h2></div>
      <div class="steps">
        <article class="step reveal"><span>01</span><h3>确认目标</h3><p>明确要做的决定、交付物和验收标准，避免在错误问题上高效输出。</p></article>
        <article class="step reveal"><span>02</span><h3>收集最小输入</h3><p>只要求真正影响结论的事实、数据与约束；缺失时先提问，而不是编造。</p></article>
        <article class="step reveal"><span>03</span><h3>按流程执行</h3><p>用领域方法、计算逻辑和质量门禁，把任务拆成可检查的步骤。</p></article>
        <article class="step reveal"><span>04</span><h3>交付与留痕</h3><p>输出结构化结果，同时保留假设、来源、未决问题和下一步动作。</p></article>
      </div>
    </div>
  </section>

  <section class="section" id="quality">
    <div class="shell">
      <div class="quality-grid">
        <div class="section-head reveal"><p class="eyebrow">QUALITY GATES</p><h2>可被信任，来自可被检查。</h2><p>我们不为“看起来很强”写更多形容词，而是把发布条件写进仓库，让每次提交都能被验证。</p><a class="text-link" href="QUALITY.html">查看完整质量门禁 →</a></div>
        <div class="quality-list">
          <div class="quality-item reveal"><strong>28 / 28</strong><div><h3>独立插件文档</h3><p>每个插件都有 README、安装命令、输入输出与适用边界。</p></div></div>
          <div class="quality-item reveal"><strong>28 / 28</strong><div><h3>技能默认启用</h3><p>修复 disable 状态，安装后可直接加载，不需要改文件。</p></div></div>
          <div class="quality-item reveal"><strong>1 : 1</strong><div><h3>目录与市场一致</h3><p>catalog、marketplace、plugin.json 与磁盘目录四方一致。</p></div></div>
          <div class="quality-item reveal"><strong>0</strong><div><h3>占位符与断链</h3><p>CI 检查 JSON、YAML、链接、截图与发布包完整性。</p></div></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section-install" id="install">
    <div class="shell install-grid">
      <div class="section-head reveal"><p class="eyebrow">GET STARTED</p><h2>30 秒，把第一个专业工作流装进你的 Agent。</h2><p>适用于支持 CodeBuddy 插件市场的宿主。技能层遵循 Agent Skills 约定。</p></div>
      <div class="install-steps reveal">
        <div class="install-step"><span>01</span><div><h3>添加市场</h3><pre><code>/plugin marketplace add Vane1981-2011/codebuddy-plugins</code><button class="copy" type="button" data-copy>复制</button></pre></div></div>
        <div class="install-step"><span>02</span><div><h3>安装插件</h3><pre><code>/plugin install financial-bp-command-center</code><button class="copy" type="button" data-copy>复制</button></pre></div></div>
        <div class="install-step"><span>03</span><div><h3>直接描述任务</h3><pre><code>用财务 BP 视角分析 Q4 渠道预算，输出差异原因和调整建议。</code><button class="copy" type="button" data-copy>复制</button></pre></div></div>
        <a class="text-link" href="INSTALL.html">查看安装、排错与宿主说明 →</a>
      </div>
    </div>
  </section>

  <section class="section star-section">
    <div class="shell star-card reveal">
      <div><p class="eyebrow">OPEN SOURCE</p><h2>如果这些工作流对你有用，<br>给它一个 Star。</h2><p>Star 不会让技能变强，但会让下一个需要它的人更容易找到这里。</p></div>
      <div class="star-actions"><a class="button button-primary" href="{REPO_URL}" target="_blank" rel="noopener">在 GitHub 上 Star <span>★</span></a><a class="button button-ghost" href="{REPO_URL}/releases" target="_blank" rel="noopener">下载 v1.0.0</a></div>
    </div>
  </section>
</main>
{footer(0)}"""
    return body


def detail(plugin: dict, domain: dict, meta: dict, related: list[dict], domain_by_id: dict) -> str:
    workflow = "\n".join(
        f"""<li class="flow-item reveal"><span>{i:02d}</span><div><h3>{esc(step.split('；')[0].strip())}</h3><p>{esc(step)}</p></div></li>"""
        for i, step in enumerate(plugin["workflow"], 1)
    )
    tags = "".join(f'<span class="tag">{esc(t)}</span>' for t in plugin["tags"])
    related_cards = "\n".join(
        f"""<a class="related-card" href="{p['name']}.html"><span>{esc(domain_by_id[p['domain']]['icon'])}</span><div><strong>{esc(p['title'])}</strong><p>{esc(p['tagline'])}</p></div><i>→</i></a>"""
        for p in related
    )
    install = f"/plugin marketplace add Vane1981-2011/codebuddy-plugins\n/plugin install {plugin['name']}"
    json_ld = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "SoftwareApplication",
            "name": plugin["title"],
            "alternateName": plugin["name"],
            "description": plugin["summary"],
            "applicationCategory": "DeveloperApplication",
            "operatingSystem": "Web",
            "url": f"{PAGES_URL}plugins/{plugin['name']}.html",
            "codeRepository": f"{REPO_URL}/tree/main/plugins/{plugin['name']}",
            "license": f"{REPO_URL}/blob/main/LICENSE",
            "author": {"@type": "Person", "name": "Vane1981", "url": "https://github.com/Vane1981-2011"},
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "CNY"},
        },
        ensure_ascii=False,
    )
    body = f"""{head(f"{plugin['title']} · CodeBuddy Skills", plugin['summary'], f"{PAGES_URL}plugins/{plugin['name']}.html", 1, "article")}
<body class="page-detail">
{header(1, "plugins")}
<main id="main">
  <section class="detail-hero">
    <div class="detail-glow" style="--domain:{domain['color']}" aria-hidden="true"></div>
    <div class="shell">
      <nav class="breadcrumb" aria-label="面包屑"><a href="../index.html">首页</a><span>/</span><a href="../index.html#plugins">技能目录</a><span>/</span><span>{esc(plugin['title'])}</span></nav>
      <div class="detail-hero-grid">
        <div>
          <div class="detail-kicker"><span class="domain-mark" style="--domain:{domain['color']}">{domain['icon']}</span><span>{esc(domain['name'])} · {esc(domain['name_en'])}</span><span class="version-pill">v{esc(meta['version'])}</span></div>
          <h1 class="reveal">{esc(plugin['title'])}</h1>
          <p class="detail-tagline reveal">{esc(plugin['tagline'])}</p>
          <p class="detail-summary reveal">{esc(plugin['summary'])}</p>
          <div class="tag-row reveal">{tags}</div>
        </div>
        <aside class="install-card reveal">
          <p class="install-card-label">安装这个插件</p>
          <pre><code>{esc(install)}</code><button class="copy" type="button" data-copy>复制命令</button></pre>
          <div class="install-meta"><span><i></i> MIT / Apache-2.0</span><span><i></i> 独立可安装</span><span><i></i> 含执行契约</span></div>
          <a class="text-link" href="{REPO_URL}/tree/main/plugins/{plugin['name']}" target="_blank" rel="noopener">查看源文件 →</a>
        </aside>
      </div>
    </div>
  </section>

  <section class="section section-tight">
    <div class="shell">
      <div class="triad">
        <article class="triad-card reveal"><span>PROBLEM</span><h2>解决什么问题</h2><p>{esc(plugin['problem'])}</p></article>
        <article class="triad-card reveal"><span>INPUT</span><h2>最小输入</h2><p>{esc(plugin['input'])}</p></article>
        <article class="triad-card reveal"><span>OUTPUT</span><h2>主要输出</h2><p>{esc(plugin['output'])}</p></article>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="shell detail-columns">
      <div>
        <div class="section-head compact reveal"><p class="eyebrow">WORKFLOW</p><h2>它如何工作</h2></div>
        <ol class="flow-list">{workflow}</ol>
      </div>
      <aside class="detail-aside">
        <div class="aside-card reveal"><p class="eyebrow">EXAMPLE</p><h3>可以这样调用</h3><pre class="example-code"><code>{esc(plugin['example'])}</code><button class="copy" type="button" data-copy>复制</button></pre></div>
        <div class="aside-card aside-warning reveal"><p class="eyebrow">NOT FOR</p><h3>什么时候不要用</h3><p>{esc(plugin['not_for'])}</p></div>
        <div class="aside-card reveal"><p class="eyebrow">CONTRACT</p><h3>交付契约</h3><ul class="check-list"><li>执行前确认目标、约束和最小输入</li><li>关键结论保留假设、来源与验收记录</li><li>专业判断标注边界，需持证人士复核</li><li>版本与变更记录可追溯</li></ul></div>
      </aside>
    </div>
  </section>

  <section class="section section-contrast">
    <div class="shell">
      <div class="section-head reveal"><p class="eyebrow">SAME DOMAIN</p><h2>同领域的其他插件</h2><p>可以单独使用，也可以与 {esc(plugin['title'])} 组合成更完整的流程。</p></div>
      <div class="related-grid">{related_cards}</div>
    </div>
  </section>

  <section class="section">
    <div class="shell detail-bottom reveal">
      <div><p class="eyebrow">OPEN SOURCE</p><h2>可读、可改、可验证。</h2><p>插件源文件、执行说明与变更记录都在仓库中。发现问题或有更好的做法，欢迎提交 Issue 或 PR。</p></div>
      <div class="hero-actions"><a class="button button-primary" href="{REPO_URL}" target="_blank" rel="noopener">打开 GitHub 仓库</a><a class="button button-ghost" href="../index.html#plugins">继续浏览</a></div>
    </div>
  </section>
</main>
{footer(1)}
<script type="application/ld+json">{json_ld}</script>"""
    return body


def catalog_page(data: dict, metadata: dict[str, dict]) -> str:
    domain_by_id = {d["id"]: d for d in data["domains"]}
    sections = []
    for domain in data["domains"]:
        rows = "\n".join(
            f"""<tr><td><a href="plugins/{p['name']}.html">{esc(p['title'])}</a><br><code>{esc(p['name'])}</code></td><td>{esc(p['tagline'])}</td><td>{esc(p['input'])}</td><td>{esc(p['output'])}</td><td><code>v{esc(metadata[p['name']]['version'])}</code></td></tr>"""
            for p in data["plugins"] if p["domain"] == domain["id"]
        )
        sections.append(
            f"""<section class="catalog-section" id="{domain['id']}"><div class="catalog-section-head"><span class="domain-mark" style="--domain:{domain['color']}">{domain['icon']}</span><div><h2>{esc(domain['name'])}</h2><p>{esc(domain['description'])} · {domain['count']} 个插件</p></div></div><div class="table-wrap"><table><thead><tr><th>插件</th><th>一句话</th><th>最小输入</th><th>主要输出</th><th>版本</th></tr></thead><tbody>{rows}</tbody></table></div></section>"""
        )
    body = f"""{head("完整技能目录 · CodeBuddy Skills", "28 个可安装 AI Agent 技能的完整索引，按 7 大领域组织，包含输入、输出与版本信息。", f"{PAGES_URL}SKILL-CATALOG.html", 0)}
<body class="page-catalog">
{header(0, "catalog")}
<main id="main">
  <section class="subpage-hero"><div class="shell"><p class="eyebrow">FULL INDEX</p><h1>完整技能目录</h1><p>28 个插件，7 大领域。每个条目都可以进入独立详情页，查看问题、输入、输出、流程和安装方式。</p></div></section>
  <div class="shell catalog-body">
    <nav class="catalog-toc">{' '.join(f'<a href="#{d["id"]}">{d["icon"]} {esc(d["name"])} <span>{d["count"]}</span></a>' for d in data["domains"])}</nav>
    {''.join(sections)}
  </div>
</main>
{footer(0)}"""
    return body


def markdown_page(title: str, subtitle: str, body_html: str, active: str = "") -> str:
    return f"""{head(f"{title} · CodeBuddy Skills", subtitle, f"{PAGES_URL}{active}.html", 0)}
<body class="page-doc">
{header(0, "")}
<main id="main">
  <section class="subpage-hero"><div class="shell"><p class="eyebrow">DOCUMENTATION</p><h1>{esc(title)}</h1><p>{esc(subtitle)}</p></div></section>
  <article class="shell prose">{body_html}</article>
</main>
{footer(0)}"""


def markdown_to_html(path: Path) -> str:
    """Render a docs page with pandoc, dropping the duplicate page title."""
    result = subprocess.run(
        ["pandoc", "-f", "gfm", "-t", "html5", "--no-highlight", str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    fragment = result.stdout
    fragment = re.sub(r"^\s*<h1[^>]*>.*?</h1>\s*", "", fragment, count=1, flags=re.S)
    fragment = re.sub(
        r"(<table>.*?</table>)",
        r'<div class="table-wrap">\1</div>',
        fragment,
        flags=re.S,
    )
    return fragment


def main() -> None:
    data = load_catalog()
    metadata = plugin_metadata(data)
    DOCS.mkdir(exist_ok=True)
    PLUGIN_DOCS.mkdir(exist_ok=True)
    domain_by_id = {d["id"]: d for d in data["domains"]}

    (DOCS / "index.html").write_text(home(data, metadata), encoding="utf-8")
    for plugin in data["plugins"]:
        related = [
            p for p in data["plugins"]
            if p["domain"] == plugin["domain"] and p["name"] != plugin["name"]
        ][:4]
        (PLUGIN_DOCS / f"{plugin['name']}.html").write_text(
            detail(plugin, domain_by_id[plugin["domain"]], metadata[plugin["name"]], related, domain_by_id),
            encoding="utf-8",
        )
    (DOCS / "SKILL-CATALOG.html").write_text(catalog_page(data, metadata), encoding="utf-8")
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")

    doc_pages = {
        "ARCHITECTURE": (
            "架构设计",
            "五层架构，把 28 个技能组织成可发现、可安装、可执行、可验证、可分发的产品。",
        ),
        "BENCHMARK": (
            "高星项目对标",
            "拆解 7 个高星 Agent Skills 仓库的结构共性，并说明本仓库如何落地。",
        ),
        "QUALITY": (
            "质量门禁",
            "六道发布门禁、28/28 覆盖标准、专业边界与问题分级。",
        ),
        "INSTALL": (
            "安装指南",
            "两条命令完成市场订阅与插件安装，并验证技能可用。",
        ),
    }
    for slug, (title, subtitle) in doc_pages.items():
        md_path = DOCS / f"{slug}.md"
        body_html = markdown_to_html(md_path)
        (DOCS / f"{slug}.html").write_text(
            markdown_page(title, subtitle, body_html, slug.lower()),
            encoding="utf-8",
        )

    urls = [PAGES_URL, f"{PAGES_URL}SKILL-CATALOG.html", f"{PAGES_URL}ARCHITECTURE.html", f"{PAGES_URL}BENCHMARK.html", f"{PAGES_URL}QUALITY.html", f"{PAGES_URL}INSTALL.html"]
    urls += [f"{PAGES_URL}plugins/{p['name']}.html" for p in data["plugins"]]
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sitemap += [f"  <url><loc>{u}</loc><lastmod>2026-10-31</lastmod></url>" for u in urls]
    sitemap.append("</urlset>")
    (DOCS / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8")
    (DOCS / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {PAGES_URL}sitemap.xml\n", encoding="utf-8")
    print(f"site built: 1 home, {len(data['plugins'])} detail pages, catalog")


if __name__ == "__main__":
    main()
