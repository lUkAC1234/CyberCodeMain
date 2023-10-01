document.addEventListener("DOMContentLoaded", function () {
    const continueShoppingLink = document.getElementById("continueShoppingLink");

    continueShoppingLink.addEventListener("click", function (e) {
        e.preventDefault();
        history.back();
    });
});