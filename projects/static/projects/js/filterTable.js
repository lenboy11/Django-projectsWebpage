const selectorCountry = document.getElementById("selectCountry");
const selectorLanguage = document.getElementById("selectLanguage");
const searchTitle = document.getElementById("search-title");
const table = document.getElementById("tableData");
const tBody = table.tBodies[0];
const rows = Array.from(tBody.querySelectorAll("tr"));

selectorCountry.addEventListener("change", () => {
  filterTable();
});
selectorLanguage.addEventListener("change", () => {
  filterTable();
});
searchTitle.addEventListener("change", () => {
  filterTable();
});
searchTitle.addEventListener("keyup", () => {
  filterTable();
});

function filterTable() {
  const titl = searchTitle.value.toLowerCase();
  const coun = selectorCountry.value;
  const lang = selectorLanguage.value;
  const filteredRows = rows.filter(function (val) {
    const t = val.children[0].firstChild.innerText.toLowerCase();
    const c = val.children[1].innerText;
    const l = val.children[2].innerText;
    return (
      (titl == "" || t.includes(titl)) &&
      (coun == "All" || coun == c) &&
      (lang == "All" || lang == l)
    );
  });

  while (tBody.firstChild) {
    tBody.removeChild(tBody.firstChild);
  }
  tBody.append(...filteredRows);
}
