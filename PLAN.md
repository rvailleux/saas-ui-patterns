# Build Plan — SaaS Design Patterns Site

## Goal
Multilingual (FR + EN) static site presenting 40 SaaS UI design patterns, deployed on GitHub Pages.

---

## Stack
| Layer | Choice | Reason |
|---|---|---|
| SSG | Eleventy 2.x (11ty) | Zero JS by default, simple data cascade, GitHub Pages compatible |
| CSS | Tailwind CSS 3.x + PostCSS | Utility-first, custom dark theme, no runtime cost |
| Search | Fuse.js (client-side) | No server needed, fuzzy search on 40 patterns |
| Deploy | GitHub Actions → `gh-pages` branch | Automated on push to `main` |

---

## Phases

### Phase 1 — Content parsing
- Write `scripts/parse-content.js`
- Reads `content.md`, outputs `src/_data/patterns.json`
- Each pattern becomes a structured object:
  ```json
  {
    "id": 1,
    "slug": "sidebar-collapsible-icon-rail",
    "category": "navigation",
    "title": { "fr": "...", "en": "..." },
    "what": { "fr": "...", "en": "..." },
    "why": { "fr": "...", "en": "..." },
    "demo": "...",
    "examples": [{ "name": "Linear", "desc": { "fr": "...", "en": "..." } }],
    "guide": [{ "fr": "...", "en": "..." }],
    "pitfalls": [{ "fr": "...", "en": "..." }]
  }
  ```
- Also outputs `src/_data/categories.json`

**English translations strategy:** translate all fields inline in the JSON (no external service). Pattern names + technical terms are already English. Translate: what/why/guide/pitfalls/example descriptions.

---

### Phase 2 — Eleventy config
- `.eleventy.js`: configures input/output dirs, registers filters, runs Tailwind as a build step
- `tailwind.config.js`: dark theme tokens, typography plugin
- `postcss.config.js`: autoprefixer

---

### Phase 3 — Templates

```
src/
  _includes/
    base.njk          ← HTML shell: <head>, sidebar, top bar, script loading
    pattern-card.njk  ← single pattern card component
  _data/
    patterns.json     ← 40 patterns, bilingual
    categories.json   ← 10 categories with slug + labels
    site.json         ← site name, base URL, available locales
  fr/
    index.njk         ← French home (uses base.njk)
  en/
    index.njk         ← English home (uses base.njk)
  index.njk           ← root redirect to /fr/
  assets/
    css/main.css      ← Tailwind @layer directives
    js/app.js         ← sidebar toggle, search, command palette, theme
```

---

### Phase 4 — Design

**Visual language**
- Background: `#0a0a0f` (near-black)
- Surface/cards: `#111118`
- Border: `#1e1e30`
- Accent: `#7c3aed` (violet-600) with violet-400 highlights
- Text: `#e2e8f0` primary, `#64748b` secondary
- Code blocks: `#1a1a2e` bg, monospace font
- Success/pitfall: green `#10b981` / red `#ef4444`

**Layout**
- Sidebar: 240px open → 48px icon-rail collapsed (localStorage state)
- Content area: fluid, max 840px
- Top bar: sticky, language switcher + ⌘K search trigger
- Mobile: sidebar becomes a slide-in drawer

**Pattern cards**
- Number badge + title + category pill
- Expandable sections (what/why/demo/examples/guide/pitfalls)
- Copy button on code/demo blocks
- Anchor link on card header

**Features implemented in JS**
- Sidebar toggle (icon-rail collapse)
- ⌘K / Ctrl+K → command palette with Fuse.js search across all patterns
- Language switcher (FR ↔ EN, preserves current position via anchor)
- Keyboard nav in command palette (↑↓ Enter Esc)
- Smooth scroll to anchors
- Copy-to-clipboard on code blocks

---

### Phase 5 — Deploy pipeline

The site runs on a Raspberry Pi via Docker. Deployment is triggered by pushing to the `deploy` branch.

```
main (protected) → PR → deploy (protected) → deploy-pi.yml → Pi
```

`deploy-pi.yml` SSHes into the Pi and runs `deploy.sh`:
```bash
git fetch origin
git reset --hard origin/deploy
docker compose up --build -d
```

Branch protection is enforced on both `main` and `deploy` (including admins). The `deploy-gate.yml` workflow auto-closes any PR to `deploy` whose source is not `main`.

---

## File creation order
1. `scripts/parse-content.js` + run it → generates `src/_data/patterns.json`
2. `tailwind.config.js`, `postcss.config.js`
3. `src/assets/css/main.css`
4. `src/_includes/base.njk`
5. `src/_includes/pattern-card.njk`
6. `src/fr/index.njk` + `src/en/index.njk` + `src/index.njk`
7. `src/assets/js/app.js`
8. `.github/workflows/deploy.yml`
9. `.gitignore`
10. Test build: `npm run build`
11. Fix any issues, then `npm run dev` for visual check

---

## Open questions / decisions needed
- **Repo name on GitHub**: needed to set `pathPrefix` in `.eleventy.js` correctly (e.g. if repo is `saas-patterns`, Pages URL is `username.github.io/saas-patterns/` and all asset paths need the prefix)
- **Custom domain?** If yes, no prefix needed
- **GitHub username**: needed to configure the `gh-pages` deploy target

---

## What is NOT in scope (for now)
- Individual pages per pattern (single-page with anchors is sufficient)
- Server-side rendering
- CMS integration
- Comments or community features
- Print stylesheet
