document.addEventListener('DOMContentLoaded', function() {
    const galleryItems = document.querySelectorAll('.gallery-item');
    const lightbox = document.querySelector('.lightbox');
    const lightboxImg = lightbox.querySelector('.lightbox-content img');
    const lightboxCaption = lightbox.querySelector('.lightbox-caption');
    const closeBtn = lightbox.querySelector('.lightbox-close');
    const prevBtn = lightbox.querySelector('.lightbox-arrow.prev');
    const nextBtn = lightbox.querySelector('.lightbox-arrow.next');
    
    let currentIndex = 0;
    const totalImages = galleryItems.length;

    // Function to show image in lightbox
    function showImage(index) {
        const galleryImage = galleryItems[index].querySelector('img');
        const caption = galleryItems[index].querySelector('.overlay-content h3');
        
        lightboxImg.src = galleryImage.src;
        lightboxCaption.textContent = caption ? caption.textContent : '';
        
        // Update navigation visibility
        prevBtn.style.visibility = index === 0 ? 'hidden' : 'visible';
        nextBtn.style.visibility = index === totalImages - 1 ? 'hidden' : 'visible';
        
        currentIndex = index;
    }

    // Open lightbox
    galleryItems.forEach((item, index) => {
        item.addEventListener('click', () => {
            lightbox.classList.add('active');
            document.body.style.overflow = 'hidden'; // Prevent scrolling
            showImage(index);
        });
    });

    // Close lightbox
    function closeLightbox() {
        lightbox.classList.remove('active');
        document.body.style.overflow = ''; // Restore scrolling
    }

    closeBtn.addEventListener('click', closeLightbox);
    
    // Close on overlay click
    lightbox.addEventListener('click', (e) => {
        if (e.target === lightbox) {
            closeLightbox();
        }
    });

    // Previous image
    prevBtn.addEventListener('click', () => {
        if (currentIndex > 0) {
            showImage(currentIndex - 1);
        }
    });

    // Next image
    nextBtn.addEventListener('click', () => {
        if (currentIndex < totalImages - 1) {
            showImage(currentIndex + 1);
        }
    });

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (!lightbox.classList.contains('active')) return;
        
        switch(e.key) {
            case 'Escape':
                closeLightbox();
                break;
            case 'ArrowLeft':
                if (currentIndex > 0) {
                    showImage(currentIndex - 1);
                }
                break;
            case 'ArrowRight':
                if (currentIndex < totalImages - 1) {
                    showImage(currentIndex + 1);
                }
                break;
        }
    });

    // Smooth scroll for hero scroll button
    document.querySelector('.hero-scroll').addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    });
}); 