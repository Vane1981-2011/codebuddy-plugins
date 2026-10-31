#!/usr/bin/env python3
"""Validate the published catalog, plugin contracts, generated site and links."""

from __future__ import annotations

import json
import re
import struct
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

import yaml


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
CHECKS: list[str] = []
PLACEHOLDERS = ("G-XXXXXXXXXX", "TODO", "TBD", "lorem ipsum", "your-domain.com")


def check(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def ok(message: str) -> None:
    CHECKS.append(message)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        ERRORS.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        return {}


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if not match:
        ERRORS.append(f"{path.relative_to(ROOT)}: missing frontmatter")
        return {}
    try:
        data = yaml.safe_load(match.group(1))
    except Exception as exc:  # noqa: BLE001
        ERRORS.append(f"{path.relative_to(ROOT)}: invalid YAML: {exc}")
        return {}
    if not isinstance(data, dict):
        ERRORS.append(f"{path.relative_to(ROOT)}: frontmatter is not a mapping")
        return {}
    return data


def semver(value: str) -> bool:
    return bool(re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", str(value)))


def png_size(path: Path) -> tuple[int, int] | None:
    try:
        header = path.read_bytes()[:24]
    except OSError:
        return None
    if header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        return None
    return struct.unpack(">II", header[16:24])


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if key in {"href", "src"} and value:
                self.links.append(value)


def validate_links() -> None:
    html_files = list((ROOT / "docs").rglob("*.html"))
    broken: list[str] = []
    for file in html_files:
        parser = LinkParser()
        parser.feed(file.read_text(encoding="utf-8"))
        for link in parser.links:
            if link.startswith(("http://", "https://", "mailto:", "#", "javascript:", "data:")):
                continue
            target = unquote(urlparse(link).path)
            if not target:
                continue
            resolved = (file.parent / target).resolve()
            if not resolved.exists():
                broken.append(f"{file.relative_to(ROOT)} -> {link}")
            if len(broken) >= 20:
                break
    check(not broken, "broken internal links:\n  " + "\n  ".join(broken))
    if not broken:
        ok(f"{len(html_files)} HTML pages, internal links resolve")


def main() -> int:
    catalog_path = ROOT / "catalog" / "plugins.json"
    catalog = load_json(catalog_path)
    plugins = catalog.get("plugins", [])
    domains = catalog.get("domains", [])
    check(len(plugins) == 28, f"catalog must contain 28 plugins, found {len(plugins)}")
    check(len(domains) == 7, f"catalog must contain 7 domains, found {len(domains)}")
    names = [p.get("name") for p in plugins]
    check(len(names) == len(set(names)), "catalog contains duplicate plugin names")

    domain_ids = {d.get("id") for d in domains}
    counts = {d.get("id"): 0 for d in domains}
    for plugin in plugins:
        check(plugin.get("domain") in domain_ids, f"{plugin.get('name')}: unknown domain")
        if plugin.get("domain") in counts:
            counts[plugin["domain"]] += 1
        for key in ("title", "tagline", "summary", "problem", "input", "output", "example", "not_for"):
            check(bool(plugin.get(key)), f"{plugin.get('name')}: missing catalog field {key}")
        check(len(plugin.get("workflow", [])) >= 3, f"{plugin.get('name')}: workflow needs 3+ steps")
        check(bool(plugin.get("tags")), f"{plugin.get('name')}: missing tags")
        check(plugin.get("license") in {"MIT", "Apache-2.0"}, f"{plugin.get('name')}: unsupported license")
    for domain in domains:
        check(
            counts.get(domain.get("id")) == domain.get("count"),
            f"{domain.get('id')}: count {domain.get('count')} != actual {counts.get(domain.get('id'))}",
        )
    check(len(plugins) == 28 and len(domains) == 7 and not any("count" in e for e in ERRORS), "catalog totals mismatch")
    if not ERRORS:
        ok("28 plugins / 7 domains")

    plugin_dirs = sorted(p for p in (ROOT / "plugins").iterdir() if p.is_dir())
    check(len(plugin_dirs) == 28, f"plugins/ must contain 28 directories, found {len(plugin_dirs)}")
    check({p.name for p in plugin_dirs} == set(names), "plugins/ directories do not match catalog names")

    metadata: dict[str, dict] = {}
    for plugin in plugins:
        name = plugin["name"]
        base = ROOT / "plugins" / name
        readme = base / "README.md"
        plugin_json = base / ".codebuddy-plugin" / "plugin.json"
        skill = base / "skills" / name / "SKILL.md"

        check(readme.exists(), f"{name}: missing README.md")
        if readme.exists():
            text = readme.read_text(encoding="utf-8")
            for token in (f"/plugin install {name}", "输入", "输出", "执行流程", "不适用"):
                check(token in text, f"{name}: README missing {token!r}")

        meta = load_json(plugin_json) if plugin_json.exists() else {}
        check(bool(meta), f"{name}: missing or invalid plugin.json")
        if meta:
            metadata[name] = meta
            check(meta.get("name") == name, f"{name}: plugin.json name mismatch")
            check(semver(meta.get("version", "")), f"{name}: invalid version {meta.get('version')!r}")
            check(bool(meta.get("description")), f"{name}: missing plugin.json description")
            check(meta.get("license") in {"MIT", "Apache-2.0"}, f"{name}: plugin.json license mismatch")
            check(f"./skills/{name}" in meta.get("skills", []), f"{name}: plugin.json skills entry mismatch")
            check(str(meta.get("homepage", "")).startswith("https://"), f"{name}: plugin.json homepage missing")

        check(skill.exists(), f"{name}: missing SKILL.md")
        if skill.exists():
            fm = frontmatter(skill)
            check(fm.get("name") == name, f"{name}: SKILL.md name mismatch")
            check(bool(fm.get("description")), f"{name}: SKILL.md description missing")
            check(fm.get("disable") is not True, f"{name}: SKILL.md is disabled")

    ok("28 plugin READMEs, plugin.json files and SKILL.md frontmatter")

    marketplace = load_json(ROOT / ".codebuddy-plugin" / "marketplace.json")
    entries = marketplace.get("plugins", [])
    check(len(entries) == 28, f"marketplace must contain 28 entries, found {len(entries)}")
    entry_by_name = {e.get("name"): e for e in entries}
    check(set(entry_by_name) == set(names), "marketplace names do not match catalog")
    for name in names:
        entry = entry_by_name.get(name, {})
        check(entry.get("source") == f"./plugins/{name}", f"{name}: marketplace source mismatch")
        check((ROOT / "plugins" / name).exists(), f"{name}: marketplace source does not exist")
        if name in metadata:
            check(entry.get("version") == metadata[name].get("version"), f"{name}: marketplace version mismatch")
    if not any("marketplace" in e for e in ERRORS):
        ok("marketplace matches catalog and plugin metadata")

    docs = ROOT / "docs"
    required_docs = [
        "index.html", "styles.css", "app.js", "SKILL-CATALOG.md", "SKILL-CATALOG.html",
        "ARCHITECTURE.html", "BENCHMARK.html", "QUALITY.html", "INSTALL.html",
        "assets/mark.svg", "assets/banner.svg", "assets/screenshot.png",
        "assets/social-preview.svg", "assets/social-preview.png",
        ".nojekyll", "sitemap.xml", "robots.txt",
    ]
    for rel in required_docs:
        check((docs / rel).exists(), f"docs/{rel} missing")
    detail_pages = [docs / "plugins" / f"{name}.html" for name in names]
    check(all(p.exists() for p in detail_pages), "one or more plugin detail pages are missing")
    if all(p.exists() for p in detail_pages):
        ok("28 plugin detail pages")

    screenshot = docs / "assets" / "screenshot.png"
    social = docs / "assets" / "social-preview.png"
    screenshot_size = png_size(screenshot) if screenshot.exists() else None
    social_size = png_size(social) if social.exists() else None
    check(
        bool(screenshot_size and screenshot_size[0] >= 1200 and screenshot_size[1] >= 700),
        "docs/assets/screenshot.png must be a product screenshot of at least 1200x700",
    )
    check(social_size == (1280, 640), "docs/assets/social-preview.png must be exactly 1280x640")
    if screenshot_size and social_size == (1280, 640):
        ok("product screenshot and 1280x640 social preview")

    for file in [ROOT / "README.md", *docs.rglob("*.html"), *[ROOT / "plugins" / n / "README.md" for n in names]]:
        if not file.exists():
            continue
        text = file.read_text(encoding="utf-8")
        for placeholder in PLACEHOLDERS:
            check(placeholder not in text, f"{file.relative_to(ROOT)} contains placeholder {placeholder!r}")

    root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    missing_names = [name for name in names if name not in root_readme]
    check(not missing_names, f"root README missing plugins: {missing_names}")

    for required in ("LICENSE", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md", "CHANGELOG.md", "THIRD_PARTY_NOTICES.md"):
        check((ROOT / required).exists(), f"{required} missing")
    check((ROOT / "plugins" / "jiying" / "LICENSE").exists(), "jiying LICENSE missing")

    infra_files = [
        ".github/workflows/validate.yml",
        ".github/PULL_REQUEST_TEMPLATE.md",
        ".github/ISSUE_TEMPLATE/bug_report.yml",
        ".github/ISSUE_TEMPLATE/skill_request.yml",
        ".github/ISSUE_TEMPLATE/config.yml",
    ]
    for rel in infra_files:
        check((ROOT / rel).exists(), f"{rel} missing")
    for rel in infra_files[2:]:
        path = ROOT / rel
        if path.exists():
            try:
                yaml.safe_load(path.read_text(encoding="utf-8"))
            except Exception as exc:  # noqa: BLE001
                ERRORS.append(f"{rel}: invalid YAML: {exc}")
    workflow = ROOT / ".github" / "workflows" / "validate.yml"
    if workflow.exists():
        workflow_text = workflow.read_text(encoding="utf-8")
        for token in ("scripts/build_catalog.py", "scripts/build_site.py", "scripts/validate_repo.py", "git diff --exit-code"):
            check(token in workflow_text, f"validate.yml missing {token!r}")
    if all((ROOT / rel).exists() for rel in infra_files):
        ok("GitHub CI, Issue forms and PR template")

    validate_links()

    if ERRORS:
        print("VALIDATION FAILED", file=sys.stderr)
        for error in ERRORS:
            print(f"  ✗ {error}", file=sys.stderr)
        return 1
    for line in CHECKS:
        print(f"OK {line}")
    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
