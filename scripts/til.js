"use strict";

// Haha screw everyone without native async/await and Array.flat() amirite
(function() {
  const base =
    "https://raw.githubusercontent.com/1337/yesterday-i-learned/master/";
  const resultsEl = document.getElementById("results");
  const directory = `${base}README.md`;
  let facts;

  async function getFactFiles() {
    const response = await fetch(directory);
    const resp = await response.text();
    return resp
      .split("\n")
      .filter(line => {
        if (line.indexOf("-") === 0) return line;
      })
      .map(line => line.match(/\((.+)\)/)[1]);
  }

  async function getTils(fileName) {
    const fullUrl = `${base}${fileName}`;
    const response = await fetch(fullUrl);
    const resp = await response.text();
    let tils = resp.split("\n");
    tils = tils.map(line => `**${fileName}** ${line}`);
    return tils;
  }

  getFactFiles().then(fileNames => {
    const requests = fileNames.map(getTils);
    Promise.all(requests).then(tils => {
      tils = tils.flat();
      facts = tils;
      fillRandomFact();
    });
  });

  function search(str) {
    if (!(facts && facts.length)) return;
    const hit = new RegExp(`^.*${str}.*$`, "igm");
    return facts.filter(line => {
      if (line.search(hit) > -1) return line;
    });
  }

  function doSearch() {
    const el = document.getElementById("keyword");
    if (!el.value) return;
    if (el.value.length < 3) return;
    const results = search(el.value);
    setTimeout(() => {
      if (results && results.length) {
        resultsEl.innerHTML = markdown.toHTML(results.join("\n"));
      } else {
        resultsEl.innerHTML = "No results";
      }
    }, 0);
  }
  window.doSearch = _.debounce(doSearch, 500);

  function fillRandomFact() {
    if (!(facts && facts.length)) return;
    const randomEl = document.getElementById("random");
    const randomFact = facts[Math.floor(Math.random() * facts.length)];
    randomEl.innerHTML = markdown.toHTML(randomFact);
  }
})();
