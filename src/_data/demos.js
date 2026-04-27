'use strict';

const fs   = require('fs');
const path = require('path');

module.exports = function () {
  const dir    = path.join(__dirname, 'demos');
  const result = {};

  fs.readdirSync(dir)
    .filter(f => f.endsWith('.html'))
    .forEach(f => {
      const slug     = path.basename(f, '.html');
      const html     = fs.readFileSync(path.join(dir, f), 'utf8');
      const metaPath = path.join(dir, `${slug}.json`);
      const meta     = fs.existsSync(metaPath)
        ? JSON.parse(fs.readFileSync(metaPath, 'utf8'))
        : {};
      result[slug]   = { ...meta, html };
    });

  return result;
};
