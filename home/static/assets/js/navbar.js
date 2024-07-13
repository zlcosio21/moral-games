document.addEventListener("DOMContentLoaded", function() {
    var navbar = document.querySelector(".nk-navbar-top");
    var navbarTop = navbar.offsetTop;

    window.addEventListener("scroll", function() {
        if (window.pageYOffset > navbarTop) {
            navbar.classList.add("hidden");
        } else {
            navbar.classList.remove("hidden");
        }
    });
});