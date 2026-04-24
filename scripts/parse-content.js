const fs = require("fs");
const path = require("path");

const contentPath = path.join(__dirname, "..", "content.md");
const outputDir = path.join(__dirname, "..", "src", "_data");

// Category mapping based on CLAUDE.md structure
const categoryMap = {
  1: { slug: "navigation", fr: "Navigation & Structure", en: "Navigation & Structure" },
  2: { slug: "navigation", fr: "Navigation & Structure", en: "Navigation & Structure" },
  3: { slug: "navigation", fr: "Navigation & Structure", en: "Navigation & Structure" },
  4: { slug: "navigation", fr: "Navigation & Structure", en: "Navigation & Structure" },
  5: { slug: "layout", fr: "Layout & Workspace", en: "Layout & Workspace" },
  6: { slug: "layout", fr: "Layout & Workspace", en: "Layout & Workspace" },
  7: { slug: "layout", fr: "Layout & Workspace", en: "Layout & Workspace" },
  8: { slug: "layout", fr: "Layout & Workspace", en: "Layout & Workspace" },
  9: { slug: "commands", fr: "Commandes & Recherche", en: "Commands & Search" },
  10: { slug: "commands", fr: "Commandes & Recherche", en: "Commands & Search" },
  11: { slug: "commands", fr: "Commandes & Recherche", en: "Commands & Search" },
  12: { slug: "commands", fr: "Commandes & Recherche", en: "Commands & Search" },
  13: { slug: "data", fr: "Data & Tables", en: "Data & Tables" },
  14: { slug: "data", fr: "Data & Tables", en: "Data & Tables" },
  15: { slug: "data", fr: "Data & Tables", en: "Data & Tables" },
  16: { slug: "data", fr: "Data & Tables", en: "Data & Tables" },
  17: { slug: "feedback", fr: "Feedback & États", en: "Feedback & States" },
  18: { slug: "feedback", fr: "Feedback & États", en: "Feedback & States" },
  19: { slug: "feedback", fr: "Feedback & États", en: "Feedback & States" },
  20: { slug: "feedback", fr: "Feedback & États", en: "Feedback & States" },
  21: { slug: "ai-access", fr: "AI — Accès & Invocation", en: "AI — Access & Invocation" },
  22: { slug: "ai-access", fr: "AI — Accès & Invocation", en: "AI — Access & Invocation" },
  23: { slug: "ai-access", fr: "AI — Accès & Invocation", en: "AI — Access & Invocation" },
  24: { slug: "ai-access", fr: "AI — Accès & Invocation", en: "AI — Access & Invocation" },
  25: { slug: "ai-generation", fr: "AI — Génération & Édition", en: "AI — Generation & Editing" },
  26: { slug: "ai-generation", fr: "AI — Génération & Édition", en: "AI — Generation & Editing" },
  27: { slug: "ai-generation", fr: "AI — Génération & Édition", en: "AI — Generation & Editing" },
  28: { slug: "ai-generation", fr: "AI — Génération & Édition", en: "AI — Generation & Editing" },
  29: { slug: "ai-context", fr: "AI — Contexte & Mémoire", en: "AI — Context & Memory" },
  30: { slug: "ai-context", fr: "AI — Contexte & Mémoire", en: "AI — Context & Memory" },
  31: { slug: "ai-context", fr: "AI — Contexte & Mémoire", en: "AI — Context & Memory" },
  32: { slug: "ai-context", fr: "AI — Contexte & Mémoire", en: "AI — Context & Memory" },
  33: { slug: "ai-feedback", fr: "AI — Feedback & Contrôle", en: "AI — Feedback & Control" },
  34: { slug: "ai-feedback", fr: "AI — Feedback & Contrôle", en: "AI — Feedback & Control" },
  35: { slug: "ai-feedback", fr: "AI — Feedback & Contrôle", en: "AI — Feedback & Control" },
  36: { slug: "ai-feedback", fr: "AI — Feedback & Contrôle", en: "AI — Feedback & Control" },
  37: { slug: "ai-prompt", fr: "AI — Prompt UX", en: "AI — Prompt UX" },
  38: { slug: "ai-prompt", fr: "AI — Prompt UX", en: "AI — Prompt UX" },
  39: { slug: "ai-prompt", fr: "AI — Prompt UX", en: "AI — Prompt UX" },
  40: { slug: "ai-prompt", fr: "AI — Prompt UX", en: "AI — Prompt UX" },
};

// English translations for pattern titles
const titleTranslations = {
  "Sidebar collapsible icon-rail": "Sidebar Collapsible Icon Rail",
  "Top nav + contextual left panel": "Top Nav + Contextual Left Panel",
  "Breadcrumb dynamique": "Dynamic Breadcrumb",
  "Tabs persistants / pinnable": "Persistent / Pinnable Tabs",
  "Right panel contextuel (détail)": "Contextual Right Panel (Detail)",
  "Split view / panneau dual": "Split View / Dual Panel",
  "Floating Action Button (FAB)": "Floating Action Button (FAB)",
  "Board & vue switcher": "Board & View Switcher",
  "Command palette (⌘K)": "Command Palette (⌘K)",
  "Omnibox / unified search": "Omnibox / Unified Search",
  "Inline slash commands": "Inline Slash Commands",
  "Contextual right-click menu": "Contextual Right-Click Menu",
  "Spreadsheet-like inline editing": "Spreadsheet-like Inline Editing",
  "Filtres persistants & URL-encodés": "Persistent & URL-encoded Filters",
  "Virtual scrolling": "Virtual Scrolling",
  "Column resizing & reordering": "Column Resizing & Reordering",
  "Toast notification + undo": "Toast Notification + Undo",
  "Optimistic UI": "Optimistic UI",
  "Empty states actionnables": "Actionable Empty States",
  "Skeleton screens": "Skeleton Screens",
  "AI sidebar persistante": "Persistent AI Sidebar",
  "⌘K → AI intent": "⌘K → AI Intent",
  "Floating AI button contextuel": "Contextual Floating AI Button",
  "Inline slash AI commands": "Inline Slash AI Commands",
  "Streaming text (typewriter)": "Streaming Text (Typewriter)",
  "Diff view accept/reject": "Diff View Accept/Reject",
  "Ghost text / inline autocomplete": "Ghost Text / Inline Autocomplete",
  "Canvas / artifact panel": "Canvas / Artifact Panel",
  "@-mentions pour le contexte": "@-mentions for Context",
  "Fil de conversation persistant": "Persistent Conversation Thread",
  "Memory / préférences utilisateur": "Memory / User Preferences",
  "Sources citées / grounding": "Cited Sources / Grounding",
  "Thinking / reasoning visible": "Visible Thinking / Reasoning",
  "Regenerate + variantes": "Regenerate + Variants",
  "Agentic step tracker": "Agentic Step Tracker",
  "Confidence / uncertainty signal": "Confidence / Uncertainty Signal",
  "Suggested prompts / quick actions": "Suggested Prompts / Quick Actions",
  "Prompt templates": "Prompt Templates",
  "Multimodal drop zone": "Multimodal Drop Zone",
  "Mode voix natif": "Native Voice Mode",
};

function slugify(text) {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");
}

function parsePatterns(content) {
  const patterns = [];
  const lines = content.split("\n");

  let currentPattern = null;
  let currentSection = null;
  let sectionBuffer = [];

  const sections = {
    "ce que c'est": "what",
    "pourquoi ça marche": "why",
    "démo": "demo",
    "meilleurs exemples": "examples",
    "guide d'implémentation": "guide",
    "pièges à éviter": "pitfalls",
  };

  function flushSection() {
    if (!currentPattern || !currentSection) return;
    const sectionKey = sections[currentSection.toLowerCase()];
    if (sectionKey) {
      let content = sectionBuffer.join("\n").trim();

      // Special handling for examples section
      if (sectionKey === "examples") {
        currentPattern.examples = parseExamples(content);
      } else if (sectionKey === "guide" || sectionKey === "pitfalls") {
        // Parse numbered/bullet lists
        currentPattern[sectionKey] = content
          .split("\n")
          .filter((line) => line.match(/^[\d\-\*•]/))
          .map((line) => line.replace(/^[\d\-\*•]\.?\s*/, "").trim())
          .filter((line) => line.length > 0);
      } else {
        currentPattern[sectionKey] = { fr: content, en: translateContent(sectionKey, content) };
      }
    }
    sectionBuffer = [];
  }

  function parseExamples(content) {
    const examples = [];
    const lines = content.split("\n");
    let currentExample = null;

    for (const line of lines) {
      const match = line.match(/^-\s*\*\*(.+?)\*\*\s*[—–-]\s*(.+)/);
      if (match) {
        if (currentExample) examples.push(currentExample);
        currentExample = {
          name: match[1].trim(),
          desc: { fr: match[2].trim(), en: "" },
        };
      } else if (currentExample && line.trim().startsWith("-")) {
        // Additional description line
        currentExample.desc.fr += " " + line.replace(/^-\s*/, "").trim();
      }
    }
    if (currentExample) examples.push(currentExample);

    // Translate examples
    examples.forEach((ex) => {
      ex.desc.en = translateExampleDesc(ex.desc.fr);
    });

    return examples;
  }

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    // Match pattern headers like "## 1. Sidebar collapsible icon-rail"
    const patternMatch = line.match(/^##\s+(\d+)\.\s+(.+)$/);
    if (patternMatch) {
      flushSection();
      if (currentPattern) {
        patterns.push(currentPattern);
      }

      const id = parseInt(patternMatch[1], 10);
      const titleFr = patternMatch[2].trim();
      const category = categoryMap[id];

      currentPattern = {
        id,
        slug: slugify(titleFr),
        category: category?.slug || "misc",
        title: {
          fr: titleFr,
          en: titleTranslations[titleFr] || titleFr,
        },
        categoryLabel: category || { slug: "misc", fr: "Autre", en: "Other" },
        examples: [],
        guide: [],
        pitfalls: [],
      };
      currentSection = null;
      continue;
    }

    // Match section headers
    const sectionMatch = line.match(/^\*\*(.+?)\*\*/);
    if (sectionMatch && currentPattern) {
      const sectionName = sectionMatch[1].toLowerCase().replace(/[:\s]+$/, "");
      if (sections[sectionName]) {
        flushSection();
        currentSection = sectionName;
        // Extract any content after the header on the same line
        const inlineContent = line.replace(/^\*\*.*?\*\*\s*[-—]?\s*/, "").trim();
        if (inlineContent) {
          sectionBuffer.push(inlineContent);
        }
        continue;
      }
    }

    // Match code blocks (for demo section)
    if (line.startsWith("```") && currentPattern && currentSection === "démo") {
      sectionBuffer.push(line);
      // Keep collecting until end of code block
      i++;
      while (i < lines.length && !lines[i].startsWith("```")) {
        sectionBuffer.push(lines[i]);
        i++;
      }
      if (i < lines.length) {
        sectionBuffer.push(lines[i]);
      }
      continue;
    }

    // Collect content for current section
    if (currentSection && currentPattern) {
      sectionBuffer.push(line);
    }
  }

  flushSection();
  if (currentPattern) {
    patterns.push(currentPattern);
  }

  return patterns;
}

// Simple translation function - in production this would use a translation service
function translateContent(type, content) {
  // For now, return content with a note that it's French
  // In a real implementation, you would use an API or pre-translated content
  return `[EN] ${content.substring(0, 100)}${content.length > 100 ? "..." : ""}`;
}

function translateExampleDesc(desc) {
  // Placeholder translations for common phrases
  const translations = {
    "transition fluide": "smooth transition",
    "état mémorisé": "state persistence",
    "icône rail avec flyout": "icon rail with flyout",
    "référence fondatrice": "foundational reference",
    "référence absolue": "absolute reference",
    "implémentation enterprise": "enterprise implementation",
    "parfaitement coordonnés": "perfectly coordinated",
    "déclinaison plus dense": "denser variant",
    "configurable par admin": "admin-configurable",
    "hover dropdown sur chaque segment": "hover dropdown on each segment",
    "éditable inline": "inline editable",
    "indicateur de non-sauvegarde": "unsaved changes indicator",
    "preview mode": "preview mode",
    "édition complète inline": "full inline editing",
    "largeur ajustable": "adjustable width",
    "détail de contact/deal": "contact/deal detail",
    "split de pages": "page split",
    "split de notes": "note split",
    "list+preview": "list+preview",
    "menu radial d'actions": "radial action menu",
    "15+ vues": "15+ views",
    "recherche full-text": "full-text search",
    "navigation imbriquée": "nested navigation",
    "recherche floue": "fuzzy search",
    "raccourcis affichés": "displayed shortcuts",
    "actions contextuelles": "contextual actions",
    "référence UX": "UX reference",
    "command palette comme produit entier": "command palette as entire product",
    "extensions supportées": "extensions supported",
  };

  let translated = desc;
  for (const [fr, en] of Object.entries(translations)) {
    translated = translated.replace(new RegExp(fr, "gi"), en);
  }
  return translated;
}

// Main execution
const content = fs.readFileSync(contentPath, "utf-8");
const patterns = parsePatterns(content);

// Create output directory if needed
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true });
}

// Write patterns.json
fs.writeFileSync(
  path.join(outputDir, "patterns.json"),
  JSON.stringify(patterns, null, 2)
);

// Create categories.json
const categories = [
  { slug: "navigation", fr: "Navigation & Structure", en: "Navigation & Structure" },
  { slug: "layout", fr: "Layout & Workspace", en: "Layout & Workspace" },
  { slug: "commands", fr: "Commandes & Recherche", en: "Commands & Search" },
  { slug: "data", fr: "Data & Tables", en: "Data & Tables" },
  { slug: "feedback", fr: "Feedback & États", en: "Feedback & States" },
  { slug: "ai-access", fr: "AI — Accès & Invocation", en: "AI — Access & Invocation" },
  { slug: "ai-generation", fr: "AI — Génération & Édition", en: "AI — Generation & Editing" },
  { slug: "ai-context", fr: "AI — Contexte & Mémoire", en: "AI — Context & Memory" },
  { slug: "ai-feedback", fr: "AI — Feedback & Contrôle", en: "AI — Feedback & Control" },
  { slug: "ai-prompt", fr: "AI — Prompt UX", en: "AI — Prompt UX" },
];

fs.writeFileSync(
  path.join(outputDir, "categories.json"),
  JSON.stringify(categories, null, 2)
);

// Create site.json
const site = {
  name: { fr: "SaaS UI Design Patterns", en: "SaaS UI Design Patterns" },
  description: {
    fr: "Guide de référence pour designers produit et développeurs front-end",
    en: "Reference guide for product designers and front-end developers",
  },
  locales: ["fr", "en"],
  defaultLocale: "fr",
};

fs.writeFileSync(path.join(outputDir, "site.json"), JSON.stringify(site, null, 2));

console.log(`Parsed ${patterns.length} patterns`);
console.log(`Categories: ${categories.length}`);
console.log("Output written to src/_data/");
