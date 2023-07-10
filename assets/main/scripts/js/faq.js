const buttons = document.querySelectorAll(".faq-toggle-btn");
const faq = document.querySelectorAll(".faq");
buttons.addEventListener("click", function () {
    faq.classList.toggle("active");
});