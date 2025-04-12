from .models import Tour, LuxuryCamp, City, Contact

def navigation_context(request):
    return {
        'nav_private_tours': Tour.objects.filter(is_group=False, is_active=True),
        'nav_group_tours': Tour.objects.filter(is_group=True, is_active=True),
        'nav_luxury_camps': LuxuryCamp.objects.filter(is_active=True),
        'footer_cities': City.objects.filter(is_active=True)[:3],
        'footer_tours': Tour.objects.filter(is_active=True).order_by('order')[:3],  # Using order field instead of views
    }

def contact_info(request):
    """Add contact information to all templates"""
    contact = Contact.objects.filter(is_active=True).first()
    return {
        'contact': contact
    }
  
