# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Goal

Build a multilingual static website that evangelises modern SaaS UI design patterns, deployed on GitHub Pages. All source content is in `content.md` (French, ~40 patterns across 8 categories).

## Stack Decisions

- **Static site generator**: Eleventy (11ty) — zero-JS by default, no build lock-in
- **Styling**: Tailwind CSS via CDN or PostCSS — keep the design on-trend (glassmorphism, dark-first, fluid type)
- **i18n**: Two locales minimum — `fr` (source) and `en` (translated). Locale switching via URL prefix (`/fr/`, `/en/`)
- **Deployment**: Raspberry Pi via Docker. The `deploy` branch triggers `deploy-pi.yml`, which SSHes into the Pi and runs `deploy.sh` (`docker compose up --build -d`).

## Commands

```bash
npm install          # install deps
npm run dev          # local dev server (http://localhost:8080)
npm run build        # production build → _site/
```

## Content Structure

`content.md` contains 40 patterns grouped into 8 sections:

| # | Section | Patterns |
|---|---------|---------|
| 1 | Navigation & Structure | 1–4 |
| 2 | Layout & Workspace | 5–8 |
| 3 | Commandes & Recherche | 9–12 |
| 4 | Data & Tables | 13–16 |
| 5 | Feedback & États | 17–20 |
| 6 | AI — Accès & Invocation | 21–24 |
| 7 | AI — Génération & Édition | 25–28 |
| 8 | AI — Contexte, Mémoire, Feedback & Prompt UX | 29–40 |

Each pattern card follows the same schema: **Ce que c'est** / **Pourquoi ça marche** / **Démo** (ASCII art) / **Meilleurs exemples** / **Guide d'implémentation** / **Pièges à éviter**.

## Site Architecture

```
src/
  _data/
    patterns.json     # structured content parsed from content.md
    i18n/fr.json      # UI strings in French
    i18n/en.json      # UI strings in English
  _includes/
    base.njk          # HTML shell, meta, nav, theme toggle
    card.njk          # pattern card component
  fr/                 # French pages (index, category pages)
  en/                 # English pages (index, category pages)
  assets/
    css/main.css      # Tailwind + custom design tokens
    js/search.js      # client-side search (Pagefind or Fuse.js)
_site/                # build output (gitignored, deployed to gh-pages)
```

## Design Direction

The site itself must demonstrate the patterns it documents — use them as live examples where possible:
- Sidebar collapsible icon-rail for category navigation
- Command palette (⌘K) for pattern search
- Skeleton screens on initial load
- Sticky breadcrumb showing current section
- Dark mode first, light mode toggle

## Deployment

The site runs on a Raspberry Pi behind nginx, served via Docker.

**Branch flow:**
```
feature/... → PR → main → PR → deploy → Pi (auto)
```

**Branch protection (enforced on admins too):**
- `main`: no direct pushes; requires a reviewed PR to merge
- `deploy`: no direct pushes; only PRs from `main` are accepted (others are auto-closed by `deploy-gate.yml`)

**Triggering a deploy:**
1. Open a PR from `main` → `deploy`
2. Merge it — `deploy-pi.yml` fires automatically
3. The Pi fetches `origin/deploy`, rebuilds the Docker image, and restarts the container

**Secrets required in GitHub repo settings:**
- `DEPLOY_HOST`, `DEPLOY_USER`, `DEPLOY_SSH_KEY`, `DEPLOY_PORT`

## GitHub Actions workflows

| File | Trigger | Purpose |
|---|---|---|
| `pattern-pr.yml` | PR opened to `main` | Validates branch name + required files, opens vote |
| `vote-monitor.yml` | Daily 09:00 UTC | Closes expired vote periods, tags owner |
| `deploy-pi.yml` | Push to `deploy` | SSHes to Pi, runs `deploy.sh` |
| `deploy-gate.yml` | PR opened to `deploy` | Auto-closes PRs whose source is not `main` |
| `setup-labels.yml` | Manual dispatch | Creates/updates all GitHub labels (run once) |
