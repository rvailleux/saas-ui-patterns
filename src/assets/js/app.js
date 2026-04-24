// App State
const state = {
  sidebarCollapsed: false,
  searchQuery: "",
  selectedIndex: 0,
  fuse: null,
  patterns: [],
  locale: "fr",
};

// DOM Elements
const sidebar = document.getElementById("sidebar");
const sidebarToggle = document.getElementById("sidebar-toggle");
const mobileMenuBtn = document.getElementById("mobile-menu-btn");
const mobileOverlay = document.getElementById("mobile-overlay");
const searchTrigger = document.getElementById("search-trigger");
const commandPalette = document.getElementById("command-palette");
const commandInput = document.getElementById("command-input");
const commandResults = document.getElementById("command-results");
const themeToggle = document.getElementById("theme-toggle");
const kbdCmd = document.getElementById("kbd-cmd");

// Initialize
document.addEventListener("DOMContentLoaded", () => {
  initSidebar();
  initSearch();
  initTheme();
  initKeyboardShortcuts();
  initPatternData();
});

// Initialize pattern data from window.APP_DATA
function initPatternData() {
  if (window.APP_DATA) {
    state.patterns = window.APP_DATA.patterns;
    state.locale = window.APP_DATA.locale;
    initFuse();
  }
}

// Initialize Fuse.js for fuzzy search
function initFuse() {
  const options = {
    keys: [
      { name: `title.${state.locale}`, weight: 2 },
      { name: `what.${state.locale}`, weight: 1 },
      { name: `why.${state.locale}`, weight: 0.5 },
      { name: "category", weight: 1 },
    ],
    threshold: 0.3,
    includeScore: true,
  };
  state.fuse = new Fuse(state.patterns, options);
}

// Sidebar Functions
function initSidebar() {
  // Load saved state
  const saved = localStorage.getItem("sidebarCollapsed");
  if (saved !== null) {
    state.sidebarCollapsed = saved === "true";
    updateSidebarState();
  }

  sidebarToggle?.addEventListener("click", toggleSidebar);
  mobileMenuBtn?.addEventListener("click", openMobileSidebar);
}

function toggleSidebar() {
  state.sidebarCollapsed = !state.sidebarCollapsed;
  localStorage.setItem("sidebarCollapsed", state.sidebarCollapsed);
  updateSidebarState();
}

function updateSidebarState() {
  if (state.sidebarCollapsed) {
    sidebar?.classList.add("collapsed");
  } else {
    sidebar?.classList.remove("collapsed");
  }
}

function openMobileSidebar() {
  sidebar?.classList.remove("collapsed");
  mobileOverlay?.classList.remove("hidden");
  document.body.style.overflow = "hidden";
}

function closeSidebar() {
  if (window.innerWidth < 1024) {
    mobileOverlay?.classList.add("hidden");
    document.body.style.overflow = "";
  }
}

// Search / Command Palette Functions
function initSearch() {
  searchTrigger?.addEventListener("click", openCommandPalette);
  commandPalette?.addEventListener("click", (e) => {
    if (e.target === commandPalette) closeCommandPalette();
  });
  commandInput?.addEventListener("input", handleSearchInput);
}

function openCommandPalette() {
  commandPalette?.classList.remove("hidden");
  commandInput?.focus();
  renderSearchResults(state.patterns.slice(0, 8)); // Show first 8 initially
}

function closeCommandPalette() {
  commandPalette?.classList.add("hidden");
  commandInput.value = "";
  state.searchQuery = "";
  state.selectedIndex = 0;
}

function handleSearchInput(e) {
  const query = e.target.value.trim();
  state.searchQuery = query;
  state.selectedIndex = 0;

  if (!query) {
    renderSearchResults(state.patterns.slice(0, 8));
    return;
  }

  const results = state.fuse?.search(query).map((r) => r.item) || [];
  renderSearchResults(results);
}

function renderSearchResults(results) {
  if (!commandResults) return;

  if (results.length === 0) {
    commandResults.innerHTML = `
      <div class="px-4 py-8 text-center text-text-muted">
        ${state.locale === "fr" ? "Aucun résultat" : "No results"}
      </div>
    `;
    return;
  }

  const html = results
    .map((pattern, index) => {
      const isSelected = index === state.selectedIndex;
      return `
        <div
          class="command-item ${isSelected ? "selected" : ""}"
          data-index="${index}"
          data-slug="${pattern.slug}"
          onclick="navigateToPattern('${pattern.slug}')"
        >
          <span class="flex items-center justify-center w-8 h-8 rounded bg-accent/10 text-accent text-sm font-medium">
            ${pattern.id}
          </span>
          <div class="flex-1 min-w-0">
            <div class="font-medium text-text-primary truncate">${
              pattern.title[state.locale]
            }</div>
            <div class="text-xs text-text-muted truncate">${
              pattern.categoryLabel[state.locale]
            }</div>
          </div>
          ${isSelected ? '<span class="command-shortcut">↵</span>' : ""}
        </div>
      `;
    })
    .join("");

  commandResults.innerHTML = html;
}

function navigateToPattern(slug) {
  closeCommandPalette();
  const element = document.getElementById(slug);
  if (element) {
    element.scrollIntoView({ behavior: "smooth", block: "start" });
    // Highlight the card briefly
    element.classList.add("ring-2", "ring-accent", "ring-offset-2", "ring-offset-bg");
    setTimeout(() => {
      element.classList.remove("ring-2", "ring-accent", "ring-offset-2", "ring-offset-bg");
    }, 2000);
  }
}

// Keyboard Shortcuts
function initKeyboardShortcuts() {
  // Set Cmd/Ctrl key indicator
  const isMac = navigator.platform.toUpperCase().indexOf("MAC") >= 0;
  if (kbdCmd) kbdCmd.textContent = isMac ? "⌘" : "Ctrl";

  document.addEventListener("keydown", (e) => {
    // Command palette: Cmd/Ctrl + K
    if ((e.metaKey || e.ctrlKey) && e.key === "k") {
      e.preventDefault();
      if (commandPalette?.classList.contains("hidden")) {
        openCommandPalette();
      } else {
        closeCommandPalette();
      }
      return;
    }

    // Inside command palette
    if (!commandPalette?.classList.contains("hidden")) {
      if (e.key === "Escape") {
        e.preventDefault();
        closeCommandPalette();
        return;
      }

      if (e.key === "ArrowDown") {
        e.preventDefault();
        state.selectedIndex = Math.min(
          state.selectedIndex + 1,
          commandResults?.children.length - 1 || 0
        );
        updateSelectedCommand();
        return;
      }

      if (e.key === "ArrowUp") {
        e.preventDefault();
        state.selectedIndex = Math.max(state.selectedIndex - 1, 0);
        updateSelectedCommand();
        return;
      }

      if (e.key === "Enter") {
        e.preventDefault();
        const selected = commandResults?.querySelector(".command-item.selected");
        const slug = selected?.dataset.slug;
        if (slug) navigateToPattern(slug);
        return;
      }
    }
  });
}

function updateSelectedCommand() {
  const items = commandResults?.querySelectorAll(".command-item");
  items?.forEach((item, index) => {
    if (index === state.selectedIndex) {
      item.classList.add("selected");
      item.scrollIntoView({ block: "nearest" });
    } else {
      item.classList.remove("selected");
    }
  });
}

// Theme Functions
function initTheme() {
  // Default to dark mode
  const saved = localStorage.getItem("theme");
  if (saved === "light") {
    document.documentElement.classList.remove("dark");
    updateThemeIcon(false);
  }

  themeToggle?.addEventListener("click", toggleTheme);
}

function toggleTheme() {
  const isDark = document.documentElement.classList.toggle("dark");
  localStorage.setItem("theme", isDark ? "dark" : "light");
  updateThemeIcon(isDark);
}

function updateThemeIcon(isDark) {
  const darkIcon = document.getElementById("theme-icon-dark");
  const lightIcon = document.getElementById("theme-icon-light");
  if (isDark) {
    darkIcon?.classList.add("hidden");
    lightIcon?.classList.remove("hidden");
  } else {
    darkIcon?.classList.remove("hidden");
    lightIcon?.classList.add("hidden");
  }
}

// Section Toggle Functions
function toggleSection(button) {
  const content = button.nextElementSibling;
  const icon = button.querySelector("svg");
  const isHidden = content?.classList.contains("hidden");

  if (isHidden) {
    content?.classList.remove("hidden");
    icon?.style.setProperty("transform", "rotate(180deg)");
  } else {
    content?.classList.add("hidden");
    icon?.style.setProperty("transform", "rotate(0deg)");
  }
}

function expandAll() {
  document.querySelectorAll(".section-content").forEach((el) => {
    el.classList.remove("hidden");
  });
  document.querySelectorAll(".section-toggle svg").forEach((el) => {
    el.style.setProperty("transform", "rotate(180deg)");
  });
}

function collapseAll() {
  document.querySelectorAll(".section-content").forEach((el) => {
    el.classList.add("hidden");
  });
  document.querySelectorAll(".section-toggle svg").forEach((el) => {
    el.style.setProperty("transform", "rotate(0deg)");
  });
}

// Copy Functions
function copyToClipboard(slug) {
  const url = `${window.location.origin}${window.location.pathname}#${slug}`;
  navigator.clipboard.writeText(url).then(() => {
    showToast(state.locale === "fr" ? "Lien copié !" : "Link copied!");
  });
}

function copyCode(button) {
  const block = button.closest(".section-content")?.querySelector("pre");
  if (block) {
    navigator.clipboard.writeText(block.textContent).then(() => {
      const original = button.innerHTML;
      button.innerHTML = `
        <svg viewBox="0 0 20 20" fill="currentColor" class="w-4 h-4">
          <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
        </svg>
        <span>${state.locale === "fr" ? "Copié !" : "Copied!"}</span>
      `;
      setTimeout(() => {
        button.innerHTML = original;
      }, 2000);
    });
  }
}

// Toast Notification
function showToast(message) {
  const container = document.getElementById("toast-container");
  if (!container) return;

  const toast = document.createElement("div");
  toast.className = "toast";
  toast.innerHTML = `
    <svg viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5 text-success">
      <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
    </svg>
    <span class="text-sm text-text-primary">${message}</span>
  `;

  container.appendChild(toast);
  setTimeout(() => toast.remove(), 3000);
}

// Category Navigation
function scrollToCategory(slug) {
  if (!slug) return;
  const element = document.getElementById(slug);
  if (element) {
    element.scrollIntoView({ behavior: "smooth", block: "start" });
  }
}

// Close mobile sidebar on resize
window.addEventListener("resize", () => {
  if (window.innerWidth >= 1024) {
    mobileOverlay?.classList.add("hidden");
    document.body.style.overflow = "";
  }
});

// Expose functions globally for inline event handlers
window.toggleSection = toggleSection;
window.expandAll = expandAll;
window.collapseAll = collapseAll;
window.copyToClipboard = copyToClipboard;
window.copyCode = copyCode;
window.closeSidebar = closeSidebar;
window.scrollToCategory = scrollToCategory;
window.navigateToPattern = navigateToPattern;
