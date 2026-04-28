# Contributing to SaaS UI Design Patterns

Thank you for helping grow this reference. Every pattern added here has been seen in the wild, battle-tested by real products, and is worth documenting for the community.

---

## Before you submit

**Check for duplicates first.**

1. Browse the live site or the `src/_data/patterns/` directory to see all 40+ existing patterns.
2. Search open pull requests: `https://github.com/rvailleux/saas-ui-patterns/pulls`
3. Search open issues: `https://github.com/rvailleux/saas-ui-patterns/issues`

If the pattern already exists or has been proposed in the last 6 months, add a 👍 reaction to the existing issue instead of opening a new one.

---

## What makes a pattern worth submitting

A pattern belongs here if it meets **all three criteria**:

- **Observed in production** — you have seen it in at least one real SaaS product (not just a Dribbble shot).
- **Repeatable** — it solves a recurring problem across different product contexts, not a one-off design decision.
- **Describable** — you can explain *why* it works, not just *what* it does.

Patterns that are too generic ("use a button"), too niche (specific to one company's branding), or purely aesthetic (colour choices, border radius) will not be accepted.

---

## How to submit a pattern candidature

### 1. Fork and clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/saas-ui-patterns.git
cd saas-ui-patterns
npm install
npm run dev
```

### 2. Create the three pattern files

Every pattern lives in three files. Replace `{slug}` with a lowercase, hyphen-separated identifier (e.g. `sticky-column-header`).

#### `src/_data/patterns/{slug}.json`

The full metadata for your pattern. Copy and fill in the template below — **all fields marked \* are mandatory**.

```json
{
  "id": 999,
  "slug": "{slug}",
  "category": "navigation",
  "title": {
    "fr": "Titre en français *",
    "en": "English title *"
  },
  "categoryLabel": {
    "slug": "navigation",
    "fr": "Navigation & Structure",
    "en": "Navigation & Structure"
  },
  "firstSeenOn": {
    "product": "Notion *",
    "url": "https://notion.so",
    "approximateDate": "2023"
  },
  "examples": [
    {
      "name": "Product name *",
      "desc": {
        "fr": "Description courte de l'implémentation",
        "en": "Short description of the implementation"
      }
    },
    {
      "name": "Second product",
      "desc": {
        "fr": "...",
        "en": "..."
      }
    }
  ],
  "guide": {
    "fr": [
      "**Point 1** : conseil d'implémentation concret.",
      "**Point 2** : autre conseil."
    ],
    "en": [
      "**Point 1**: concrete implementation advice.",
      "**Point 2**: another tip."
    ]
  },
  "pitfalls": {
    "fr": [
      "❌ Erreur commune à éviter",
      "❌ Autre piège"
    ],
    "en": [
      "❌ Common mistake to avoid",
      "❌ Another pitfall"
    ]
  }
}
```

**Category must be one of:**

| Value | Label |
|---|---|
| `navigation` | Navigation & Structure |
| `layout` | Layout & Workspace |
| `commands` | Commandes & Recherche |
| `data` | Data & Tables |
| `feedback` | Feedback & États |
| `ai-access` | AI — Accès & Invocation |
| `ai-generation` | AI — Génération & Édition |
| `ai-context` | AI — Contexte & Mémoire |
| `ai-feedback` | AI — Feedback & Contrôle |
| `ai-prompt` | AI — Prompt UX |

**For the `id` field:** use any 3-digit number starting with `9` (e.g. `901`) — the maintainer will assign the final sequential ID on merge.

---

#### `src/_data/demos/{slug}.html`

A self-contained, interactive HTML demo of the pattern. This renders in an iframe on the pattern page.

Requirements:
- Must be a **single HTML file** (no external dependencies except inline JS/CSS).
- Use a dark background (`background: #0f0f1a`) to match the site aesthetic.
- Must be **interactive** — clicking, toggling, or animating something.
- Keep it under **200 lines** of minified HTML.
- Do not embed large images or fonts.

```html
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #0f0f1a; color: #e2e8f0; height: 100vh; overflow: hidden; font-size: 13px; }
    /* Your styles */
  </style>
</head>
<body>
  <!-- Your demo markup -->
  <script>
    // Your interactivity
  </script>
</body>
</html>
```

---

#### `src/_data/demos/{slug}.json`

Just the iframe height in pixels:

```json
{
  "height": 320
}
```

Typical heights: `240` (compact), `320` (standard), `400` (tall), `480` (complex).

---

### 3. Verify locally

```bash
npm run dev
# Open http://localhost:8080/fr/patterns/{slug}/
```

Check that:
- The pattern page renders without errors
- The demo iframe is interactive and fits the height you set
- Both French and English titles display correctly (`/fr/` and `/en/`)

---

### 4. Open the pull request

**Branch naming:** `pattern/{slug}` (e.g. `pattern/sticky-column-header`)

**PR title format:**
```
[Pattern] Your Pattern Name — Category
```

**PR description — mandatory fields:**

```markdown
## Pattern candidature: [Pattern Name]

### Category
<!-- One of the 10 categories listed above -->

### What problem does it solve?
<!-- 2–3 sentences. What user need or product challenge does this address? -->

### First seen on
<!-- Product name + URL + approximate date -->
- **Product:** Notion
- **URL:** https://notion.so/...
- **First observed:** ~2023 Q2

### Other examples in the wild
<!-- At least 2 other products using this pattern -->
1. **Linear** — [describe their implementation]
2. **Figma** — [describe their implementation]
3. *(optional third)*

### Why it belongs in this library
<!-- What makes this pattern repeatable and worth documenting? -->

### What makes a good implementation
<!-- Key technical/design decisions that separate good from bad implementations -->

### Known pitfalls
<!-- What commonly goes wrong when implementing this? -->

### Checklist
- [ ] I checked that this pattern does not already exist in `src/_data/patterns/`
- [ ] I checked open PRs for duplicates
- [ ] My demo is interactive and self-contained
- [ ] Both FR and EN titles are filled in
- [ ] I tested the page locally at `/fr/patterns/{slug}/`
- [ ] `firstSeenOn` field is filled with a real product URL
- [ ] At least 2 examples are provided in the JSON
```

---

## Review process

### Open vote — 15 days

Once a PR is opened and passes the checklist above, a **15-day community vote period** begins automatically (marked with the `vote-open` label).

During this period:
- Anyone can comment with feedback, questions, or examples.
- React to the PR with 👍 (in favour) or 👎 (against).
- The author can update their files based on feedback — this resets nothing.

### Owner decision

After 15 days, the repository owner reviews the vote and comments, then:

- **Merges** if the pattern is well-documented, interactive demo works, and community sentiment is positive.
- **Requests changes** if the pattern is good but the submission needs work (demo quality, missing examples, weak description).
- **Closes** if the pattern is too niche, a duplicate, or doesn't meet the criteria above.

There is no threshold for votes — the vote is advisory, not binding. A pattern with 1 👍 can be merged if it's excellent. A pattern with 10 👍 can be closed if it doesn't meet quality standards.

**Merged patterns** are assigned their final sequential ID. The maintainer then merges `main` → `deploy` to trigger the live site update, which happens automatically via CI within minutes.

---

## Questions?

Open an issue with the label `question` or start a discussion in the [GitHub Discussions](https://github.com/rvailleux/saas-ui-patterns/discussions) tab.
