# SaaS UI Design Patterns

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Built with Eleventy](https://img.shields.io/badge/Built%20with-Eleventy-black?style=flat&logo=11ty)](https://www.11ty.dev/)
[![Tailwind CSS](https://img.shields.io/badge/Styled%20with-Tailwind%20CSS-38B2AC?style=flat&logo=tailwind-css)](https://tailwindcss.com/)

> A multilingual reference library of modern SaaS UI design patterns, harvested from production software and documented for the community.

[🌐 View Live Site](https://saas-ui-patterns.io) · [📖 Documentation](#quick-start) · [🤝 Contributing](#contributing)

---

## What is this?

This repository documents **40+ UI patterns** commonly found in modern SaaS products. Each pattern includes:

- **Real-world examples** from products like Linear, Notion, Figma, Vercel
- **Interactive demos** you can play with
- **Implementation guides** with practical advice
- **Common pitfalls** to avoid
- **Bilingual content** (French & English)

The patterns are organized into 10 categories covering navigation, layout, commands, data display, feedback, and AI-specific interactions.

---

## Quick Start

### Prerequisites

- [Node.js](https://nodejs.org/) 18+ installed
- npm or yarn

### Installation

```bash
# Clone the repository
git clone https://github.com/rvailleux/saas-ui-patterns.git
cd saas-ui-patterns

# Install dependencies
npm install

# Start the development server
npm run dev
```

Open [http://localhost:8080](http://localhost:8080) in your browser.

### Available Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server with hot reload |
| `npm run build` | Build production site to `_site/` |
| `npm run preview` | Build and preview production build |
| `npm run clean` | Remove build output |

---

## Project Structure

```
saas-ui-patterns/
├── src/
│   ├── _data/
│   │   ├── patterns/          # Pattern metadata (JSON)
│   │   └── demos/             # Interactive demos (HTML + config)
│   ├── _includes/             # Nunjucks templates
│   ├── fr/                    # French pages
│   ├── en/                    # English pages
│   └── assets/                # CSS, JS, images
├── _site/                     # Build output (gitignored)
├── content.md                 # Source content (French)
└── package.json
```

---

## Contributing

We welcome contributions! Whether you're fixing a typo, improving a demo, or adding a new pattern — every contribution helps.

### Using Claude Code (Recommended)

If you have [Claude Code](https://claude.ai/code) installed, two skills are available:

```bash
# Create a new pattern interactively
"I want to add a new pattern"

# Submit your pattern as a PR
"Submit my pattern"
```

### Manual Contribution

1. **Check for duplicates** — Search existing patterns first
2. **Read the guide** — See [HOW_TO_ADD_PATTERN.md](./HOW_TO_ADD_PATTERN.md) for step-by-step instructions
3. **Create your pattern** — You'll need 3 files:
   - `src/_data/patterns/{slug}.json` — Pattern metadata
   - `src/_data/demos/{slug}.html` — Interactive demo
   - `src/_data/demos/{slug}.json` — Demo height config
4. **Test locally** — Run `npm run dev` and verify at `/fr/patterns/{slug}/`
5. **Submit a PR** — Branch naming: `pattern/{slug}`

See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidelines.

### What Makes a Good Pattern

A pattern belongs here if it meets **all three criteria**:

- ✅ **Observed in production** — Seen in at least one real SaaS product
- ✅ **Repeatable** — Solves a recurring problem across different contexts
- ✅ **Describable** — Can explain *why* it works, not just *what* it does

---

## Pattern Categories

| Category | Description | Examples |
|----------|-------------|----------|
| **Navigation & Structure** | Wayfinding and app organization | Sidebar collapsible icon-rail, Breadcrumb dynamique |
| **Layout & Workspace** | Spatial organization and view management | Split view panneau dual, Board vue switcher |
| **Commands & Search** | User input and command execution | Command palette ⌘K, Omnibox unified search |
| **Data & Tables** | Data presentation and manipulation | Column resizing/reordering, Virtual scrolling |
| **Feedback & States** | System status and user feedback | Toast notification undo, Skeleton screens |
| **AI — Access & Invocation** | How users trigger AI features | Floating AI button contextuel, K AI intent |
| **AI — Generation & Editing** | AI content creation interfaces | Ghost text inline autocomplete, Diff view accept/reject |
| **AI — Context & Memory** | Managing AI context | Mentions pour le contexte, Memory préférences utilisateur |
| **AI — Feedback & Control** | Steering AI behavior | Confidence uncertainty signal, Regenerate variantes |
| **AI — Prompt UX** | Prompt design patterns | Prompt templates, Suggested prompts quick actions |

---

## Community

- 💬 **Discussions** — [GitHub Discussions](https://github.com/rvailleux/saas-ui-patterns/discussions) for questions and ideas
- 🐛 **Issues** — [GitHub Issues](https://github.com/rvailleux/saas-ui-patterns/issues) for bug reports
- 🗳️ **Voting** — New patterns go through a 15-day community vote period

### Code of Conduct

This project adheres to a standard code of conduct. Be respectful, constructive, and welcoming to all contributors.

---

## License

[MIT License](./LICENSE) — feel free to use this project for personal or commercial purposes.

---

## Acknowledgments

Thanks to the teams behind the products that inspire these patterns:

- [Linear](https://linear.app) — for command palettes and keyboard UX
- [Notion](https://notion.so) — for flexible block-based editing
- [Figma](https://figma.com) — for real-time collaboration patterns
- [Vercel](https://vercel.com) — for deployment and dashboard UX
- [Claude Code](https://claude.ai/code) — for the skills that power contributor workflows

---

<p align="center">
  Built with ❤️ by the community
</p>
# Batch 31-38
 
