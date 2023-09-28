let modal = document.getElementById("myModal");
let modalContent = document.getElementById("modalContent");
let modalUser = document.getElementById("modalUser");
let closeModal = document.getElementById("closeModal");
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

        modal.style.display = "grid";
        body.style.overflowY = "hidden";
    });
});

closeModal.addEventListener("click", function () {
    modal.style.display = "none";
    body.style.overflowY = "auto";
});

// Close the modal window when clicking outside the window
window.addEventListener("click", function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
        body.style.overflowY = "auto";
    }
});
