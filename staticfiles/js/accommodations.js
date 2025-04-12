document.addEventListener('DOMContentLoaded', function() {
    const expandAllBtn = document.querySelector('.expand-all-accommodations');
    const accommodationItems = document.querySelectorAll('.accommodation-item');
    let isAllExpanded = false;

    // Toggle expand all button
    expandAllBtn.addEventListener('click', function() {
        isAllExpanded = !isAllExpanded;
        
        // Update button text and icon
        this.classList.toggle('expanded');
        this.firstChild.textContent = isAllExpanded ? 'Collapse All' : 'Expand All';
        
        // Toggle all items
        accommodationItems.forEach(item => {
            item.classList.toggle('expanded', isAllExpanded);
        });
    });

    // Individual item toggle
    accommodationItems.forEach(item => {
        const header = item.querySelector('.accommodation-item-header');
        
        header.addEventListener('click', function() {
            const isExpanded = item.classList.toggle('expanded');
            
            // Update expand all button state
            updateExpandAllState();
        });
    });

    // Function to update expand all button state
    function updateExpandAllState() {
        const allExpanded = Array.from(accommodationItems).every(item => 
            item.classList.contains('expanded')
        );
        
        expandAllBtn.classList.toggle('expanded', allExpanded);
        expandAllBtn.firstChild.textContent = allExpanded ? 'Collapse All' : 'Expand All';
        isAllExpanded = allExpanded;
    }

    // Handle external links
    const viewMoreLinks = document.querySelectorAll('.view-more-link');
    viewMoreLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            window.open(this.href, '_blank');
        });
    });
}); 