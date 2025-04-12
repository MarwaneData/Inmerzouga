document.addEventListener('DOMContentLoaded', function() {
    const expandAllBtn = document.querySelector('.expand-all-faq');
    const faqItems = document.querySelectorAll('.faq-item');
    let isAllExpanded = false;

    // Toggle expand all button
    expandAllBtn.addEventListener('click', function() {
        isAllExpanded = !isAllExpanded;
        
        // Update button text and icon
        this.classList.toggle('expanded');
        this.firstChild.textContent = isAllExpanded ? 'Collapse All' : 'Expand All';
        
        // Toggle all items
        faqItems.forEach(item => {
            item.classList.toggle('expanded', isAllExpanded);
        });
    });

    // Individual item toggle
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        
        question.addEventListener('click', function() {
            const isExpanded = item.classList.toggle('expanded');
            
            // Update expand all button state
            updateExpandAllState();
        });
    });

    // Function to update expand all button state
    function updateExpandAllState() {
        const allExpanded = Array.from(faqItems).every(item => 
            item.classList.contains('expanded')
        );
        
        expandAllBtn.classList.toggle('expanded', allExpanded);
        expandAllBtn.firstChild.textContent = allExpanded ? 'Collapse All' : 'Expand All';
        isAllExpanded = allExpanded;
    }
}); 