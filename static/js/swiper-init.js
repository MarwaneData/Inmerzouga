// Initialize Things Swiper
const thingsSwiper = new Swiper('.things-swiper', {
    slidesPerView: 1,
    spaceBetween: 30,
    loop: true,
    pagination: {
        el: '.things-section .swiper-pagination',
        clickable: true
    },
    navigation: {
        nextEl: '.things-section .swiper-button-next',
        prevEl: '.things-section .swiper-button-prev',
    },
    breakpoints: {
        768: {
            slidesPerView: 2,
        },
        1024: {
            slidesPerView: 3,
        }
    }
});

// Initialize Museums Swiper
const museumsSwiper = new Swiper('.museums-swiper', {
    slidesPerView: 1,
    spaceBetween: 30,
    loop: true,
    pagination: {
        el: '.museums-section .swiper-pagination',
        clickable: true
    },
    navigation: {
        nextEl: '.museums-section .swiper-button-next',
        prevEl: '.museums-section .swiper-button-prev',
    },
    breakpoints: {
        768: {
            slidesPerView: 2,
        },
        1024: {
            slidesPerView: 3,
        }
    }
});

document.addEventListener('DOMContentLoaded', function() {
    // Common Swiper configuration
    const swiperConfig = {
        slidesPerView: 1,
        spaceBetween: 30,
        loop: true,
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        breakpoints: {
            640: {
                slidesPerView: 2,
            },
            1024: {
                slidesPerView: 3,
            }
        }
    };

    // Initialize Things To Do Swiper
    const thingsDoSwiper = new Swiper('.things-do-swiper', {
        ...swiperConfig,
        pagination: {
            el: '.things-section:not(.museums):not(.food) .swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.things-section:not(.museums):not(.food) .swiper-button-next',
            prevEl: '.things-section:not(.museums):not(.food) .swiper-button-prev',
        },
    });

    // Initialize Museums Swiper
    const museumsSwiper = new Swiper('.museums-swiper', {
        ...swiperConfig,
        pagination: {
            el: '.things-section.museums .swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.things-section.museums .swiper-button-next',
            prevEl: '.things-section.museums .swiper-button-prev',
        },
    });

    // Initialize Food Swiper
    const foodSwiper = new Swiper('.food-swiper', {
        ...swiperConfig,
        pagination: {
            el: '.things-section.food .swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.things-section.food .swiper-button-next',
            prevEl: '.things-section.food .swiper-button-prev',
        },
    });
}); 