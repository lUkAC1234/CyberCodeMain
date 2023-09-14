/* HEADER-NAVBAR + BOTTOM BTN TO TOP */
var className = "header-active";
var BtnTop = "btn-top-active";
var scrollTrigger = 60;
var scrollBtn = 600;
const backToTopButton = document.getElementById('back-to-top');
const siteProgressBar = document.getElementById('progress');
window.onscroll = function() {
    if (window.scrollY >= scrollTrigger || window.pageYOffset >= scrollTrigger) {
        document.getElementById("header").classList.add(className);
        siteProgressBar.classList.remove("progress-hidden");
        siteProgressBar.style.background = 'var(--progress-background)';
    } else {
        document.getElementById("header").classList.remove(className);
        siteProgressBar.classList.add("progress-hidden");
    }
    
    if (window.scrollY >= scrollBtn || window.pageYOffset >= scrollBtn) {
        document.getElementById("btn-top-container").classList.add(BtnTop);
    } else {
        document.getElementById("btn-top-container").classList.remove(BtnTop);
    }
};

// Smooth scroll to the top when the button is clicked
backToTopButton.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});


// HIDE THE HEADER WHEN USER SCROOLS DOWN 
const siteHeader = document.getElementById('header');
const dropdownMenu = document.getElementById('dropdown__menu');
let lastScrollPosition = 0;
const screenWidthThreshold = 1400;
window.addEventListener('scroll', () => {
if (window.innerWidth <= screenWidthThreshold) {
    siteHeader.style.transform = 'translateY(0)';
} else {
    const currentScrollPosition = window.scrollY;
    if (currentScrollPosition > lastScrollPosition) {
    // Scrolling down
    siteHeader.style.transform = 'translateY(-100%)';
    siteProgressBar.style.bottom = '0';
    siteProgressBar.style.top = 'unset';
    siteProgressBar.style.transform = 'translateY(5px)';
    if (dropdownMenu) {
        dropdownMenu.style.transform = 'translateY(-120%)';
    }
    } else {
        // Scrolling up
        siteHeader.style.transform = 'translateY(0)';
        siteProgressBar.style.top = '0';
        siteProgressBar.style.bottom = 'unset';
        siteProgressBar.style.transform = 'translateY(0px)';
        if (dropdownMenu) {
            dropdownMenu.style.transform = 'translateY(0)';
        }
    }
    lastScrollPosition = currentScrollPosition; 
}
});
    
/* HEADER-NAVBAR + BOTTOM BTN TO TOP END */

/*  HEADER ACTIVE CLASS FUNCTION START */
const navLinks = document.querySelectorAll('.nav-link');

navLinks.forEach(link => {
    if (link.href === window.location.href) {
        link.classList.toggle('active');
    }
});

/*=============== DROPDOWN JS ===============*/
const dropdownProfileImage = document.getElementById('dropdownProfileImage');
const showDropdown = (content, button) =>{
    const dropdownContent = document.getElementById(content),
            dropdownButton = document.getElementById(button);

    dropdownButton.addEventListener('click', () =>{
        dropdownContent.classList.toggle('show-dropdown');
        dropdownProfileImage.classList.toggle('active');
    })
}

showDropdown('dropdown-content','dropdown-button')

/*  HEADER ACTIVE CLASS FUNCTION END */