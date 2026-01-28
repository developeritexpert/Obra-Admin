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
addLink?.addEventListener("click", () => {
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

