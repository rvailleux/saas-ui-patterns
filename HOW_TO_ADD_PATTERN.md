# How to Add a New Pattern

A complete step-by-step guide to adding a new UI pattern to the SaaS Patterns library.

---

## Quick Overview

Adding a pattern requires **3 files** in specific locations:

```
src/_data/patterns/{slug}.json     # Pattern metadata (required)
src/_data/demos/{slug}.html        # Interactive demo (required)
src/_data/demos/{slug}.json        # Demo height config (required)
```

---

## Step 1: Choose a Slug

Your slug should be:
- Lowercase
- Hyphen-separated
- Descriptive and unique

**Examples:**
- ✅ `sticky-column-header`
- ✅ `inline-command-palette`
- ✅ `ai-confidence-indicator`
- ❌ `Pattern123`
- ❌ `new_pattern`

---

## Step 2: Create the Pattern JSON

**File:** `src/_data/patterns/{slug}.json`

### Template

```json
{
  "id": 901,
  "slug": "your-pattern-slug",
  "category": "feedback",
  "title": {
    "fr": "Titre en français",
    "en": "English Title"
  },
  "categoryLabel": {
    "slug": "feedback",
    "fr": "Feedback & États",
    "en": "Feedback & States"
  },
  "firstSeenOn": {
    "product": "Linear",
    "url": "https://linear.app",
    "approximateDate": "2022"
  },
  "examples": [
    {
      "name": "Linear",
      "desc": {
        "fr": "description de l'implémentation",
        "en": "implementation description"
      }
    },
    {
      "name": "Figma",
      "desc": {
        "fr": "description",
        "en": "description"
      }
    },
    {
      "name": "Notion",
      "desc": {
        "fr": "description",
        "en": "description"
      }
    },
    {
      "name": "Vercel",
      "desc": {
        "fr": "description",
        "en": "description"
      }
    }
  ],
  "guide": {
    "fr": [
      "**Conseil 1** : explication concrète.",
      "**Conseil 2** : autre point important."
    ],
    "en": [
      "**Tip 1**: concrete explanation.",
      "**Tip 2**: another important point."
    ]
  },
  "pitfalls": {
    "fr": [
      "❌ Erreur commune à éviter",
      "❌ Autre piège fréquent"
    ],
    "en": [
      "❌ Common mistake to avoid",
      "❌ Another frequent pitfall"
    ]
  },
  "what": {
    "fr": "Description concise de ce qu'est le pattern.",
    "en": "Concise description of what the pattern is."
  },
  "why": {
    "fr": "Explication de pourquoi ce pattern fonctionne et quel problème il résout.",
    "en": "Explanation of why this pattern works and what problem it solves."
  }
}
```

### Field Reference

| Field | Required | Description |
|-------|----------|-------------|
| `id` | ✅ | Use `901`+ (maintainer assigns final ID) |
| `slug` | ✅ | Your hyphenated pattern identifier |
| `category` | ✅ | One of 10 categories (see below) |
| `title.fr` | ✅ | French pattern title |
| `title.en` | ✅ | English pattern title |
| `firstSeenOn.product` | ✅ | First product where you saw this |
| `firstSeenOn.url` | ✅ | URL to that product |
| `firstSeenOn.approximateDate` | ✅ | Year first observed |
| `examples` | ✅ | Array of 2-4 products using this pattern |
| `guide.fr/en` | ✅ | Array of implementation tips |
| `pitfalls.fr/en` | ✅ | Array of common mistakes (prefix with ❌) |
| `what.fr/en` | ✅ | "What it is" description |
| `why.fr/en` | ✅ | "Why it works" explanation |

### Valid Categories

| Category Value | French Label | English Label |
|----------------|--------------|---------------|
| `navigation` | Navigation & Structure | Navigation & Structure |
| `layout` | Layout & Workspace | Layout & Workspace |
| `commands` | Commandes & Recherche | Commands & Search |
| `data` | Data & Tables | Data & Tables |
| `feedback` | Feedback & États | Feedback & States |
| `ai-access` | AI — Accès & Invocation | AI — Access & Invocation |
| `ai-generation` | AI — Génération & Édition | AI — Generation & Editing |
| `ai-context` | AI — Contexte & Mémoire | AI — Context & Memory |
| `ai-feedback` | AI — Feedback & Contrôle | AI — Feedback & Control |
| `ai-prompt` | AI — Prompt UX | AI — Prompt UX |

---

## Step 3: Create the Interactive Demo

**File:** `src/_data/demos/{slug}.html`

### Requirements

- Single self-contained HTML file
- No external dependencies (inline all CSS/JS)
- Dark background: `background: #0f0f1a`
- Interactive (clicking, toggling, animating)
- Under 200 lines
- No large images/fonts

### Template

```html
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: system-ui, -apple-system, sans-serif;
      background: #0f0f1a;
      color: #e2e8f0;
      height: 100vh;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 13px;
    }
    /* Your component styles here */
  </style>
</head>
<body>
  <!-- Your demo markup here -->
  <div class="demo-container">
    <button onclick="toggle()">Click me</button>
  </div>

  <script>
    // Your interactivity here
    function toggle() {
      // Demo logic
    }
  </script>
</body>
</html>
```

### Tips for Good Demos

1. **Show the pattern in action** — don't just describe it
2. **Use realistic data** — "Project Alpha" not "Lorem ipsum"
3. **Make it responsive** — should look good at demo width
4. **Add hover states** — shows interactivity
5. **Keep animations subtle** — 150-300ms transitions

---

## Step 4: Set Demo Height

**File:** `src/_data/demos/{slug}.json`

```json
{
  "height": 320
}
```

**Height guidelines:**
- `240` — Compact patterns (buttons, badges)
- `320` — Standard patterns (most common)
- `400` — Tall patterns (tables, lists)
- `480` — Complex patterns (multi-pane layouts)

---

## Step 5: Test Locally

```bash
# Install dependencies
npm install

# Start dev server
npm run dev

# View your pattern at:
open http://localhost:8080/fr/patterns/{slug}/
open http://localhost:8080/en/patterns/{slug}/
```

### Checklist Before Submitting

- [ ] Pattern page loads without errors
- [ ] Demo iframe displays correctly
- [ ] Demo is interactive (click it!)
- [ ] Both French and English titles display
- [ ] No console errors in browser
- [ ] JSON is valid (no trailing commas)

---

## Step 6: Submit Pull Request

### Branch Naming
```
pattern/{slug}
```

Example: `pattern/sticky-column-header`

### Commit Message Format
```
feat: add [Pattern Name] pattern

- Add pattern metadata
- Add interactive demo
- Category: [Category Name]
```

### PR Title Format
```
[Pattern] Pattern Name — Category
```

Example: `[Pattern] Sticky Column Header — Data & Tables`

### PR Description Template

```markdown
## Pattern Proposal: [Name]

### Category
<!-- e.g., feedback, ai-access, data -->

### What problem does it solve?
<!-- 2-3 sentences -->

### First seen on
- **Product:** Linear
- **URL:** https://linear.app
- **First observed:** ~2022

### Other examples
1. **Figma** — description
2. **Notion** — description
3. **Vercel** — description

### Why it belongs here
<!-- What makes this repeatable? -->

### Checklist
- [ ] Checked for duplicates
- [ ] Demo is interactive
- [ ] Both FR and EN filled
- [ ] Tested locally
```

---

## Review Process

### 1. Automated Checks
Upon PR creation, automated checks verify:
- Branch name format
- Required files exist
- JSON validity
- Demo file presence

### 2. Community Vote (15 days)
- PR gets `vote-open` label
- Community reacts with 👍 / 👎
- Feedback can be incorporated

### 3. Merge Decision
Maintainer evaluates:
- Pattern quality and uniqueness
- Demo interactivity
- Documentation completeness
- Community feedback

### 4. Deployment
Once merged to `main`:
1. Maintainer creates PR: `main` → `deploy`
2. On merge, CI deploys to production automatically
3. Live within ~2 minutes

---

## Complete Example

See `keyboard-shortcut-overlay` for a complete example:

- **Pattern:** `src/_data/patterns/keyboard-shortcut-overlay.json`
- **Demo HTML:** `src/_data/demos/keyboard-shortcut-overlay.html`
- **Demo Config:** `src/_data/demos/keyboard-shortcut-overlay.json`

---

## Common Issues

### "Pattern not found" error
- Check slug matches exactly in all 3 files
- Verify file extensions (.json vs .html)

### Demo not displaying
- Check demo JSON has valid `height` number
- Verify HTML has no syntax errors
- Ensure no external resources (CDN links)

### JSON validation fails
- Remove trailing commas
- Ensure all quotes are straight `"` not curly `"`
- Validate at jsonlint.com

### Category not recognized
- Must be exact value from category table
- Case-sensitive

---

## Questions?

- Check existing patterns in `src/_data/patterns/` for reference
- Open an issue with label `question`
- Start a GitHub Discussion
