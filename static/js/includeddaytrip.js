document.addEventListener('DOMContentLoaded', function() {
    const expandAllBtn = document.querySelector('.expand-all-included');
    const includedItems = document.querySelectorAll('.included-item');
    let isAllExpanded = false;

    // Toggle expand all button
    if (expandAllBtn) {
        expandAllBtn.addEventListener('click', function() {
            isAllExpanded = !isAllExpanded;
            
            // Update button text and icon
            this.classList.toggle('expanded');
            this.firstChild.textContent = isAllExpanded ? 'Collapse All' : 'Expand All';
            
            // Toggle all items
            includedItems.forEach(item => {
                item.classList.toggle('expanded', isAllExpanded);
            });
        });
    }

    // Individual item toggle
    includedItems.forEach(item => {
        const header = item.querySelector('.included-item-header');
        if (header) {
            header.addEventListener('click', function() {
                const isExpanded = item.classList.toggle('expanded');
                
                // Update expand all button state
                if (expandAllBtn) {
                    updateExpandAllState();
                }
            });
        }
    });

    // Function to update expand all button state
    function updateExpandAllState() {
        const allExpanded = Array.from(includedItems).every(item => 
            item.classList.contains('expanded')
        );
        
        expandAllBtn.classList.toggle('expanded', allExpanded);
        expandAllBtn.firstChild.textContent = allExpanded ? 'Collapse All' : 'Expand All';
        isAllExpanded = allExpanded;
    }
}); 