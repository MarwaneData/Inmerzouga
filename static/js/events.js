document.addEventListener('DOMContentLoaded', function() {
    // Hero Section Slideshow
    const slides = document.querySelectorAll('.hero-background .slide');
    let currentSlide = 0;

    function nextSlide() {
        slides[currentSlide].classList.remove('active');
        currentSlide = (currentSlide + 1) % slides.length;
        slides[currentSlide].classList.add('active');
    }

    setInterval(nextSlide, 5000);

    // Modal Handling
    const modal = document.querySelector('.event-modal');
 

    // Open modal with event details
    document.querySelectorAll('.read-more-arrow').forEach(arrow => {
        arrow.addEventListener('click', function() {
            const eventItem = this.closest('.event-item');
            const collapse = eventItem.querySelector('.event-collapse');
            const icon = this.querySelector('i');
            
            // Toggle collapse
            collapse.classList.toggle('active');
            
            // Rotate arrow
            if (collapse.classList.contains('active')) {
                icon.classList.replace('fa-chevron-down', 'fa-chevron-up');
                this.style.transform = 'rotate(180deg)';
                
                // Scroll to collapsed content on mobile
                if (window.innerWidth <= 992) {
                    setTimeout(() => {
                        collapse.scrollIntoView({ behavior: 'smooth', block: 'start' });
                    }, 100);
                }
            } else {
                icon.classList.replace('fa-chevron-up', 'fa-chevron-down');
                this.style.transform = 'rotate(0deg)';
            }
            
            // Close other collapses
            document.querySelectorAll('.event-item').forEach(item => {
                if (item !== eventItem) {
                    item.querySelector('.event-collapse').classList.remove('active');
                    const otherIcon = item.querySelector('.read-more-arrow i');
                    otherIcon.classList.replace('fa-chevron-up', 'fa-chevron-down');
                    item.querySelector('.read-more-arrow').style.transform = 'rotate(0deg)';
                }
            });
        });
    });

    // Close modal when clicking outside
    window.addEventListener('click', function(e) {
        if (e.target === modal) {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    });
}); 