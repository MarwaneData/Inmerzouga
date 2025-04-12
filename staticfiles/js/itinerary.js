document.addEventListener('DOMContentLoaded', function() {
    const collapseAllBtn = document.querySelector('.collapse-all');
    const dayItems = document.querySelectorAll('.itinerary-item');
    let isExpanded = false;

    // Toggle collapse all button
    collapseAllBtn.addEventListener('click', function() {
        isExpanded = !isExpanded;
        
        // Update button text and icon
        this.classList.toggle('expanded');
        this.firstChild.textContent = isExpanded ? 'Expand all days' : 'Collapse all days';
        
        // Toggle all day items
        dayItems.forEach(item => {
            item.classList.toggle('expanded', isExpanded);
            updateToggleButton(item, isExpanded);
        });
    });

    // Individual day item toggle
    dayItems.forEach(item => {
        const toggleBtn = item.querySelector('.item-toggle');
        toggleBtn.addEventListener('click', function() {
            const isItemExpanded = item.classList.toggle('expanded');
            updateToggleButton(item, isItemExpanded);
            
            // Update collapse all button if all items are expanded/collapsed
            updateCollapseAllButton();
        });
    });

    // Function to update individual toggle button text and icon
    function updateToggleButton(item, isExpanded) {
        const toggleBtn = item.querySelector('.item-toggle');
        const toggleText = toggleBtn.querySelector('span');
        toggleText.textContent = isExpanded ? 'See less' : 'See more';
    }

    // Function to update collapse all button state
    function updateCollapseAllButton() {
        const allExpanded = Array.from(dayItems).every(item => 
            item.classList.contains('expanded')
        );
        
        collapseAllBtn.classList.toggle('expanded', allExpanded);
        collapseAllBtn.firstChild.textContent = allExpanded ? 'Expand all days' : 'Collapse all days';
        isExpanded = allExpanded;
    }
}); 