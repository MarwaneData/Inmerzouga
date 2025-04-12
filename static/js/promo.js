// Check if user has closed the popup before
function hasClosedPromo() {
    return localStorage.getItem('promoPopupClosed');
}

// Set popup as closed in localStorage
function closePromo(event) {
    if (event) {
        event.preventDefault();
        event.stopPropagation();
    }
    const popup = document.getElementById('promoPopup');
    popup.classList.remove('show');
    setTimeout(() => {
        popup.style.display = 'none';
    }, 500); // Wait for transition to complete
    localStorage.setItem('promoPopupClosed', 'true');
}

// Show the popup
function showPromo() {
    const popup = document.getElementById('promoPopup');
    if (popup) {
        popup.style.display = 'block';
        // Force reflow
        popup.offsetHeight;
        popup.classList.add('show');
    }
}

// Update countdown timer
function updateTimer() {
    const timerElement = document.getElementById('timer');
    if (!timerElement) return;

    const endDateStr = timerElement.getAttribute('data-end-date');
    if (!endDateStr) return;

    const now = new Date();
    const endDate = new Date(endDateStr);
    
    const diff = endDate - now;
    
    // If promotion has ended
    if (diff <= 0) {
        closePromo();
        return;
    }
    
    // Calculate remaining time
    const hours = Math.floor(diff / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((diff % (1000 * 60)) / 1000);
    
    // Update the display
    timerElement.textContent = 
        `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
}

// Initialize promo popup
document.addEventListener('DOMContentLoaded', function() {
    const popup = document.getElementById('promoPopup');
    const closeButton = document.querySelector('.close-promo');
    
    // Clear localStorage for testing (remove this in production)
    localStorage.removeItem('promoPopupClosed');
    
    if (closeButton) {
        closeButton.addEventListener('click', closePromo);
    }

    if (!hasClosedPromo() && popup) {
        // Show popup after 3 seconds
        setTimeout(showPromo, 3000);
    }
    
    // Update timer every second
    setInterval(updateTimer, 1000);
    updateTimer();
}); 