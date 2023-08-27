(function ($) {
    "use strict";

    $(".carousel-slide-container").owlCarousel({
        smartSpeed: 1000,
        loop: true,
        center: true,
        dots: false,
        nav: true,
        navText : [
            '<i class="fa-sharp fa-solid fa-circle-chevron-left carouselPrev"></i>',
            '<i class="fa-sharp fa-solid fa-circle-chevron-right carouselNext"></i>'
        ],
        responsive: {
            0:{
                items:1
            },

            450:{
                items: 1.3
            },

            600:{
                items:1.5
            },
            1000:{
                items:2
            },
            1300:{
                items:3
            },
            2000:{
                items:4
            },

            3000:{
                items:5
            },
        }
    });

    $(".feedback-container").owlCarousel({
        smartSpeed: 1000,
        loop: true,
        center: true,
        dots: false,
        margin: 10,
        nav: true,
        navText : [
            '<i class="fa-sharp fa-solid fa-circle-chevron-left feedbackPrev"></i>',
            '<i class="fa-sharp fa-solid fa-circle-chevron-right feedbackNext"></i>'
        ],
        responsive: {
            0:{
                items: 1.25
            },
            600:{
                items: 2
            },
            992:{
                items: 1.1
            },
            1300:{
                items:1.1
            },

            2000:{
                items: 1.5
            },
            3000:{
                items: 2
            },
            4000:{
                items: 1.1
            }
        }
    });

    $(".featured-categories-wrapper").owlCarousel({
        smartSpeed: 1000,
        loop: false,
        center: false,
        dots: false,
        nav: true,
        margin: 10,
        navText : [
            '<i class="fa-sharp fa-solid fa-circle-chevron-left feedbackPrev"></i>',
            '<i class="fa-sharp fa-solid fa-circle-chevron-right feedbackNext"></i>'
        ],
        responsive: {
            0:{
                items: 2,
            },

            425:{
                items: 3,
            },

            801: {
                items: 5
            },

            1301:{
                items: 3,
            }
        }
    });
    
})(jQuery);



