const profileImage = document.querySelector('.profile-image');
const profileUploadInput = document.querySelector('.profile-upload-input');

profileUploadInput.addEventListener('change', (event) => {
    profileImage.src = URL.createObjectURL(event.target.files[0]);
});