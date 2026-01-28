console.log('HIIIIII' , $("#Panel-content"));

let PanelContent=document.querySelector("#Panel-content")
let PanelTable=document.querySelector("#Panel-table")
document.querySelector("#ForRegionsPanelBtn").addEventListener("click", () => {
  PanelContent.classList.toggle("hidden");
  PanelTable.classList.toggle("hidden")
});

let CatalogPanelContent = document.querySelector("#catalogues-content")
let CatalogPanelTable = document.querySelector("#catalogues-table")

document.querySelector("#ForCataloguesPanelBtn").addEventListener("click", () => {
  CatalogPanelContent.classList.toggle("hidden");
  CatalogPanelTable.classList.toggle("hidden");
});