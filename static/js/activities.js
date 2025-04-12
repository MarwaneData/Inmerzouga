document.addEventListener('DOMContentLoaded', () => {
    // Get all learn more buttons
    const learnMoreButtons = document.querySelectorAll('.learn-more');
    const closeModalButtons = document.querySelectorAll('.close-modal');
    const modals = document.querySelectorAll('.activity-modal');

    // Function to open modal
    const openModal = (modal) => {
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';
        setTimeout(() => {
            modal.classList.add('active');
        }, 10);
    };

    // Function to close modal
    const closeModal = (modal) => {
        modal.classList.remove('active');
        setTimeout(() => {
            modal.style.display = 'none';
            document.body.style.overflow = '';
        }, 300);
    };

    // Add click event to learn more buttons
    learnMoreButtons.forEach((button, index) => {
        button.addEventListener('click', () => {
            const modal = modals[index];
            if (modal) {
                openModal(modal);
            }
        });
    });

   
    // Add click event to close buttons
    closeModalButtons.forEach(button => {
        button.addEventListener('click', () => {
            const modal = button.closest('.activity-modal');
            if (modal) {
                closeModal(modal);
            }
        });
    });

    // Close modal when clicking outside
    modals.forEach(modal => {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                closeModal(modal);
            }
        });
    });

    // Close modal with escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            modals.forEach(modal => {
                if (modal.classList.contains('active')) {
                    closeModal(modal);
                }
            });
        }
    });

    // Add smooth scroll for navigation
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add intersection observer for animation
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe activity cards for animation
    document.querySelectorAll('.activity-card').forEach(card => {
        observer.observe(card);
    });
}); 