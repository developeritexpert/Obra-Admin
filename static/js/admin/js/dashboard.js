(function () {
  const ctx = document.getElementById("salesChart");
  const legendContainer = document.getElementById("customLegend");

  if (!ctx || !legendContainer) return;

  const chart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: [
        "Ene",
        "Feb",
        "Mar",
        "Abr",
        "May",
        "Jun",
        "Jul",
        "Ago",
        "Sep",
        "Oct",
        "Nov",
        "Dic",
      ],
      datasets: [
        {
          label: "Ingresos",
          data: [20, 35, 35, 75, 55, 65, 45, 75, 55, 80, 55, 80],
          backgroundColor: "#1B2022",
          barThickness: 7,
        },
        {
          label: "gap",
          data: new Array(12).fill(0),
          backgroundColor: "transparent",
          barThickness: 1,
        },
        {
          label: "Gastos",
          data: [85, 65, 75, 35, 85, 35, 65, 40, 40, 65, 45, 90],
          backgroundColor: "#5F6364",
          barThickness: 7,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
      },
    },
  });

  const legendData = [
    { color: "#1B2022", value: "$9.65K", label: "Ingresos" },
    { color: "#1B2022", value: "$3.75K", label: "Gastos" },
  ];

  legendData.forEach((item) => {
    const legendItem = document.createElement("div");
    legendItem.className = "flex items-center gap-2";

    legendItem.innerHTML = `
      <span style="outline:7px solid ${item.color}" class="w-2 h-2 rounded-full"></span>
      <span style="font-weight:700">${item.value}</span>
      <span style="color:#B7B9BA">/ ${item.label}</span>
    `;

    legendContainer.appendChild(legendItem);
  });
})();

/* SIDEBAR TOGGLE */
const logoutBtn = document.getElementById("logoutBtn");
const hamburger = document.getElementById("hamburger");
const sidebar = document.getElementById("sidebar");

const logoExpanded = sidebar?.querySelector(".sidebar-logo");
const logoCollapsed = sidebar?.querySelector(".sidebar-logo-collapsed");

const desktopQuery = window.matchMedia("(min-width: 1024px)");

hamburger?.addEventListener("click", () => {
  if (!sidebar) return;

  // =====================
  // DESKTOP (>=1024px)
  // =====================
  if (desktopQuery.matches) {
    const isExpanded = sidebar.classList.contains("w-[280px]");

    sidebar.classList.toggle("w-[130px]", isExpanded);
    sidebar.classList.toggle("w-[280px]", !isExpanded);

    sidebar.classList.toggle("2xl:w-[150px]", isExpanded);
    sidebar.classList.toggle("2xl:w-[374px]", !isExpanded);

    sidebar.querySelectorAll(".sidebar-text").forEach((el) => {
      el.classList.toggle("hidden", isExpanded);
    });

    logoExpanded?.classList.toggle("hidden", isExpanded);
    logoCollapsed?.classList.toggle("hidden", !isExpanded);

    logoutBtn?.classList.toggle("border-[3px]", !isExpanded);
    logoutBtn?.classList.toggle("border-[#5F6364]", !isExpanded);

    document.body.classList.toggle("is-collapsed", isExpanded);
  }

  // =====================
  // MOBILE (<1024px)
  // =====================
  else {
    sidebar.classList.toggle("translate-x-0");
    sidebar.classList.toggle("-translate-x-full");
  }
});
const hamburger2 = document.getElementById("hamburger2");

// CLOSE SIDEBAR
hamburger2?.addEventListener("click", () => {
  if (!sidebar) return;

  // Mobile → close
  if (!desktopQuery.matches) {
    sidebar.classList.remove("translate-x-0");
    sidebar.classList.add("-translate-x-full");
  }

  // Desktop → reset to expanded
  else {
    sidebar.classList.remove("w-[130px]", "2xl:w-[150px]");
    sidebar.classList.add("w-[280px]", "2xl:w-[374px]");
  }
});

//sidebar dropdown toggle
document.querySelectorAll(".toggle").forEach((toggle) => {
  toggle.addEventListener("click", function () {
    this.closest(".group").classList.toggle("open");
  });
});

// uploaded image js

$(function () {
  const $input = $("#imageInput");
  const $preview = $("#preview");
  const $dropArea = $("#dropArea");

  function handleFiles(files) {
    Array.from(files).forEach((file) => {
      if (!file.type.startsWith("image/")) return;

      const reader = new FileReader();

      reader.onload = function (e) {
        const img = `
            <div class="relative group">
              <img
                src="${e.target.result}"
                class="h-24 w-full object-cover rounded-md border"
              />
            </div>
          `;
        $preview.append(img);
      };

      reader.readAsDataURL(file);
    });
  }

  // Browse upload
  $input.on("change", function () {
    handleFiles(this.files);
  });

  // Drag over
  $dropArea.on("dragover", function (e) {
    e.preventDefault();
    $(this).addClass("border-blue-500 bg-blue-50");
  });

  // Drag leave
  $dropArea.on("dragleave", function () {
    $(this).removeClass("border-blue-500 bg-blue-50");
  });

  // Drop
  $dropArea.on("drop", function (e) {
    e.preventDefault();
    $(this).removeClass("border-blue-500 bg-blue-50");
    handleFiles(e.originalEvent.dataTransfer.files);
  });
});
//  custom select

$(document).ready(function () {
  // Toggle dropdown (only this select)
  $(".custom-select .select-box").on("click", function (e) {
    e.stopPropagation();

    const $select = $(this).closest(".custom-select");

    // Close others
    $(".custom-select").not($select).find(".options").addClass("hidden");
    $(".custom-select").not($select).find("img").removeClass("rotate-180");

    // Toggle this one
    $select.find(".options").toggleClass("hidden");
    $(this).find("img").toggleClass("rotate-180");
  });

  // Select option (only this select)
  $(".custom-select .option").on("click", function () {
    const $select = $(this).closest(".custom-select");
    const selectedText = $(this).text();

    $select.find(".selected").text(selectedText);
    $select.find(".options").addClass("hidden");
    $select.find("img").removeClass("rotate-180");
  });

  // Close all when clicking outside
  $(document).on("click", function () {
    $(".options").addClass("hidden");
    $(".custom-select img").removeClass("rotate-180");
  });
});

// image preview
$(document).ready(function () {
  $("#fileInput").on("change", function () {
    const preview = $("#preview");
    preview.empty();

    $.each(this.files, function (_, file) {
      if (!file.type.startsWith("image/")) return;

      const img = $("<img>", {
        src: URL.createObjectURL(file),
        class: "rounded border border-gray-200 object-cover",
        css: {
          width: "60px",
          height: "60px",
        },
      });

      preview.append(img);
    });
  });
});

// test editor js

// Simple accordion toggle
document.querySelectorAll(".accordion-btn").forEach((button) => {
  button.addEventListener("click", () => {
    const content = button.nextElementSibling;
    const arrow = button.querySelector("span");
    content.classList.toggle("hidden");
    arrow.classList.toggle("rotate-180"); // arrow flips
  });
});

// text editor
const editor = document.getElementById("editor");
const buttons = document.querySelectorAll("[data-cmd]");
const toggleCode = document.getElementById("toggleCode");
const addLink = document.getElementById("addLink");
const actionButtons = document.querySelectorAll("[data-action]");

let isCode = false;

// Bold / Italic / etc
buttons.forEach((btn) => {
  btn.addEventListener("click", () => {
    editor.focus();
    document.execCommand(btn.dataset.cmd);
  });
});

// Link
addLink.addEventListener("click", () => {
  const url = prompt("Enter URL");
  if (url) {
    editor.focus();
    document.execCommand("createLink", false, url);
  }
});

// Code toggle
toggleCode.addEventListener("click", () => {
  isCode = !isCode;

  if (isCode) {
    editor.textContent = editor.innerHTML;
    editor.setAttribute("contenteditable", false);
  } else {
    editor.innerHTML = editor.textContent;
    editor.setAttribute("contenteditable", true);
  }
});

// -----------------------------
// ICON BUTTON ACTIONS
// -----------------------------
actionButtons.forEach((btn) => {
  btn.addEventListener("click", () => {
    const action = btn.dataset.action;

    switch (action) {
      case "attach":
        attachFile();
        break;

      case "emoji":
        insertEmoji("😊");
        break;

      case "settings":
        openEditorSettings();
        break;
    }
  });
});

// -----------------------------
// FUNCTIONS
// -----------------------------
function attachFile() {
  const input = document.createElement("input");
  input.type = "file";
  input.click();
}

function insertEmoji(emoji) {
  editor.focus();
  document.execCommand("insertText", false, emoji);
}

function openEditorSettings() {
  alert("Editor settings coming soon ⚙️");
}

const editBtn = document.getElementById("editBannerBtn");
const deleteBtn = document.getElementById("deleteBannerBtn");
const bannerImage = document.getElementById("bannerImage");

// Edit (open file picker)
editBtn.addEventListener("click", () => {
  const input = document.createElement("input");
  input.type = "file";
  input.accept = "image/*";

  input.onchange = (e) => {
    const file = e.target.files[0];
    if (file) {
      bannerImage.src = URL.createObjectURL(file);
    }
  };

  input.click();
});

// Delete
deleteBtn.addEventListener("click", () => {
  if (confirm("Are you sure you want to delete the banner image?")) {
    bannerImage.src = "";
    bannerImage.classList.add("hidden");
  }
});

// sections active state
$(document).ready(function () {
  // Hide all sections except first on load
  $(".tab-section").hide();
  $(".tab-section").first().show();

  // Set first menu item active
  $('nav a[href^="#"]').first().addClass("sidebar-active");

  $("nav").on("click", 'a[href^="#"]', function (e) {
    e.preventDefault();

    let target = $(this).attr("href");

    // Remove active from all
    $("nav a").removeClass("sidebar-active");

    // Add active to clicked
    $(this).addClass("sidebar-active");

    // Hide all sections
    $(".tab-section").hide();

    // Show target section
    $(target).fadeIn(200);
  });
});

// sublist tabs
$(document).ready(function () {
  // Hide all website tabs
  $(".websiteTabList").hide();

  // Show first tab by default
  $(".websiteTabList").first().show();
  $(".website-tab-link").first().addClass("website-active");

  // Click handler
  $(".website-tab-link").on("click", function () {
    let target = $(this).data("target");

    // Remove active state
    $(".website-tab-link").removeClass("website-active");

    // Add active to clicked
    $(this).addClass("website-active");

    // Hide all tab content
    $(".websiteTabList").hide();

    // Show selected tab
    $(target).fadeIn(200);
  });
});