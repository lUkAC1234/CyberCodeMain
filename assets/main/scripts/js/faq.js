const buttons = document.querySelectorAll(".faq-toggle-btn");
const faq = document.querySelectorAll(".faq");

buttons.forEach((button) => {
    button.addEventListener('click', () =>
        button.parentElement.classList.toggle('active')
    )
})
