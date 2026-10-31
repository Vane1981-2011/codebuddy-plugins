---
name: "spa-engineering-guard"
description: >
  Engineering guardrails for developing single-file HTML applications with WorkBuddy. Covers regex pitfalls, CSS selector traps, localStorage isolation, Q bank validation, lock/cancel/exit navigation protocols, button icon singularity, color conventions. 单文件HTML应用工程护栏——覆盖正则陷阱、CSS选择器、localStorage隔离、题库验证等。
version: "2.2.0"
agent_created: true
qualityGate: "enhanced"
trigger_recommended:
  - HTML应用开发
  - 单文件应用
  - 工程护栏
  - 正则陷阱
  - SPA开发
  - single-file HTML
  - localStorage
  - 导航协议
  - 按钮规范
trigger_exclusive:
  - 单文件HTML工程
  - SPA工程护栏
anti_triggers:
  - 设计风格
  - 配色方案
  - 数据可视化
dependencies:
  - quality-assessment-expert-system (optional)
supersedes:
zcode:
  version: "1.0"
  τ_role: "gatekeeper"
  τ_impact:
    - {'metric': 'τ_qa', 'direction': 'auto', 'target': 'auto', 'mechanism': '五维工程标准自动门禁'}
    - {'metric': 'τ_execute', 'direction': 'maintain', 'target': '0%', 'mechanism': '防止不良工程实践引入额外τ'}
  bus_compatible: true
  cross_validate_with:
    - frontend-dev
disable: false
last_updated: 2026-07-01
---
# SPA Engineering Guard

Systematic patterns and anti-patterns for developing single-file HTML/JS/CSS applications
with WorkBuddy. Covers edit reliability, state management, CSS architecture, and QA
validation — distilled from repeated debugging cycles on a real-world 50-question math
quiz platform.

## When to Use

Trigger this skill when:

- Making complex multi-location edits to a single HTML file (especially > 100K chars)
- The Edit tool or regex-based `Write` scripts produce syntax errors (extra `}`, broken quotes, missing functions)
- Debugging CSS visibility/display issues with `fixed` nav, tabs, or overlays
- Implementing multi-user localStorage data isolation
- Adding PIN/password authentication to a client-side app
- Running browser-based end-to-end tests via playwright-cli
- Validating a Q bank or content corpus for correctness

## Core Principles

### 1. Edit Tool Integrity Protocol

The Edit tool performs exact string replace. It fails silently or partially when the target string
contains invisible characters, encoding differences, or has been modified by a linter. Follow this
protocol:

- **Read before every Edit.** The file may have been modified by a linter or prior batch script
  since the last Read. Always Read the target lines before editing.
- **Use unique context.** When a string appears multiple times (e.g., `updateStats()`), include
  surrounding lines to make the match unique.
- **Verify after Edit.** After each Edit, Read the modified area to confirm correctness. A brace
  balance check (`{` vs `}` count) catches the most common error.
- **Prefer one Edit per logical change.** Chaining 3+ Edits on a single function is fragile.
  When a function needs a full rewrite, use a Node.js script that reads the file, performs the
  replacement with `String.replace()`, and writes back — then verify with a brace balance check.

### 2. Regex-Based Code Replacement Safety

When using a Node.js script to replace JavaScript functions with regex — **and when performing
multiple sequential Edit operations on the same file across sessions:**

**Cumulative erosion warning:** Each text-level operation on an HTML file containing `<style>`
blocks has a non-zero risk of incidentally trimming adjacent CSS rules. Over 5+ edit sessions,
cumulative loss can render entire CSS rule sets empty. After every 3+ Edit operations, run a
CSS rule count diff against the canonical backup (`grep -c '{' file.html`). If the count drops
by >5%, restore missing CSS from the backup (see pitfalls.md for full protocol).

**Regex patterns:**

```javascript
// DANGEROUS: greedy match that may span multiple functions
const pattern = /function renderStats\(\)\{[\s\S]*?document\.getElementById\('sc2'\)\.innerHTML=[^;]*;\s*\}/;

// SAFER: match specific function boundaries with brace counting
function replaceFunction(html, funcName, newBody) {
  const start = html.indexOf(`function ${funcName}(`);
  if (start < 0) return html;
  let depth = 0, pos = start;
  for (; pos < html.length; pos++) {
    if (html[pos] === '{') depth++;
    if (html[pos] === '}') { depth--; if (depth === 0) break; }
  }
  return html.slice(0, start) + newBody + html.slice(pos + 1);
}
```

Always run brace balance validation after regex-based replacements:

```javascript
let depth = 0;
for (let i = 0; i < html.length; i++) {
  if (html[i] === '{') depth++;
  if (html[i] === '}') depth--;
  if (depth < 0) { console.error('Extra } at position', i); break; }
}
```

### 3. CSS Selector Specificity & Visibility Debugging

When elements should be visible but `getComputedStyle(el).display` is `none`, or rendered but
invisible/unclickable:

**A. Selector Mismatch (Descendant vs Sibling)**

1. Check **DOM hierarchy** — is the element a child or sibling of the controlling selector?
   - `#parent .child` requires `.child` to be inside `#parent`
   - `#parent ~ .sibling` works for subsequent siblings
   - `#parent + .sibling` works only for the immediate next sibling

2. Check **specificity** — `#cv.active .bn { display: flex }` overrides `.bn { display: none }`
   ONLY if `.bn` is a descendant of `#cv.active`.

3. Use browser DevTools `getComputedStyle()` to verify which rule is taking effect.

**B. Active State Color Contrast**

Stateful CSS rules (`.active`, `:active`, `:focus`) must explicitly set BOTH `color` and
`background`. Setting only `background` leaves `color` inherited from ancestors, which may
match the new background → invisible text.

```css
/* BROKEN: color inherited, matches background → invisible */
.filter-btn.active { background: var(--bg-primary); }
/* FIXED */
.filter-btn.active { background: var(--bg-primary); color: var(--text-on-primary); }
```

**C. Physical Occlusion (Stacking Context)**

An element in the DOM with `display:block` may be physically covered by a sibling that paints
on top due to DOM order without explicit `z-index`. Different from display/visibility bugs.
Fix: add `position: relative; z-index: 10` on the occluded element.

**D. Opacity Transition Flicker**

CSS opacity transitions can flash if the baseline `opacity` is `1` and JS toggles via class.
The element renders at full opacity for one frame before transition starts.
Fix: set baseline `opacity: 0` and use `requestAnimationFrame` to sequence the transition.

**Real case:** Bottom nav `.bn` outside `#cv` → `#cv.active .bn` never matched → sibling `~`.

### 4. Multi-User localStorage Isolation

For client-side apps with multiple user accounts:

```
// WRONG: global keys that overwrite
P+'user'          // Last logged-in user wins
P+'progress'      // All users share one progress

// RIGHT: namespaced by user identity
P+'user_'+nickname     // Per-user credentials
P+'progress_'+nickname // Per-user data
P+'locked_'+nickname   // Per-user lockout flags
```

**Critical rules:**
- Never auto-restore `user` from localStorage on page load. Always show the login screen first.
- Reset the in-memory `progress` object to `{towers:{},...}` when registering a new user.
- Always use a `loadProgressFor(nickname)` function that explicitly fetches the right key.
- `saveUserData()` must ONLY write `P+'user_'+nickname`, never a global key.
- When deleting a session (logout/lock), call `localStorage.removeItem(P+'user')` if such
  a key exists, and set `user = null`.

### 5. Content Corpus QA

For Q banks, quiz data, or any structured content arrays:

1. **Validate answer indices** — Every `answerIndex` must be 0-3 (for 4-option questions).
2. **Check for debugging artifacts** — Look for "不对", "不管", "等等", "可能", "再看看" in
   explanation fields. These are signs of unfinished thought processes left in production data.
3. **Verify mathematical correctness** — Spot-check computations. For geometry questions, verify
   coordinates produce the claimed result. For algebra, verify substitution.
4. **Trim explanations** — Explanations longer than 100 characters are usually chatty drafts.
   A good explanation is: formula → substitution → result, in under 80 chars.

### 6. Playwright Eval Constraints

When using `playwright-cli eval`:

- `eval` wraps code in an arrow function: `() => (expression)`. 
- **Cannot** use `var`, `let`, `const`, `for`, or `if` statements in the expression.
- **Can** use ternary operators, `&&`/`||` chains, and single expressions.
- For multi-step operations, use multiple `eval` calls with `sleep 0.3` between them.
- For clicking elements: `eval "document.querySelector('.cls') && document.querySelector('.cls').click()"`
- Never use backtick template strings in eval — the shell interprets them.

### 7. Atomic Edit Boundaries

When an Edit operation fails with "String to replace not found", the file has changed.
Re-read the target area, find the exact current string, and retry. Common causes:

- Line numbers shifted from a previous Edit
- A linter reformatted the file between Reads
- Invisible characters (UTF-8 BOM, non-breaking spaces) in the HTML
- The string being searched is split across multiple lines in the source

### 8. Data Model Field Name Consistency

When a data structure is stored in one function but read/displayed in another,
field name mismatches cause silent `undefined` values with no JS error.

**Protocol:**
1. Define the data model schema with field names explicitly documented
2. When adding new fields to a stored object, grep all read sites for old field references
3. Display functions must test: `if (data.field === undefined) console.error('Missing field')`
4. Never use different names for the same concept across storage and display layers

**Example from this project:**
```javascript
// stored as {q, e} — read as {question, explanation}
// Fix: align both sides to use the same keys
progress.wrongQuestions.push({q: text, e: explanation, options: [...], answer: idx});
// Display: q.q, q.e, q.options, q.answer  (NOT q.question, q.explanation)
```

### 9. Chart.js Canvas Lifecycle Management

When embedding Chart.js in a single-file SPA where charts are re-rendered on state changes
(tab switches, data refreshes, etc.):

```javascript
// Always maintain a reference and destroy before re-creating
let chartInstance = null;
function renderChart(data) {
  if (chartInstance) {
    chartInstance.destroy();
    chartInstance = null;
  }
  const ctx = document.getElementById('myChart').getContext('2d');
  chartInstance = new Chart(ctx, { type: 'bar', data });
}
```

**Rule:** `new Chart(canvas)` will throw `"Canvas is already in use"` if the canvas already
has a Chart instance bound to it. Always destroy first, then create. Never call `new Chart()`
twice on the same canvas element without an intermediate `.destroy()`.

### 10. Multi-Condition State Toggle — Single Update Path

When a UI element's visibility is controlled by multiple boolean conditions across different
event handlers, scattered show/hide logic produces stuck states:

```javascript
// BROKEN: visibility set in 3+ different places
function onAnswer() { ... nextBtn.style.display = 'block'; }
function onLastAnswer() { ... nextBtn.style.display = 'none'; }
function showResult() { ... nextBtn.style.display = 'none'; }

// FIXED: single truth-table function, called from ONE updateUI()
function shouldShowNextButton() {
  return isAnswered && !isLastQuestion && !showingResult && !isLocked;
}
function updateUI() {
  document.getElementById('next-btn').classList.toggle('hidden', !shouldShowNextButton());
  // ... all other UI updates go here
}
```

**Rule:** For every UI element whose visibility depends on state, define exactly one
`shouldShow*()` function and call it from exactly one `updateUI()` function. Never
scatter `style.display` or `classList.toggle` across multiple event handlers.

### 11. Lock/Cancel/Exit Navigation Protocol

When implementing lock-screen with PIN verification in a single-file SPA:

**Lock button (`lS()`)**:
```javascript
function lS(){
  if(!currentUser){location.hash='#login';return}
  // Don't change hash — show overlay over current content
  login-overlay.style.display='flex'
  main.style.display='none'
  login-box-main.style.display='none'  // hide registration form
  login-box-pin.style.display='block'  // show PIN keypad
  // Render user avatar + name card
  // Reset PIN dots
}
```

**Cancel button (`pC()`)**: Must clear session and go to login page, NOT return to main app.
```javascript
function pC(){
  // Clear everything
  currentUser=''; clearAllData();
  localStorage.removeItem(P+'lastUser');
  // Show login form (not main app)
  login-overlay.style.display='flex'
  login-box-pin.style.display='none'
  login-box-main.style.display='block'
  location.replace('#login');  // REPLACE, not hash assignment
}
```

**Exit button (`logout()`)**: Must navigate away and prevent back-button return.
```javascript
function logout(){
  clearSession();
  window.location.replace('https://www.baidu.com');
  // NOT: location.hash='#login' — that allows browser back to previous state
}
```

**Key rule**: Both `pC()` and `logout()` must use `location.replace()` (not `location.hash=`), 
which replaces the current history entry, preventing the browser back button (◀) from 
returning to the previously logged-in page.

### 12. Button Icon Singularity Rule

Each button must contain exactly ONE icon — either an SVG or an emoji, never both:

```html
<!-- WRONG: SVG + emoji duplicate -->
<button>
  <svg>...</svg>
  <span>🔒 锁定</span>  <!-- emoji competes with SVG -->
</button>

<!-- RIGHT: SVG only -->
<button>
  <svg>...</svg>
  <span>锁定</span>  <!-- text only, no emoji -->
</button>
```

**Rule**: After creating any button with an SVG, grep for emoji in the adjacent `<span>` 
and remove any duplicates. This applies to ALL buttons: lock, exit, login, settings, etc.

### 13. Top Bar Button Color Pairing Convention

```
Left button  (lock/secure) → #C23350 / #D9486E  (deep wine red)
Right button (exit/leave)  → #55489D / #6A5ACD  (deep indigo/purple)
```

Apply consistently: button SVG gradient, border color, text color, box-shadow, hover states.
Text color must match border color, not a pale derivative.

### 14. Overlay Display Hierarchy

Login overlay stacking (top to bottom):
```
login-overlay (display:flex → covers everything)
  ├── login-box-main  (display:block → registration form)
  └── login-box-pin   (display:block → PIN keypad + user card)
main (display:block → app content)
```

**Rule**: Only ONE of `login-box-main` or `login-box-pin` is visible at a time. 
When `login-overlay` is flex, `main` must be none. When `main` is block, `login-overlay` must be none.
Always call `getElementById` on all three elements in any state transition to ensure consistency.

### 15. Web Page Title Auto-Matching

When generating a web page, the `<title>` tag must be auto-generated from the project theme:

```
Format: [Core Topic] + [Functional Suffix]
Examples:
  Math → "中考数学知识点大冒险互动学习"
  Physics → "初中物理闯关挑战"
  English → "英语词汇探险互动学习"
```

**Do NOT use**: emoji in title, generic titles like "My App" or "学习平台" alone, 
or `<title>` tags that differ from the page's actual content theme.

The browser automatically reads `<title>` for address bar suggestions and tab labels —
no additional meta tags needed.

### 16. Inline onclick String Escape Protocol

When generating HTML strings in JavaScript with inline `onclick` handlers containing
quoted string parameters, escaping errors silently break ALL JS execution:

```javascript
// WRONG: double backslash inside string literal → SyntaxError
'<span onclick="showWordPopup(\\''+word+'\\')">'

// RIGHT: single escaped quote inside string
'<span onclick="showWordPopup(\''+word+'\')">'

// Pattern: use a helper function
function esc(str) { return str.replace(/'/g, "\\'").replace(/"/g, '&quot;'); }
```

**Rule**: After any edit involving `onclick` with quoted parameters, immediately run
`node --check` on the extracted JS block. This catches invisible escape errors that
`new Function()` would otherwise silently fail on.

### 17. DOM Mutation vs Reference Separation

When a DOM element's content is mutated by one function but referenced by another,
the reference breaks after mutation:

```javascript
// BROKEN: cnEl is INSIDE boxEl — mutation destroys cnEl
<div id="boxX">       // box.innerHTML = '...' replaces everything
  <div class="en">...</div>
  <div id="cnX">...</div> // cnX is DESTROYED by the above mutation
</div>

// FIXED: cnEl is a SIBLING of boxEl — survives mutation
<div id="boxX">
  <div class="en">...</div>
</div>
<div id="cnX">...</div>  // cnX is untouched by box.innerHTML updates
```

**Rule**: Any element whose `getElementById` is called MUST be physically outside
any container whose `innerHTML` is dynamically replaced. Use sibling separation.

### 18. Dynamic Content Pronunciation Sync

When a pronunciation button reads text that may change after initial render,
never cache the text in the `onclick` attribute:

```javascript
// WRONG: text frozen at render time
'<button onclick="speak(\''+originalText+'\')">📢</button>'

// RIGHT: read current text from DOM at click time
'<button onclick="speak(getElementById(\'exBox'+id+'\').textContent)">📢</button>'
```

**Rule**: All pronunciation/speech buttons that operate on mutable content must
read their target text from the DOM at click time, never from a render-time variable.

### 19. Sentence Carousel Pattern

For cycling through a fixed set of example sentences in educational apps:

```javascript
const SENTENCE_POOL = [
  {en: 'Template with {w} placeholder', cn: '含{w}占位符的模板'},
  {en: 'Another {w} example', cn: '另一个{w}示例'},
];
const sentenceIdx = {}; // per-word index tracker

function cycleSentence(wid, word, btn) {
  sentenceIdx[wid] = ((sentenceIdx[wid] || 0) + 1) % SENTENCE_POOL.length;
  const item = SENTENCE_POOL[sentenceIdx[wid]];
  const rendered = item.en.replace(/\{w\}/g, '<b>'+word+'</b>');
  // Update DOM + sync CN translation
  const cnEl = document.getElementById('exCn'+wid);
  if (cnEl) cnEl.textContent = item.cn.replace(/\{w\}/g, cn);
}
```

**Key properties**:
- Cycle, not random — each click goes to the next sentence
- Global refresh resets all indices to 0 (full reset button)
- CN translation synchronized with EN example
- Separated from random "refresh all" functionality

### 20. Vocabulary Expansion Engine

Morphological rule-based vocabulary generation for educational apps:

```javascript
// 18 suffix/prefix rules per core word
const RULES = [
  {suffix:'able', pos:'adj.', cnTpl:'可{cn}的'},
  {suffix:'ment', pos:'n.', cnTpl:'{cn}过程'},
  {suffix:'tion', pos:'n.', cnTpl:'{cn}化'},
  {prefix:'re', pos:'v.', cnTpl:'重新{cn}'},
  // ... 14 more rules
];

function expandVocabulary(coreWords) {
  const expanded = [];
  coreWords.forEach(v => {
    RULES.forEach(rule => {
      const w = rule.prefix ? rule.prefix+v.word : v.word+rule.suffix;
      // Validate: length 3-18, no special chars, no dupes
      if (w.length >= 3 && w.length <= 18 && !/[^a-z\-]/.test(w)) {
        expanded.push(createEntry(w, rule, v));
      }
    });
  });
  return expanded;
}
```

**Cache strategy**: Use versioned localStorage key (`kp_vocabExpanded_v2`) to avoid
stale cached data when rules change.

### 21. Inline SVG Icon Integration

For custom icons in navigation buttons, inline SVG provides pixel-perfect control:

```html
<button class="nav-btn">
  <span class="nav-icon">
    <svg width="16" height="20" viewBox="0 0 28 36" style="vertical-align:middle">
      <!-- SVG content with defs, gradients, filters -->
    </svg>
  </span>
  标签文字
</button>
```

**Rules**:
- SVG dimensions must match sibling emoji character size (16-18px width)
- Use `vertical-align: middle` for baseline alignment with text
- Add `aria-label` for accessibility
- Keep viewBox compact (28×36 for card-shaped icons)
- `<defs>` IDs must be globally unique (namespace with project prefix)

---

### 22. Automated QA Validation Script

After making edits to an SPA HTML file, run the automated QA script to catch common issues:

```bash
python3 <SKILL_DIR>/scripts/qa_html.py <file.html>
```

This checks:
- Brace balance (`{` vs `}` count) in JavaScript blocks
- CSS rule count (detect cumulative erosion)
- onclick string escape issues (double-escaping `\\'`)
- localStorage key namespace violations
- Inline SVG sizing

Exit code 0 = all checks passed. Exit code 1 = issues found, review before delivery.

---

## Result Delivery (v2.0)

### 23. Mandatory present_files After Build

After generating or modifying an HTML application, **always** deliver the result via `present_files`:

```
present_files(["{workspace}/outputs/app.html"])
```

This ensures:
- The HTML file appears as an artifact card in the results panel
- The live preview panel automatically opens for HTML files
- The user can immediately view and interact with the result

### 24. Memory Persistence Protocol

After completing substantive work on an SPA (build, significant edit, bug fix), **must** write a work log:

**Workspace daily log (`{workspace}/.workbuddy/memory/YYYY-MM-DD.md`):**
- Record what was built/modified
- Note any engineering guard patterns that were applied
- Document any new anti-patterns discovered

**Workspace MEMORY.md (`{workspace}/.workbuddy/memory/MEMORY.md`):**
- Persist project conventions, naming rules, CSS variable definitions
- Record field name schemas to prevent future mismatch bugs
- Update when new guard patterns are formalized

**User-level MEMORY.md (`~/.workbuddy/MEMORY.md`):**
- Cross-project preferences (e.g., button color conventions, title format rules)
- Navigation protocol preferences shared across all SPA projects

### 25. Agent-Based Parallel Testing (v2.0)

For complex SPAs with multiple test scenarios, use WorkBuddy's `Agent` tool to run tests in parallel:

```
→ Agent("Test PIN authentication flow", subagent_type="Explore")
→ Agent("Test localStorage isolation across 3 users", subagent_type="Explore")
→ Agent("Validate Q bank for answer index correctness", subagent_type="Explore")
→ Agent("Run CSS visibility audit on all overlays", subagent_type="Explore")
```

Each agent independently tests its scenario using `playwright-cli` and reports findings.
This reduces end-to-end test time by parallelizing independent test suites.

### 26. Deployment to CloudStudio

After final validation, deploy the SPA using WorkBuddy's built-in deployment:

```
workbuddy_cloudstudio_deploy --directory ./outputs --entry app.html
```

Then present the deployment URL:
```
present_files(["https://{sandbox-id}.app.codebuddy.work/app.html"])
```

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v2.1.0 | 2026-06-21 | **[UPGRADE]** Added Rule 22: Automated QA Validation Script (`scripts/qa_html.py`). Renumbered Rules 23-26. Updated changelog. |
| v2.0.0 | 2026-06-17 | **[MAJOR UPGRADE]** Added Rule 23: Mandatory `present_files` after build. Added Rule 24: Memory persistence protocol (3-layer system). Added Rule 25: Agent-based parallel testing. Added Rule 26: CloudStudio deployment workflow. |
| v1.0.0 | — | Initial 21 engineering guard rules distilled from real-world SPA development |

## Zcode 集成

### τ 角色与贡献

本技能在 Zcode 体系中承担 **gatekeeper** 角色，遵循 `skills/shared/zcode/zcode-embedding-standard.md` 标准。

| 指标 | 方向 | 机制 | 目标压缩 |
|------|------|------|---------|
| τ_qa | auto | 五维工程标准自动门禁 | auto |
| τ_execute | maintain | 防止不良工程实践引入额外τ | 0% |

### 质量门禁

- **等级**: enhanced
- **依据**: `skills/shared/skill-quality-gate.md`
- **执行前**: 输入校验 + 反模式预检（`skills/shared/feedback/anti-patterns.yaml`）
- **执行后**: 输出校验 + 交付判定（三阶段门禁）

### 交叉验证

- **协同技能**: frontend-dev
- **校验协议**: `skills/shared/zcode/zcode-embedding-standard.md` 第 4 节

### 反馈闭环

- **输出触发**: Memory 写入 + τ 快照更新 + 反模式比对（如适用）
- **遵循协议**: `skills/shared/feedback/feedback-loop-protocol.md`

---
*Zcode 嵌入版本: 1.0 | © 版权所有：默笙夏夏の知書房 - 2026-07-09*
