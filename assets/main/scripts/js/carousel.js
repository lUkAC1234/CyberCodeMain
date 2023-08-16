    // Carousel No image function 

    const imageContainers = document.querySelectorAll('.image-container');

    imageContainers.forEach(container => {
        const img = container.querySelector('img');
        const noImageMessage = container.querySelector('.noImageMessage');

        img.onerror = function () {
            img.style.display = 'none';
            noImageMessage.style.display = 'flex';
        };
    });

    // End Carousel No image function 

    // Carousel function

    const carousel = document.querySelector('.carousel');
    const prevButton = document.querySelector('.carousel-prev');
    const nextButton = document.querySelector('.carousel-next');
    const totalSlides = carousel.children.length;

    let slideWidth = 0;

    function calculateSlideWidth() {
        const firstSlide = carousel.querySelector('.carousel-slide');
        if (firstSlide) {
            slideWidth = firstSlide.clientWidth;
            if (window.innerWidth < 500) { // Mobile
                slideWidth += 0.4 * 16;
            } else if (window.innerWidth < 768) {
                slideWidth += 1 * 16;
            }
        }
    }

    calculateSlideWidth();

    let touchStartX = 0;
    let touchEndX = 0;
    let dragging = false;
    let currentIndex = 0;

    function showSlide(index) {
        console.log('Count: ', index)
        currentIndex = Math.min(Math.max(index, 0), totalSlides - 1);
        const translateValue = -currentIndex * slideWidth;
        carousel.style.transform = `translateX(${translateValue}px)`;
    }

    function handleTouchStart(event) {
        touchStartX = event.touches[0].clientX;
        dragging = true;
    }

    function handleTouchMove(event) {
        if (!dragging) return;
        touchEndX = event.touches[0].clientX;
    }

    function handleTouchEnd() {
        if (!dragging) return;
        dragging = false;

        const touchDiff = touchStartX - touchEndX;

        if (touchDiff > 50) {
            showSlide(currentIndex + 1); // Change to +1 for one slide forward
        } else if (touchDiff < -50) {
            showSlide(currentIndex - 1); // Change to -1 for one slide backward
        }
    }

    function handleMouseDown(event) {
        touchStartX = event.clientX;
        dragging = true;
        document.addEventListener('mousemove', handleMouseMove);
        document.addEventListener('mouseup', handleMouseUp);
    }

    function handleMouseMove(event) {
        if (!dragging) return;
        touchEndX = event.clientX;
    }

    function handleMouseUp() {
        if (!dragging) return;
        dragging = false;
        document.removeEventListener('mousemove', handleMouseMove);
        document.removeEventListener('mouseup', handleMouseUp);

        const touchDiff = touchStartX - touchEndX;

        if (touchDiff > 50) {
            showSlide(currentIndex + 1); // Change to +1 for one slide forward
        } else if (touchDiff < -50) {
            showSlide(currentIndex - 1); // Change to -1 for one slide backward
        }
    }

    window.addEventListener('resize', calculateSlideWidth);
    nextButton.addEventListener('click', () => showSlide(currentIndex + 1)); // Change to +1 for one slide forward
    prevButton.addEventListener('click', () => showSlide(currentIndex - 1)); // Change to -1 for one slide backward
    carousel.addEventListener('touchstart', handleTouchStart);
    carousel.addEventListener('touchmove', handleTouchMove);
    carousel.addEventListener('touchend', handleTouchEnd);
    carousel.addEventListener('mousedown', handleMouseDown);

    showSlide(currentIndex);



// Uncomment the following lines if you want to enable autoplay
// const autoplayInterval = 300; // Adjust as needed
// let autoplayTimer;
// function startAutoplay() {
//   autoplayTimer = setInterval(() => {
//     nextSlide();
//   }, autoplayInterval);
// }
// function stopAutoplay() {
//   clearInterval(autoplayTimer);
// }
// startAutoplay();
// carousel.addEventListener('mouseenter', stopAutoplay);
// carousel.addEventListener('mouseleave', startAutoplay);


// End Carousel function