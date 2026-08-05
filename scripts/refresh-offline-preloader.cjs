#!/usr/bin/env node
/**
 * Refresh the JSON data embedded in the offline reader preloader.
 *
 * The preloader intercepts fetches, so these copies must stay in sync with
 * their source files whenever the reading spine or localized content changes.
 */
const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const preloaderPath = path.join(root, "assets", "offline-preloader.js");
const sources = [
  "assets/config.json",
  "content/pages.json",
  "content/toc.json",
  "content/i18n/sw-TZ/texts.json",
  "content/i18n/sw-TZ/audios.json",
  "content/i18n/sw-TZ/videos.json",
  "content/i18n/sw-TZ/images.json",
  "content/i18n/sw-TZ/glossary.json",
  "content/i18n/sw-TZ/timecode/timecode_output.json",
];

const source = fs.readFileSync(preloaderPath, "utf8");
const startMarker = "var INLINE = ";
const endMarker = ";\n  var BASE_DIR";
const start = source.indexOf(startMarker);
const end = source.indexOf(endMarker, start);
if (start < 0 || end < 0) throw new Error("Could not locate embedded preloader data.");

const inline = JSON.parse(source.slice(start + startMarker.length, end));
for (const relativePath of sources) {
  const diskPath = path.join(root, relativePath);
  if (!fs.existsSync(diskPath)) continue;
  inline[`./${relativePath}`] = JSON.parse(fs.readFileSync(diskPath, "utf8"));
}

fs.writeFileSync(
  preloaderPath,
  `${source.slice(0, start + startMarker.length)}${JSON.stringify(inline)}${source.slice(end)}`,
);
console.log(`Refreshed ${sources.length} offline-preloader data sources.`);
