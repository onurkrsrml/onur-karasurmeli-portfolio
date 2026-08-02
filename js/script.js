// Onur Karasurmeli — Portfolio
// Small shared behaviours: active nav state + mobile nav toggle.

document.addEventListener("DOMContentLoaded", function () {
  var currentPage = document.body.getAttribute("data-page");

  document.querySelectorAll(".sidenav a[data-page]").forEach(function (link) {
    if (link.getAttribute("data-page") === currentPage) {
      link.classList.add("is-active");
    }
  });

  var toggle = document.querySelector(".mobile-topbar__toggle");
  var nav = document.querySelector(".sidenav");

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      nav.classList.toggle("is-open");
    });
  }
});
