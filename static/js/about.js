// Intersection Observer for animations
document.addEventListener('DOMContentLoaded', function() {
    // Initialize AOS
    AOS.init({
        duration: 1000,
        once: true,
        offset: 100
    });

    // Enhanced scroll animations
    const observerOptions = {
        threshold: 0.2,
        rootMargin: '0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                
                // Add counter animation for stats
                if (entry.target.classList.contains('story-stats')) {
                    animateStats();
                }
                
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe elements
    document.querySelectorAll('.story-grid, .values-grid, .instagram-grid').forEach(el => {
        observer.observe(el);
    });

    // Stats counter animation
    function animateStats() {
        const stats = document.querySelectorAll('.stat-number');
        stats.forEach(stat => {
            const target = parseInt(stat.textContent);
            let current = 0;
            const increment = target / 50;
            const duration = 1500;
            const step = duration / 50;
            
            const counter = setInterval(() => {
                current += increment;
                if (current >= target) {
                    stat.textContent = target + '+';
                    clearInterval(counter);
                } else {
                    stat.textContent = Math.floor(current) + '+';
                }
            }, step);
        });
    }

    // Parallax effect for story image
    window.addEventListener('scroll', () => {
        const storyImage = document.querySelector('.story-image img');
        if (storyImage) {
            const scrolled = window.pageYOffset;
            const rate = scrolled * 0.3;
            storyImage.style.transform = `translate3d(0, ${rate}px, 0) scale(1.1)`;
        }
    });

    // Instagram grid masonry layout
    const msnry = new Masonry('.instagram-grid', {
        itemSelector: '.insta-post',
        columnWidth: '.insta-post',
        percentPosition: true
    });
}); 