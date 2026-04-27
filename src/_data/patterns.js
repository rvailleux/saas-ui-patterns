'use strict';

const fs   = require('fs');
const path = require('path');

module.exports = function () {
  const dir = path.join(__dirname, 'patterns');
  return fs
    .readdirSync(dir)
    .filter(f => f.endsWith('.json'))
    .map(f => JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8')))
    .sort((a, b) => a.id - b.id);
};
