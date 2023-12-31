// Функция для проверки, виден ли элемент на экране
function isElementInViewport(el) {
    const rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Функция для обработки события прокрутки страницы
function handleScroll() {
    const targetElement = document.querySelector('.btn-for-list-of-packages');

    if (isElementInViewport(targetElement)) {
        targetElement.classList.add('visible');
    } else {
        targetElement.classList.remove('visible');
    }
}

// Добавляем обработчик события прокрутки
window.addEventListener('scroll', handleScroll);

// Вызываем обработчик события один раз, чтобы проверить видимость элемента при загрузке страницы
handleScroll();