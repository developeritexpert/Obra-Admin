$(document).ready(function () {
  const $toggle = $("#products-toggle");
  const $menu = $("#products-menu");
  const $arrow = $("#products-arrow");

  if (!$toggle.length || !$menu.length) return;

  const activePages = [
    "products",
    "inventory",
    "collections",
    "purchase_orders",
  ];

  const currentPage = $("body").data("page");

  if (activePages.includes(currentPage)) {
    $menu.removeClass("hidden");
    $arrow.addClass("rotate-90");
  }

  $toggle.on("click", function () {
    $menu.toggleClass("hidden");
    $arrow.toggleClass("rotate-90");
  });
});
