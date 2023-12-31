let modal = document.getElementById("myModal");
let modalContent = document.getElementById("modalContent");
let modalUser = document.getElementById("modalUser");
let closeModalBtn = document.getElementById("closeModal");
let body = document.body;

var slides = document.querySelectorAll(".feedback-slide");

slides.forEach(function (slide) {
    slide.addEventListener("click", function () {
        let feedbackText = this.querySelector(".feedback-content-text").getAttribute("data-text");
        let userImage = this.querySelector(".feedback-user-container").getAttribute("data-image");
        let user = this.querySelector('.feedback-username').textContent;
        let createdAt = this.getAttribute("data-created-at");
        modalContent.textContent = feedbackText;
        modalUserImage.src = userImage;
        modalUser.textContent = user
        modalCreatedAt.textContent = createdAt;

        modal.style.transform = "scaleY(1)";
        body.style.overflowY = "hidden";
    });
});

function closeModal() {
    modal.style.transform = "scaleY(0)";
    body.style.overflowY = "auto";
}

closeModalBtn.addEventListener("click", closeModal);

window.addEventListener("click", function (event) {
    if (event.target == modal) { closeModal(); }
});
window.addEventListener("touchstart", function (event) {
    if (event.target == modal) { closeModal(); }
});
