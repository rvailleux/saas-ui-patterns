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
  initBackToTop();
  initSidebarActiveTracking();
  restoreExpandState();
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
const mainContent = document.querySelector("main");
const sidebarExpand = document.getElementById("sidebar-expand");

function initSidebar() {
  // Load saved state
  const saved = localStorage.getItem("sidebarCollapsed");
  if (saved !== null) {
    state.sidebarCollapsed = saved === "true";
    updateSidebarState();
  }

  sidebarToggle?.addEventListener("click", toggleSidebar);
  sidebarExpand?.addEventListener("click", toggleSidebar);
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
    // Shrink main content margin to match collapsed sidebar
    document.documentElement.style.setProperty("--sidebar-width", "var(--sidebar-collapsed)");
  } else {
    sidebar?.classList.remove("collapsed");
    // Restore full sidebar width
    document.documentElement.style.setProperty("--sidebar-width", "240px");
  }
}

function openMobileSidebar() {
  sidebar?.classList.add("mobile-open");
  mobileOverlay?.classList.remove("hidden");
  document.body.style.overflow = "hidden";
}

function closeSidebar() {
  if (window.innerWidth < 1024) {
    sidebar?.classList.remove("mobile-open");
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
  state.selectedIndex = 0;
  commandPalette?.classList.remove("hidden");
  commandInput?.focus();
  renderSearchResults(state.patterns.slice(0, 8));
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

function scrollWithOffset(element) {
  const headerH = document.querySelector("header")?.offsetHeight || 64;
  const top = element.getBoundingClientRect().top + window.scrollY - headerH - 8;
  window.scrollTo({ top, behavior: "smooth" });
}

function navigateToPattern(slug) {
  closeCommandPalette();
  window.location.href = '/' + state.locale + '/patterns/' + slug + '/';
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
  const isDark = localStorage.getItem("theme") === "dark";
  if (isDark) {
    document.documentElement.classList.add("dark");
  } else {
    document.documentElement.classList.remove("dark");
  }
  updateThemeIcon(isDark);
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
function getSectionKey(button) {
  const card = button.closest(".pattern-card");
  const section = button.closest("[data-section]");
  return card && section ? `${card.id}:${section.dataset.section}` : null;
}

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

  const key = getSectionKey(button);
  if (key) sessionStorage.setItem(`section:${key}`, isHidden ? "open" : "closed");
}

function restoreExpandState() {
  document.querySelectorAll(".section-toggle").forEach((button) => {
    const key = getSectionKey(button);
    if (!key) return;
    const saved = sessionStorage.getItem(`section:${key}`);
    if (saved === "open") {
      const content = button.nextElementSibling;
      const icon = button.querySelector("svg");
      content?.classList.remove("hidden");
      icon?.style.setProperty("transform", "rotate(180deg)");
    }
  });
}

function expandAll() {
  document.querySelectorAll(".section-content").forEach((el) => {
    el.classList.remove("hidden");
  });
  document.querySelectorAll(".section-toggle svg").forEach((el) => {
    el.style.setProperty("transform", "rotate(180deg)");
  });
  document.querySelectorAll(".section-toggle").forEach((button) => {
    const key = getSectionKey(button);
    if (key) sessionStorage.setItem(`section:${key}`, "open");
  });
}

function collapseAll() {
  document.querySelectorAll(".section-content").forEach((el) => {
    el.classList.add("hidden");
  });
  document.querySelectorAll(".section-toggle svg").forEach((el) => {
    el.style.setProperty("transform", "rotate(0deg)");
  });
  document.querySelectorAll(".section-toggle").forEach((button) => {
    const key = getSectionKey(button);
    if (key) sessionStorage.setItem(`section:${key}`, "closed");
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
  if (element) scrollWithOffset(element);
}

// Back-to-top FAB
function initBackToTop() {
  const fab = document.getElementById("back-to-top");
  if (!fab) return;
  window.addEventListener("scroll", () => {
    fab.classList.toggle("visible", window.scrollY > 400);
  }, { passive: true });
  fab.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
}

// Sidebar active link tracking via IntersectionObserver
function initSidebarActiveTracking() {
  const sections = document.querySelectorAll("section[id]");
  if (!sections.length) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          document.querySelectorAll(".sidebar-item").forEach((link) => {
            const href = link.getAttribute("href") || "";
            const isActive = href.endsWith(`#${entry.target.id}`);
            link.classList.toggle("active", isActive);
          });
        }
      });
    },
    { rootMargin: "-20% 0px -70% 0px" }
  );

  sections.forEach((section) => observer.observe(section));
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
window.openMobileSidebar = openMobileSidebar;
