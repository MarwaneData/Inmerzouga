document.addEventListener('DOMContentLoaded', function() {
    // Create Google Translate Script
    const script = document.createElement('script');
    script.src = '//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
    document.body.appendChild(script);

    // Initialize Google Translate
    window.googleTranslateElementInit = function() {
        new google.translate.TranslateElement(
            {
                pageLanguage: 'en',
                includedLanguages: 'en,es,it',
                autoDisplay: false
            },
            'google_translate_element'
        );
        
        // Check for saved language preference
        const savedLang = localStorage.getItem('selectedLanguage');
        if (savedLang) {
            setTimeout(() => {
                doGTranslate(`en|${savedLang}`);
            }, 1000);
        }
    };

    // Add click handlers for language selection
    const langItems = document.querySelectorAll('.lang-item');
    langItems.forEach(item => {
        item.addEventListener('click', function() {
            const lang = this.getAttribute('data-lang');
            if (lang === 'english') {
                // Reset to original English
                window.location.reload();
            }
        });
    });
});

function doGTranslate(lang_pair) {
    if (window.gt && window.gt._) {
        window.gt._(lang_pair);
    } else {
        const gtConstElem = document.querySelector('.goog-te-combo');
        if (gtConstElem) {
            gtConstElem.value = lang_pair.split('|')[1];
            gtConstElem.dispatchEvent(new Event('change'));
        }
    }
    
    // Add language class to body
    const selectedLang = lang_pair.split('|')[1];
    document.body.classList.remove('lang-en', 'lang-es', 'lang-it');
    document.body.classList.add(`lang-${selectedLang}`);
    
    // Save language preference
    localStorage.setItem('selectedLanguage', selectedLang);
} 