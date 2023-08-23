const englishButton = document.getElementById('englishButton');
const russianButton = document.getElementById('russianButton');
const englishContent = document.querySelector('.english-content');
const russianContent = document.querySelector('.russian-content');

englishButton.addEventListener('click', () => {
    englishButton.classList.add('active');
    russianButton.classList.remove('active');
    englishContent.style.display = 'block';
    russianContent.style.display = 'none';
});

russianButton.addEventListener('click', () => {
    russianButton.classList.add('active');
    englishButton.classList.remove('active');
    russianContent.style.display = 'block';
    englishContent.style.display = 'none';
});
