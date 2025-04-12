document.addEventListener('DOMContentLoaded', function() {
    const mapImage = document.getElementById('mapImage');
    const mapWrapper = document.getElementById('mapWrapper');
    const zoomInBtn = document.getElementById('zoomIn');
    const zoomOutBtn = document.getElementById('zoomOut');
    const fullscreenBtn = document.getElementById('fullscreen');

    let scale = 1;
    let isDragging = false;
    let startPos = { x: 0, y: 0 };
    let currentTranslate = { x: 0, y: 0 };

    // Zoom Controls
    zoomInBtn.addEventListener('click', () => {
        scale = Math.min(scale * 1.2, 4); // Max zoom 4x
        updateMapTransform();
    });

    zoomOutBtn.addEventListener('click', () => {
        scale = Math.max(scale / 1.2, 1); // Min zoom 1x
        updateMapTransform();
    });

    // Fullscreen Control
    fullscreenBtn.addEventListener('click', () => {
        if (!document.fullscreenElement) {
            mapWrapper.requestFullscreen().catch(err => {
                console.error(`Error attempting to enable fullscreen: ${err.message}`);
            });
        } else {
            document.exitFullscreen();
        }
    });

    // Pan Controls
    mapWrapper.addEventListener('mousedown', startDragging);
    mapWrapper.addEventListener('mousemove', drag);
    mapWrapper.addEventListener('mouseup', stopDragging);
    mapWrapper.addEventListener('mouseleave', stopDragging);

    // Touch Events
    mapWrapper.addEventListener('touchstart', (e) => {
        startDragging(e.touches[0]);
    });
    mapWrapper.addEventListener('touchmove', (e) => {
        e.preventDefault();
        drag(e.touches[0]);
    });
    mapWrapper.addEventListener('touchend', stopDragging);

    function startDragging(e) {
        isDragging = true;
        startPos = {
            x: e.clientX - currentTranslate.x,
            y: e.clientY - currentTranslate.y
        };
    }

    function drag(e) {
        if (!isDragging) return;

        const x = e.clientX - startPos.x;
        const y = e.clientY - startPos.y;

        // Limit panning based on zoom level
        const maxTranslate = (scale - 1) * mapWrapper.offsetWidth / 2;
        currentTranslate = {
            x: Math.max(Math.min(x, maxTranslate), -maxTranslate),
            y: Math.max(Math.min(y, maxTranslate), -maxTranslate)
        };

        updateMapTransform();
    }

    function stopDragging() {
        isDragging = false;
    }

    function updateMapTransform() {
        mapImage.style.transform = `translate(${currentTranslate.x}px, ${currentTranslate.y}px) scale(${scale})`;
    }

    // Reset transform on window resize
    window.addEventListener('resize', () => {
        scale = 1;
        currentTranslate = { x: 0, y: 0 };
        updateMapTransform();
    });
}); 