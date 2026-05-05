---
name: submit-pattern
description: Use this skill when the user wants to submit a new pattern as a pull request to the SaaS UI Patterns repository. This skill guides contributors through the PR submission process, validates that all required files exist, ensures the branch is properly named, completes the submission checklist, and creates a well-formed PR using the gh CLI. Trigger on phrases like "submit pattern", "create PR", "open pull request", "submit my pattern", or when the user has finished creating pattern files and wants to contribute them.
---

# Submit Pattern Skill

You help contributors submit their new UI pattern as a well-formed pull request to the SaaS UI Patterns catalog.

## When to Use This Skill

Use this skill when:
- A user has finished creating pattern files and wants to submit them
- Someone says "submit my pattern", "create PR", or "open pull request"
- A contributor needs help with the PR submission process

## Prerequisites

Before starting, confirm:
1. The pattern files have been created using the `create-pattern` skill (or manually)
2. The contributor has tested the pattern locally (`npm run dev`)
3. The contributor has a GitHub account and push access to the repository (or has forked it)

## Pre-Submission Validation

First, verify the pattern is ready for submission by checking all required files exist:

### Step 1: Check Required Files Exist

Run these checks:

```bash
# Get the slug from the user
slug="{pattern-slug}"

# Check pattern JSON exists
if [ ! -f "src/_data/patterns/${slug}.json" ]; then
    echo "❌ Missing: src/_data/patterns/${slug}.json"
fi

# Check demo HTML exists
if [ ! -f "src/_data/demos/${slug}.html" ]; then
    echo "❌ Missing: src/_data/demos/${slug}.html"
fi

# Check demo config exists
if [ ! -f "src/_data/demos/${slug}.json" ]; then
    echo "❌ Missing: src/_data/demos/${slug}.json"
fi
```

If any file is missing, stop and tell the user to complete the pattern first (use the `create-pattern` skill).

### Step 2: Validate JSON Structure

Check that the pattern JSON has all required fields:

```bash
# Quick validation - check for required keys
jq -e '.id and .slug and .category and .title.fr and .title.en and .firstSeenOn.product and .examples | length >= 2' "src/_data/patterns/${slug}.json" || echo "❌ JSON missing required fields"
```

### Step 3: Check Git Status

Ensure the contributor is on a clean state to create a new branch:

```bash
git status
```

If there are uncommitted changes, advise the user to commit or stash them first.

## Submission Checklist

Walk the contributor through this mandatory checklist. Ask each question and wait for confirmation before proceeding.

### Checklist Questions

Ask these one by one. All must be confirmed with "yes" before proceeding:

1. **Have you checked that this pattern does not already exist in `src/_data/patterns/`?**
   - Action: Run `ls src/_data/patterns/ | grep -i {keyword}` for the main keywords
   - Must be confirmed: Yes/No

2. **Have you checked open PRs for duplicates?**
   - Action: Run `gh pr list --search "{pattern-name}"` or browse to https://github.com/rvailleux/saas-ui-patterns/pulls
   - Must be confirmed: Yes/No

3. **Is your demo interactive and self-contained?**
   - Requirements: No external dependencies, has clicking/toggling/animating behavior
   - Must be confirmed: Yes/No

4. **Are both French and English titles filled in the JSON?**
   - Check: `jq '.title.fr, .title.en' src/_data/patterns/{slug}.json`
   - Must be confirmed: Yes/No

5. **Is the `firstSeenOn` field filled with a real product URL?**
   - Must be confirmed: Yes/No

6. **Are at least 2 examples provided in the JSON?**
   - Check: `jq '.examples | length' src/_data/patterns/{slug}.json`
   - Must be confirmed: Yes/No

7. **Have you tested the page locally at `/fr/patterns/{slug}/`?**
   - Requirements: No errors, demo displays correctly
   - Must be confirmed: Yes/No

8. **Does the demo fit within the height set in `demos/{slug}.json`?**
   - Must be confirmed: Yes/No

If any answer is "no", stop and help the contributor fix the issue before proceeding.

## Creating the Branch

Once all checklist items are confirmed:

### Step 4: Create and Checkout Branch

Branch naming convention: `pattern/{slug}`

```bash
# Create and checkout the branch
git checkout -b "pattern/${slug}"
```

If the branch already exists, check if it's the contributor's existing work or a conflict:

```bash
git branch -a | grep "pattern/${slug}"
```

### Step 5: Stage and Commit Files

```bash
# Stage the three files
git add "src/_data/patterns/${slug}.json"
git add "src/_data/demos/${slug}.html"
git add "src/_data/demos/${slug}.json"

# Create the commit with proper format
git commit -m "feat: add ${title_en} pattern

- Add pattern metadata
- Add interactive demo
- Category: ${category_name}"
```

The commit message format must be:
```
feat: add [Pattern Name] pattern

- Add pattern metadata
- Add interactive demo
- Category: [Category Name]
```

### Step 6: Push Branch

```bash
# Push the branch
# If contributor has fork:
git push -u origin "pattern/${slug}"

# If pushing to main repo directly:
git push -u origin "pattern/${slug}"
```

## Creating the Pull Request

### Step 7: Extract Information from JSON

Read the pattern JSON to populate the PR description:

```bash
# Get key information
slug=$(jq -r '.slug' src/_data/patterns/${slug}.json)
title_en=$(jq -r '.title.en' src/_data/patterns/${slug}.json)
title_fr=$(jq -r '.title.fr' src/_data/patterns/${slug}.json)
category=$(jq -r '.category' src/_data/patterns/${slug}.json)
product=$(jq -r '.firstSeenOn.product' src/_data/patterns/${slug}.json)
url=$(jq -r '.firstSeenOn.url' src/_data/patterns/${slug}.json)
date=$(jq -r '.firstSeenOn.approximateDate' src/_data/patterns/${slug}.json)
what_en=$(jq -r '.what.en' src/_data/patterns/${slug}.json)
why_en=$(jq -r '.why.en' src/_data/patterns/${slug}.json)
```

Map category to label:
- `navigation` → "Navigation & Structure"
- `layout` → "Layout & Workspace"
- `commands` → "Commands & Search"
- `data` → "Data & Tables"
- `feedback` → "Feedback & States"
- `ai-access` → "AI — Access & Invocation"
- `ai-generation` → "AI — Generation & Editing"
- `ai-context` → "AI — Context & Memory"
- `ai-feedback` → "AI — Feedback & Control"
- `ai-prompt` → "AI — Prompt UX"

### Step 8: Build PR Description

Create the PR description using the template. Ask the contributor to fill in any missing sections (problem solved, why it belongs, good implementation traits, pitfalls).

```markdown
## Pattern candidature: ${title_en}

### Category
${category_label}

### What problem does it solve?
${what_en}

${why_en}

### First seen on
- **Product:** ${product}
- **URL:** ${url}
- **First observed (approx. date):** ${date}

### Other examples in the wild
${examples_section}

### Why it belongs in this library
<!-- Contributor fills this -->

### What makes a good implementation
<!-- Contributor fills this -->

### Known pitfalls
<!-- Contributor fills this -->

---

### Files included in this PR
- [x] `src/_data/patterns/${slug}.json`
- [x] `src/_data/demos/${slug}.html`
- [x] `src/_data/demos/${slug}.json`

### Submission checklist
- [x] I searched `src/_data/patterns/` and confirmed this pattern does not already exist
- [x] I searched open PRs and issues for duplicates
- [x] My demo is interactive and self-contained (no external dependencies)
- [x] Both `fr` and `en` titles are filled in the JSON
- [x] `firstSeenOn` contains a real product URL
- [x] At least 2 examples are listed in the JSON and in this PR description
- [x] I tested the page locally at `/fr/patterns/${slug}/`
- [x] The demo fits within the height I set in `demos/${slug}.json`
```

Build the examples section from the JSON:
```bash
examples_section=""
for i in {0..3}; do
    name=$(jq -r ".examples[${i}].name" src/_data/patterns/${slug}.json)
    desc=$(jq -r ".examples[${i}].desc.en" src/_data/patterns/${slug}.json)
    if [ "$name" != "null" ] && [ -n "$name" ]; then
        examples_section="${examples_section}${i}. **${name}** — ${desc}
"
    fi
done
```

### Step 9: Ask for Missing Information

The PR description has sections that need manual input:
1. **Why it belongs in this library** — What makes this pattern repeatable?
2. **What makes a good implementation** — Key technical/design decisions
3. **Known pitfalls** — What commonly goes wrong?

Ask the contributor to provide 2-3 sentences for each.

### Step 10: Create the PR via gh CLI

Once the description is complete:

```bash
# Create the PR
git push -u origin "pattern/${slug}"

gh pr create \
  --title "[Pattern] ${title_en} — ${category_label}" \
  --body "${pr_body}" \
  --base main
```

The PR title format must be:
```
[Pattern] Pattern Name — Category
```

Examples:
- `[Pattern] Keyboard Shortcut Overlay — Commands & Search`
- `[Pattern] Sticky Column Header — Data & Tables`
- `[Pattern] AI Confidence Indicator — AI — Feedback & Control`

## Post-Submission Summary

After the PR is created, provide the contributor with:

1. **PR URL** — Share the link to the created PR
2. **What happens next** — Explain the review process:
   - 15-day community vote period starts automatically
   - Community can react with 👍/👎 and leave feedback
   - Maintainer will review after the vote period
   - If accepted, pattern gets a final ID and is merged

3. **Reminder** — The contributor can update their files based on feedback without resetting the vote period.

## Error Handling

Common issues and solutions:

### "gh" CLI not installed
Advise installing GitHub CLI: https://cli.github.com/

### "Authentication failed"
Run `gh auth login` to authenticate

### "Branch already exists"
Check if it's the contributor's own branch or a conflict with someone else's work

### "No changes to commit"
Verify files are actually modified: `git status`

### Push rejected
May need to fork first if contributor doesn't have write access:
```bash
# Fork the repo via gh CLI
gh repo fork rvailleux/saas-ui-patterns --remote --clone
cd saas-ui-patterns
# Then create branch and submit PR as normal
```
