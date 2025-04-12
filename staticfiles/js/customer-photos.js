document.addEventListener('DOMContentLoaded', function() {
    const sliderTrack = document.querySelector('.slider-track');
    const slides = document.querySelectorAll('.slide');
    const prevButton = document.querySelector('.slider-nav.prev');
    const nextButton = document.querySelector('.slider-nav.next');
    
    let currentIndex = 0;
    let slidesPerView = getSlidesPerView();

    // Update slides per view on window resize
    window.addEventListener('resize', () => {
        slidesPerView = getSlidesPerView();
        goToSlide(currentIndex);
    });

    // Function to determine slides per view based on screen width
    function getSlidesPerView() {
        if (window.innerWidth <= 767) return 1;
        if (window.innerWidth <= 1170) return 2;
        return 3;
    }

    // Function to update slide position
    function goToSlide(index) {
        const slideWidth = slides[0].offsetWidth + 16; // Include margin
        const maxIndex = slides.length - slidesPerView;
        
        // Ensure index stays within bounds
        currentIndex = Math.max(0, Math.min(index, maxIndex));
        
        // Update transform
        sliderTrack.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
        
        // Update button states
        prevButton.style.opacity = currentIndex === 0 ? '0.5' : '1';
        nextButton.style.opacity = currentIndex === maxIndex ? '0.5' : '1';
    }

    // Previous slide
    prevButton.addEventListener('click', () => {
        goToSlide(currentIndex - 1);
    });

    // Next slide
    nextButton.addEventListener('click', () => {
        goToSlide(currentIndex + 1);
    });

    // Initialize slider
    goToSlide(0);
}); 