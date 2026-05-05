---
name: create-pattern
description: Use this skill when the user wants to add a new UI pattern to the SaaS UI Patterns catalog. This skill guides contributors through the process of creating a new pattern by collecting essential information, generating the required files, and ensuring the pattern meets project standards. Trigger on phrases like "add pattern", "create pattern", "new pattern", "submit a pattern", or when discussing adding content to the pattern library.
---

# Create Pattern Skill

You help contributors add new UI patterns to the SaaS UI Patterns catalog. This is a guided workflow that collects pattern information and generates the three required files.

## When to Use This Skill

Use this skill when:
- A user wants to add a new UI pattern to the catalog
- Someone mentions "adding a pattern", "new pattern", or "pattern proposal"
- A contributor needs help creating pattern files

## Before You Start

Check that the pattern doesn't already exist:
1. Search existing patterns: `ls src/_data/patterns/ | grep -i <keyword>`
2. Check if a similar pattern is already documented

If the pattern exists, inform the user and stop.

## Pattern Requirements

For a pattern to be accepted, it must meet ALL three criteria:
1. **Observed in production** — seen in at least one real SaaS product (not just Dribbble)
2. **Repeatable** — solves a recurring problem across different contexts
3. **Describable** — can explain *why* it works, not just *what* it does

## The Three Required Files

Every pattern requires exactly three files:

| File | Purpose |
|------|---------|
| `src/_data/patterns/{slug}.json` | Pattern metadata, titles, examples, guide, pitfalls |
| `src/_data/demos/{slug}.html` | Self-contained interactive demo |
| `src/_data/demos/{slug}.json` | Demo height configuration |

## Information Collection Flow

Collect information from the contributor in this order. Ask one question at a time and wait for the answer before proceeding.

### Step 1: Pattern Identity

1. **Slug** (required): Ask for a lowercase, hyphen-separated identifier
   - Good: `sticky-column-header`, `command-palette`, `ai-confidence-indicator`
   - Bad: `Pattern123`, `new_pattern`, `myCoolPattern`

2. **Category** (required): Present the 10 options and ask them to choose:

   | Category | Description |
   |----------|-------------|
   | `navigation` | Navigation & Structure |
   | `layout` | Layout & Workspace |
   | `commands` | Commands & Search |
   | `data` | Data & Tables |
   | `feedback` | Feedback & States |
   | `ai-access` | AI — Access & Invocation |
   | `ai-generation` | AI — Generation & Editing |
   | `ai-context` | AI — Context & Memory |
   | `ai-feedback` | AI — Feedback & Control |
   | `ai-prompt` | AI — Prompt UX |

3. **Titles** (required): Ask for both French and English titles
   - French: Short, descriptive (e.g., "Overlay de raccourcis clavier")
   - English: Short, descriptive (e.g., "Keyboard Shortcut Overlay")

### Step 2: Pattern Description

4. **What it is** (required): Ask for a concise description of what the pattern is
   - Keep it to 1-2 sentences
   - Focus on the user's perspective
   - Get both French and English versions

5. **Why it works** (required): Ask for an explanation of why this pattern works
   - What problem does it solve?
   - Why is this approach effective?
   - Get both French and English versions

### Step 3: Attribution & Examples

6. **First seen on** (required): Collect:
   - Product name (e.g., "Linear", "Notion")
   - URL (e.g., "https://linear.app")
   - Approximate date first observed (e.g., "2023", "2022 Q2")

7. **Other examples** (required): Ask for at least 2 other products using this pattern
   - For each: Product name + brief description of their implementation
   - Get descriptions in both French and English

### Step 4: Implementation Guide

8. **Implementation tips** (required): Ask for 2-4 concrete tips for implementing this pattern well
   - Focus on practical advice
   - Get both French and English versions
   - Format as bullet points starting with bold (e.g., "**Contextualisez** : ...")

9. **Common pitfalls** (required): Ask for 2-4 common mistakes to avoid
   - What goes wrong when teams implement this?
   - Get both French and English versions
   - Prefix with ❌ emoji

### Step 5: Interactive Demo

10. **Demo concept**: Ask what the demo should show
    - The demo must be interactive (clicking, toggling, animating)
    - It should demonstrate the pattern in action
    - Keep it simple but illustrative

11. **Demo height**: Ask which height fits best:
    - `240` — Compact patterns (buttons, badges)
    - `320` — Standard patterns (most common, default)
    - `400` — Tall patterns (tables, lists)
    - `480` — Complex patterns (multi-pane layouts)

## Creating the Files

Once all information is collected, create the three files:

### 1. Pattern JSON: `src/_data/patterns/{slug}.json`

Use this exact structure:

```json
{
  "id": 901,
  "slug": "{slug}",
  "category": "{category}",
  "title": {
    "fr": "{french_title}",
    "en": "{english_title}"
  },
  "categoryLabel": {
    "slug": "{category}",
    "fr": "{french_category_label}",
    "en": "{english_category_label}"
  },
  "firstSeenOn": {
    "product": "{product}",
    "url": "{url}",
    "approximateDate": "{date}"
  },
  "examples": [
    {
      "name": "{example1_name}",
      "desc": {
        "fr": "{example1_fr_desc}",
        "en": "{example1_en_desc}"
      }
    },
    {
      "name": "{example2_name}",
      "desc": {
        "fr": "{example2_fr_desc}",
        "en": "{example2_en_desc}"
      }
    }
  ],
  "guide": {
    "fr": [
      "{tip1_fr}",
      "{tip2_fr}"
    ],
    "en": [
      "{tip1_en}",
      "{tip2_en}"
    ]
  },
  "pitfalls": {
    "fr": [
      "❌ {pitfall1_fr}",
      "❌ {pitfall2_fr}"
    ],
    "en": [
      "❌ {pitfall1_en}",
      "❌ {pitfall2_en}"
    ]
  },
  "what": {
    "fr": "{what_fr}",
    "en": "{what_en}"
  },
  "why": {
    "fr": "{why_fr}",
    "en": "{why_en}"
  }
}
```

Use the category label mapping:
- `navigation` → "Navigation & Structure"
- `layout` → "Layout & Workspace"
- `commands` → "Commandes & Recherche" / "Commands & Search"
- `data` → "Data & Tables"
- `feedback` → "Feedback & États" / "Feedback & States"
- `ai-access` → "AI — Accès & Invocation" / "AI — Access & Invocation"
- `ai-generation` → "AI — Génération & Édition" / "AI — Generation & Editing"
- `ai-context` → "AI — Contexte & Mémoire" / "AI — Context & Memory"
- `ai-feedback` → "AI — Feedback & Contrôle" / "AI — Feedback & Control"
- `ai-prompt` → "AI — Prompt UX"

### 2. Demo HTML: `src/_data/demos/{slug}.html`

Create a self-contained interactive demo using this template:

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
    /* Add your component styles here */
  </style>
</head>
<body>
  <!-- Your demo markup here -->

  <script>
    // Your interactivity here
  </script>
</body>
</html>
```

Requirements for the demo:
- Must be interactive (respond to clicks, hovers, or keypresses)
- Use dark background (#0f0f1a) to match site aesthetic
- No external dependencies (inline all CSS/JS)
- Keep under 200 lines
- Use realistic example data

### 3. Demo Config: `src/_data/demos/{slug}.json`

```json
{
  "height": {height}
}
```

## After Creating Files

Once all three files are created:

1. Run `npm run dev` to verify the pattern loads correctly
2. Navigate to `/fr/patterns/{slug}/` and `/en/patterns/{slug}/`
3. Confirm the demo is interactive and displays correctly
4. Use the `submit-pattern` skill to submit the pattern as a PR

## Important Reminders

- **Always use id 901+** — the maintainer will assign the final sequential ID on merge
- **Both French and English are required** for all text fields
- **The demo MUST be interactive** — static screenshots are not acceptable
- **First seen on must be a real product** with a real URL
- **At least 2 examples are required** in the examples array
