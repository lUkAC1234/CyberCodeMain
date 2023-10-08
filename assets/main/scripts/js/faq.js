const buttons = document.querySelectorAll(".faq-card-title");

buttons.forEach((button) => {
    button.addEventListener('click', () => {
        const faqElement = button.closest('.faq'); // Find the parent .faq element
        faqElement.classList.toggle('active'); // Toggle the 'active' class for this faqElement
    });
});