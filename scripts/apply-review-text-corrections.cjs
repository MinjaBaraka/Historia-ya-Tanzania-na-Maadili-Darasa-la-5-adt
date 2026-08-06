#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const textPath = path.join(root, 'content/i18n/sw-TZ/texts.json');
const texts = JSON.parse(fs.readFileSync(textPath, 'utf8'));

const corrections = [
  ['pg070_n0012', 'mweledezo', 'mwendelezo'],
  ['pg076_n0003', 'alikuchukua', 'alichukua'],
  ['pg076_n0010', 'mbabbu', 'mababu'],
  ['pg076_n0010_easy_read', 'mbabbu', 'mababu'],
  ['pg080_n0030', 'telegranu', 'telegramu'],
  ['pg080_n0030_easy_read', 'telegranu', 'telegramu'],
  ['pg082_n0009', 'kibepori', 'kibepari'],
  ['pg082_n0009_easy_read', 'kibepori', 'kibepari'],
  ['pg094_n0007', 'Lakini pia, laana ni apizo aliloalo mzazi, wakuu wa familia au ukoo kwa Mungu, mizimu na mababu, ili aliyeituka maadili afikwe na ubaya fulani au asipate mema waliyo yakusudia kwa kukuika maadili ya jamii.', 'Lakini pia, laana ni apizo alitoalo mzazi, wakuu wa familia au ukoo kwa Mungu, mizimu na mababu, ili aliyeukiuka maadili afikwe na ubaya fulani au asipate mema waliyoyakusudia kwa kukiuka maadili ya jamii.'],
  ['pg111_n0023', 'kuziiIinda', 'kuzilinda'],
  ['pg111_n0028', 'Ina maanaisha kwamba', 'Ina maana kwamba'],
  ['pg114_n0012', 'Uzalendo haugizwi ni hisia kali za mapenzi kwa nchi zinazotoka moyoni mwa raia mwaminifu.', 'Uzalendo hauigizwi; ni hisia kali za mapenzi kwa nchi zinazotoka moyoni mwa raia mwaminifu.'],
  ['pg114_n0024', 'anayejiti sheria', 'anayetii sheria'],
  ['pg114_n0024_easy_read', 'anayejitia sheria', 'anayetii sheria'],
  ['pg115_n0015', 'kuzikuzza', 'kuzikuza'],
];

for (const [id, before, after] of corrections) {
  if (!texts[id]) throw new Error(`Missing text ID: ${id}`);
  if (texts[id].includes(before)) texts[id] = texts[id].replace(before, after);
  if (!texts[id].includes(after)) throw new Error(`Correction was not applied: ${id}`);
}
delete texts.pg001_n0006;
fs.writeFileSync(textPath, `${JSON.stringify(texts, null, 2)}\n`);

const htmlCorrections = new Map([
  ['pg070_sec001.html', [['mweledezo', 'mwendelezo']]],
  ['pg076_sec001.html', [['alikuchukua', 'alichukua'], ['mbabbu', 'mababu']]],
  ['pg080_sec001.html', [['telegranu', 'telegramu']]],
  ['pg082_sec001.html', [['kibepori', 'kibepari']]],
  ['pg094_sec001.html', [['Lakini pia, laana ni apizo aliloalo mzazi, wakuu wa familia au ukoo kwa Mungu, mizimu na mababu, ili aliyeituka maadili afikwe na ubaya fulani au asipate mema waliyo yakusudia kwa kukuika maadili ya jamii.', 'Lakini pia, laana ni apizo alitoalo mzazi, wakuu wa familia au ukoo kwa Mungu, mizimu na mababu, ili aliyeukiuka maadili afikwe na ubaya fulani au asipate mema waliyoyakusudia kwa kukiuka maadili ya jamii.']]],
  ['pg111_sec001.html', [['kuziiIinda', 'kuzilinda'], ['Ina maanaisha kwamba', 'Ina maana kwamba']]],
  ['pg114_sec001.html', [['Uzalendo haugizwi ni hisia kali za mapenzi kwa nchi zinazotoka moyoni mwa raia mwaminifu.', 'Uzalendo hauigizwi; ni hisia kali za mapenzi kwa nchi zinazotoka moyoni mwa raia mwaminifu.'], ['anayejiti sheria', 'anayetii sheria']]],
  ['pg115_sec001.html', [['kuzikuzza', 'kuzikuza']]],
]);

for (const [file, replacements] of htmlCorrections) {
  const filePath = path.join(root, file);
  let html = fs.readFileSync(filePath, 'utf8');
  for (const [before, after] of replacements) {
    if (html.includes(before)) html = html.replace(before, after);
    if (!html.includes(after)) throw new Error(`HTML correction was not applied: ${file}`);
  }
  fs.writeFileSync(filePath, html);
}

const indexPath = path.join(root, 'index.html');
let index = fs.readFileSync(indexPath, 'utf8');
index = index.replace(/\s*<p data-id="pg001_n0006" class="sr-only">FOR ONLINE READING ONLY<\/p>/, '');
if (index.includes('FOR ONLINE READING ONLY')) throw new Error('Cover-only message remains');
fs.writeFileSync(indexPath, index);

console.log(`Applied ${corrections.length} reviewed text corrections.`);
