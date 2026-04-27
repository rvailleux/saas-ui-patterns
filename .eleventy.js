const { execSync } = require("child_process");

module.exports = function (eleventyConfig) {
  // Run Tailwind on build
  eleventyConfig.on("beforeBuild", () => {
    try {
      execSync(
        "npx tailwindcss -i src/assets/css/main.css -o _site/assets/css/main.css --minify",
        {
          stdio: "inherit",
        }
      );
    } catch (e) {
      console.warn("Tailwind build warning:", e.message);
    }
  });

  eleventyConfig.addWatchTarget("src/assets/css/");
  eleventyConfig.addWatchTarget("src/assets/js/");

  eleventyConfig.addPassthroughCopy({ "src/assets/js": "assets/js" });
  eleventyConfig.addPassthroughCopy({ "src/assets/icons": "assets/icons" });
  eleventyConfig.addPassthroughCopy({ "src/assets/images": "assets/images" });
  eleventyConfig.addPassthroughCopy({ "src/assets/manifest.webmanifest": "assets/manifest.webmanifest" });
  eleventyConfig.addPassthroughCopy({ "src/assets/sw.js": "assets/sw.js" });
  eleventyConfig.addPassthroughCopy({
    "node_modules/fuse.js/dist/fuse.min.js": "assets/js/fuse.min.js",
  });

  // Filters
  eleventyConfig.addFilter("slugify", (str) =>
    str
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-|-$/g, "")
  );

  eleventyConfig.addFilter("categoryIcon", (slug) => {
    const icons = {
      navigation: `<svg viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5"><path d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z"/></svg>`,
      layout: `<svg viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5"><path d="M3 4a1 1 0 011-1h12a1 1 0 011 1v2a1 1 0 01-1 1H4a1 1 0 01-1-1V4zm0 6a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H4a1 1 0 01-1-1v-6zm10 0a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z"/></svg>`,
      commands: `<svg viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5"><path d="M3.25 4A2.25 2.25 0 001 6.25v7.5A2.25 2.25 0 003.25 16h7.5A2.25 2.25 0 0013 13.75v-7.5A2.25 2.25 0 0010.75 4h-7.5zM19 4.75a.75.75 0 00-1.28-.53l-3 3a.75.75 0 000 1.06l3 3a.75.75 0 001.28-.53V4.75z"/></svg>`,
      data: `<svg viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5"><path d="M3 3a1 1 0 000 2h11a1 1 0 100-2H3zM3 7a1 1 0 000 2h5a1 1 0 000-2H3zM3 11a1 1 0 100 2h4a1 1 0 100-2H3zM13 16a1 1 0 102 0v-5.586l1.293 1.293a1 1 0 001.414-1.414l-3-3a1 1 0 00-1.414 0l-3 3a1 1 0 101.414 1.414L13 10.414V16z"/></svg>`,
      feedback: `<svg viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5"><path d="M10 2a6 6 0 00-6 6v3.586l-.707.707A1 1 0 004 14h12a1 1 0 00.707-1.707L16 11.586V8a6 6 0 00-6-6zM10 18a3 3 0 01-3-3h6a3 3 0 01-3 3z"/></svg>`,
      "ai-access": `<svg viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5"><path d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z"/></svg>`,
      "ai-generation": `<svg viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>`,
      "ai-context": `<svg viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5"><path d="M9 4.804A7.968 7.968 0 005.5 4c-1.255 0-2.443.29-3.5.804v10A7.969 7.969 0 015.5 14c1.669 0 3.218.51 4.5 1.385A7.962 7.962 0 0114.5 14c1.255 0 2.443.29 3.5.804v-10A7.968 7.968 0 0014.5 4c-1.255 0-2.443.29-3.5.804V12a1 1 0 11-2 0V4.804z"/></svg>`,
      "ai-feedback": `<svg viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5"><path d="M2 10.5a1.5 1.5 0 113 0v6a1.5 1.5 0 01-3 0v-6zM6 10.333v5.43a2 2 0 001.106 1.79l.05.025A4 4 0 008.943 18h5.416a2 2 0 001.962-1.608l1.2-6A2 2 0 0015.56 8H12V4a2 2 0 00-2-2 1 1 0 00-1 1v.667a4 4 0 01-.8 2.4L6.8 7.933a4 4 0 00-.8 2.4z"/></svg>`,
      "ai-prompt": `<svg viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5"><path d="M2 5a2 2 0 012-2h7a2 2 0 012 2v4a2 2 0 01-2 2H9l-3 3v-3H4a2 2 0 01-2-2V5z"/><path d="M15 7v2a4 4 0 01-4 4H9.828l-1.766 1.767c.28.149.599.233.938.233h2l3 3v-3h2a2 2 0 002-2V9a2 2 0 00-2-2h-1z"/></svg>`,
    };
    return icons[slug] || icons["ai-access"];
  });

  // Filter patterns by category
  eleventyConfig.addFilter("filterByCategory", (patterns, category) => {
    return patterns.filter((p) => p.category === category);
  });

  // Find item in array by property
  eleventyConfig.addFilter("find", (arr, prop, value) => {
    return arr?.find((item) => item[prop] === value);
  });

  // Get property from object
  eleventyConfig.addFilter("getProp", (obj, prop) => {
    return obj?.[prop];
  });

  // Previous/Next pattern filters
  eleventyConfig.addFilter("prevPattern", (patterns, slug) => {
    const idx = patterns.findIndex((p) => p.slug === slug);
    return idx > 0 ? patterns[idx - 1] : null;
  });

  eleventyConfig.addFilter("nextPattern", (patterns, slug) => {
    const idx = patterns.findIndex((p) => p.slug === slug);
    return idx < patterns.length - 1 ? patterns[idx + 1] : null;
  });

  return {
    dir: {
      input: "src",
      output: "_site",
      includes: "_includes",
      data: "_data",
    },
    templateFormats: ["njk", "html"],
    htmlTemplateEngine: "njk",
  };
};
