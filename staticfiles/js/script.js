document.addEventListener('DOMContentLoaded', function() {
    // Navigation elements
    const dropdowns = document.querySelectorAll('.dropdown');
    const menuItems = document.querySelectorAll('.menu-item');
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    const menuOverlay = document.querySelector('.menu-overlay');

    // Set active state based on current page
    function setActiveNavItem() {
        const currentPath = window.location.pathname;
        const navLinks = document.querySelectorAll('.nav-link');
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === currentPath || 
                (currentPath === '/' && link.getAttribute('href') === '/')) {
                link.classList.add('active');
            }
        });

        // Handle special cases for nested pages
        if (currentPath.includes('/tour/')) {
            document.querySelector('a[href*="tour"]').closest('.dropdown').querySelector('.nav-link').classList.add('active');
        } else if (currentPath.includes('/luxury-camp/')) {
            document.querySelector('a[href*="luxury-camp"]').closest('.dropdown').querySelector('.nav-link').classList.add('active');
        } else if (currentPath.includes('/activities/')) {
            document.querySelector('a[href*="activities"]').closest('.dropdown').querySelector('.nav-link').classList.add('active');
        } else if (currentPath.includes('/events/')) {
            document.querySelector('a[href*="events"]').closest('.dropdown').querySelector('.nav-link').classList.add('active');
        }
    }

    // Initialize active state
    setActiveNavItem();

    // Toggle mobile menu
    navToggle?.addEventListener('click', function() {
        this.classList.toggle('active');
        navMenu.classList.toggle('active');
        
        // Prevent body scroll when menu is open
        document.body.style.overflow = this.classList.contains('active') ? 'hidden' : '';
    });

    // Handle mobile dropdowns
    dropdowns.forEach(dropdown => {
        const link = dropdown.querySelector('.nav-link');
        
        link.addEventListener('click', function(e) {
            if (window.innerWidth <= 1024) {
                e.preventDefault();
                e.stopPropagation();
                
                // Close other dropdowns
                dropdowns.forEach(other => {
                    if (other !== dropdown) {
                        other.classList.remove('active');
                    }
                });
                
                // Toggle current dropdown
                dropdown.classList.toggle('active');
            }
        });
    });

    // Handle dropdown toggles
    dropdowns.forEach(dropdown => {
        const link = dropdown.querySelector('.nav-link');
        const dropdownMenu = dropdown.querySelector('.dropdown-menu');
        
        link.addEventListener('click', function(e) {
            // Only prevent default if it's a "#" link
            if (this.getAttribute('href') === '#') {
                e.preventDefault();
            }
            e.stopPropagation();
            
            // Close other dropdowns
            dropdowns.forEach(other => {
                if (other !== dropdown) {
                    other.querySelector('.dropdown-menu').classList.remove('active');
                    other.querySelector('.nav-link').classList.remove('active');
                }
            });

            // Toggle current dropdown
            this.classList.toggle('active');
            dropdownMenu.classList.toggle('active');
            if (menuOverlay) {
                menuOverlay.classList.toggle('active');
            }
        });
    });

    // Handle submenu toggles
    menuItems.forEach(item => {
        const trigger = item.querySelector('.menu-trigger');
        const submenu = item.querySelector('.submenu');
        
        if (trigger && submenu) {
            trigger.addEventListener('click', function(e) {
                // Only prevent default if it's a "#" link
                if (this.getAttribute('href') === '#') {
                    e.preventDefault();
                }
                e.stopPropagation();
                
                // Close other submenus
                menuItems.forEach(other => {
                    if (other !== item && other.querySelector('.submenu')) {
                        other.querySelector('.submenu').classList.remove('active');
                        other.querySelector('.menu-trigger').classList.remove('active');
                    }
                });

                // Toggle current submenu
                this.classList.toggle('active');
                submenu.classList.toggle('active');
            });
        }
    });

    // Handle navigation to pages from submenu
    document.querySelectorAll('.submenu a').forEach(link => {
        link.addEventListener('click', function(e) {
            e.stopPropagation(); // Prevent bubbling
            // Allow actual navigation
        });
    });

    // Close menus when clicking overlay
    if (menuOverlay) {
        menuOverlay.addEventListener('click', function() {
            // Close all menus
            navMenu.classList.remove('active');
            dropdowns.forEach(dropdown => {
                dropdown.querySelector('.dropdown-menu').classList.remove('active');
                dropdown.querySelector('.nav-link').classList.remove('active');
            });
            menuItems.forEach(item => {
                const submenu = item.querySelector('.submenu');
                const trigger = item.querySelector('.menu-trigger');
                if (submenu && trigger) {
                    submenu.classList.remove('active');
                    trigger.classList.remove('active');
                }
            });
            menuOverlay.classList.remove('active');
            if (navToggle) {
                navToggle.querySelector('i').classList.remove('fa-times');
                navToggle.querySelector('i').classList.add('fa-bars');
            }
        });
    }

    // Close menu when clicking outside
    document.addEventListener('click', function(e) {
        if (window.innerWidth <= 1024) {
            if (!navMenu.contains(e.target) && !navToggle.contains(e.target)) {
                navMenu.classList.remove('active');
                navToggle.classList.remove('active');
                document.body.style.overflow = '';
                
                dropdowns.forEach(dropdown => {
                    dropdown.classList.remove('active');
                });
            }
        }
    });
}); 