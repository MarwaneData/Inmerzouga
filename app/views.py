from django.shortcuts import render, get_object_or_404
from .models import (
    Tour, LuxuryCamp, ActivitiesPage, Activity, DayTrip, Package, 
    City, PhotographyPage, AboutPage, PhotographyImage,
    EventsPage, Event, HomePage, HomeSlider, ThingsToDoSection, MuseumSection, FoodSection, Promo
)
from django.db import models
from django.http import HttpResponse
from django.utils import timezone
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.shortcuts import redirect

def manual_sitemap(request):
    return render(request, 'sitemap.xml', content_type="application/xml")

def get_seo_context(page_obj):
    """
    Helper function to get SEO data from any model that inherits from SEOModel
    Returns a dict with all SEO fields
    """
    seo_data = {
        'meta_title': page_obj.meta_title if page_obj.meta_title else "Inmerzouga - Morocco Desert Tours & Experiences",
        'meta_description': page_obj.meta_description,
        'meta_keywords': page_obj.meta_keywords,
        'og_title': page_obj.og_title,
        'og_description': page_obj.og_description,
        'og_image': page_obj.og_image if page_obj.og_image else None,
        'og_type': page_obj.og_type,
        'twitter_card': page_obj.twitter_card,
        'twitter_title': page_obj.twitter_title,
        'twitter_description': page_obj.twitter_description,
        'twitter_image': page_obj.twitter_image,
        'canonical_url': page_obj.canonical_url,
        'robots_index': page_obj.robots_index,
        'robots_follow': page_obj.robots_follow,
    }
    return seo_data

def index(request):
    home_page = HomePage.objects.first()
    home_sliders = HomeSlider.objects.all().order_by('order')
    # Get latest 3 active tours and daytrips
    popular_tours = Tour.objects.filter(is_active=True)[:3]
    popular_daytrips = DayTrip.objects.filter(is_active=True)[:3]
    cities = City.objects.filter(is_active=True).order_by('order')[:4]
    packages = Package.objects.all().order_by('order')[:4]
    
    # Get section items
    things_to_do = ThingsToDoSection.objects.filter(is_active=True).order_by('order')
    museums = MuseumSection.objects.filter(is_active=True).order_by('order')
    foods = FoodSection.objects.filter(is_active=True).order_by('order')
    
    context = {
        'home_page': home_page,
        'home_sliders': home_sliders,
        'popular_tours': popular_tours,
        'popular_daytrips': popular_daytrips,
        'cities': cities,
        'packages': packages,
        'things_to_do': things_to_do,
        'museums': museums,
        'foods': foods,
        'seo': get_seo_context(home_page)  # Add SEO data to context
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def activities(request):
    return render(request, 'activities.html')

def book_now(request):
    # Static SEO content for book-now page
    seo = {
        'meta_title': 'Book Your Moroccan Desert Tour | Inmerzouga',
        'meta_description': 'Book your unforgettable Moroccan desert experience with Inmerzouga. Luxury camps, desert tours, and customized adventures in Merzouga.',
        'meta_keywords': 'book desert tour, morocco booking, merzouga reservation, desert camp booking, morocco travel reservation',
        'og_title': 'Book Your Moroccan Desert Adventure | Inmerzouga',
        'og_description': 'Reserve your spot for an authentic Moroccan desert experience. Luxury camps, guided tours, and memorable adventures in Merzouga.',
        'og_type': 'website',
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Book Your Desert Tour | Inmerzouga',
        'twitter_description': 'Plan your Moroccan desert adventure. Book luxury camps, guided tours, and authentic experiences in Merzouga.',
        'robots_index': True,
        'robots_follow': True
    }
    
    context = {
        'hide_contact_section': True,
        'seo': seo
    }
    return render(request, 'book-now.html', context)

def contact(request):
    # Static SEO content for contact page
    seo = {
        'meta_title': 'Contact Inmerzouga | Morocco Desert Tours & Experiences',
        'meta_description': 'Get in touch with Inmerzouga for desert tours, luxury camps, and authentic Moroccan experiences. We\'re here to help plan your perfect desert adventure.',
        'meta_keywords': 'contact inmerzouga, morocco desert contact, merzouga tours contact, desert camp inquiry',
        'og_title': 'Contact Us | Inmerzouga Desert Tours',
        'og_description': 'Contact Inmerzouga for personalized desert experiences, tour information, and booking assistance. Let us help plan your Moroccan adventure.',
        'og_type': 'website',
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Contact Inmerzouga Desert Tours',
        'twitter_description': 'Reach out to plan your desert adventure. Expert guidance for tours, camps, and authentic Moroccan experiences.',
        'robots_index': True,
        'robots_follow': True
    }
    
    context = {
        'hide_contact_section': True,
        'seo': seo
    }
    return render(request, 'contact.html', context)

def luxury_camp(request, slug=None):
    if slug:
        # Get specific luxury camp by slug
        camp = get_object_or_404(LuxuryCamp.objects.prefetch_related(
            'experiences',
            'inclusions',
            'exclusions',
            'extra_activities',
            'prices',
            'faqs',
            'photos'
        ), slug=slug)
    else:
        # Get the first luxury camp instance if no slug provided
        camp = get_object_or_404(LuxuryCamp.objects.prefetch_related(
            'experiences',
            'inclusions',
            'exclusions',
            'extra_activities',
            'prices',
            'faqs',
            'photos'
        ).first())
    
    context = {
        'camp': camp,
        'experiences': camp.experiences.all(),
        'inclusions': camp.inclusions.all(),
        'exclusions': camp.exclusions.all(),
        'activities': camp.extra_activities.all(),
        'prices': camp.prices.all(),
        'faqs': camp.faqs.all(),
        'photos': camp.photos.all(),
        'seo': get_seo_context(camp),
    }
    
    return render(request, 'luxury-camp.html', context)

def tour(request):
    return render(request, 'tour.html')

def events(request):
    page = get_object_or_404(EventsPage, is_active=True)
    events = Event.objects.filter(is_active=True).order_by('type', 'order')
    context = {
        'page': page,
        'events': events,
        'seo': get_seo_context(page),  # SEO context is already here
    }
    return render(request, 'events.html', context)

def tour_detail(request, slug):
    tour = get_object_or_404(Tour, slug=slug)    
    context = {
        'tour': tour,
        'day_overviews': tour.day_overviews.all().order_by('order', 'day_number'),
        'days': tour.days.all().order_by('day_number'),
        'highlights': tour.highlights.all().order_by('order'),
        'inclusions': tour.inclusions.all().order_by('inclusion_type', 'order'),
        'exclusions': tour.exclusions.all().order_by('order'),
        'faqs': tour.faqs.all().order_by('order'),
        'customer_photos': tour.customer_photos.all().order_by('order'),
        'extra_activities': tour.extra_activities.all().order_by('order'),
        'seo': get_seo_context(tour),
    }    
    return render(request, 'tour-detail.html', context)

def activities_view(request):
    page = get_object_or_404(ActivitiesPage)  # Just get the first page since it's a singleton
    activities = Activity.objects.filter(is_active=True).order_by('order')
    
    context = {
        'page': page,
        'activities': activities,
        'seo': get_seo_context(page)  # Add SEO data to context
    }
    
    return render(request, 'activities.html', context)


def daytrip_detail(request, slug):
    daytrip = get_object_or_404(DayTrip.objects.prefetch_related(
        'highlights',
        'activities',
        'inclusions',
        'exclusions',
        'faqs',
        'customer_photos',
        'prices'
    ), slug=slug)

    context = {
        'daytrip': daytrip,
        'seo': get_seo_context(daytrip),
    }
    return render(request, 'daytrip-detail.html', context)

def city_list(request):
    cities = City.objects.filter(is_active=True).order_by('order')
    return render(request, 'city-list.html', {'cities': cities})

def city_detail(request, slug):
    city = get_object_or_404(City.objects.prefetch_related(
        'gallery_images',
        'sections'
    ), slug=slug)
    
    # Get some featured/popular tours instead of city-specific tours
    related_tours = Tour.objects.filter(
        is_active=True
    ).order_by('-id')[:3]  # Get latest 3 tours
    
    context = {
        'city': city,
        'gallery_images': city.gallery_images.all(),
        'sections': city.sections.all(),
        'related_tours': related_tours,
        'seo': get_seo_context(city),
    }
    return render(request, 'city-detail.html', context)

def photography(request):
    page = get_object_or_404(PhotographyPage, is_active=True)
    
    # Create a list of hero grid images
    hero_grid_images = []
    for i in range(1, 9):
        image = getattr(page, f'hero_image_{i}')
        if image:
            hero_grid_images.append({
                'image': image,
                'alt_text': f'Hero grid image {i}'
            })
    
    # Get gallery images
    gallery_images = page.gallery_images.filter(is_active=True, is_hero=False)
    
    # Get unique categories from gallery images and remove None/empty values
    categories = set(gallery_images.exclude(
        category__isnull=True
    ).exclude(
        category=''
    ).values_list('category', flat=True))
    
    # Format categories for template
    formatted_categories = [
        {'name': dict(PhotographyPage.GALLERY_CATEGORIES)[cat], 'slug': cat}
        for cat in sorted(categories)
    ]
    
    # Get packages in specific order
    packages = Package.objects.all().order_by('package_type', 'order')
    
    # Order packages manually based on PACKAGE_TYPES order
    ordered_packages = sorted(
        packages,
        key=lambda x: x.package_order
    )
    
    context = {
        'page': page,
        'hero': {
            'title': page.hero_title,
            'subtitle': page.hero_subtitle,
        },
        'hero_images': hero_grid_images,
        'gallery_images': gallery_images,
        'packages': ordered_packages,
        'categories': formatted_categories,
        'seo': get_seo_context(page),
    }
    return render(request, 'photography.html', context)


def about_view(request):
    # Get the about page instance (assuming there's only one)
    about_page = AboutPage.objects.first()
    
    if not about_page:
        # Handle case where no about page content exists
        return HttpResponse("About page content not found", status=404)
    
    context = {
        'about': about_page,
        'testimonials': about_page.testimonials.all(),
        'gallery_images': about_page.gallery_images.all(),
        'seo': get_seo_context(about_page),
    }
    return render(request, 'about.html', context)

def get_active_promo():
    now = timezone.now()
    try:
        return Promo.objects.get(
            is_active=True,
            start_date__lte=now,
            end_date__gte=now
        )
    except Promo.DoesNotExist:
        return None

# Add to your context processor or update your views
def base_context(request):
    context = {
        'tours': Tour.objects.filter(is_active=True).order_by('order'),
        'day_trips': DayTrip.objects.filter(is_active=True).order_by('order'),
        'cities': City.objects.filter(is_active=True).order_by('order'),
        'luxury_camps': LuxuryCamp.objects.filter(is_active=True),
        'activities': Activity.objects.filter(is_active=True),
        'active_promo': get_active_promo(),
    }
    return context

def custom_404(request, exception):
    return render(request, '404.html', {'hide_contact_section': True}, status=404)

def contact_email(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        hear = request.POST.get('hear')
        message = request.POST.get('message')

        # Create email subject
        subject = f"New Contact Form Submission from {name}"

        # Create plain text message
        plain_message = (
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Phone: {phone}\n"
            f"How they heard about us: {hear}\n"
            f"Message:\n{message}"
        )

        # Create HTML message
        html_message = render_to_string('email_template_contact.html', {
            'name': name,
            'email': email,
            'phone': phone,
            'hear': hear,
            'message': message
        })

        # Email settings
        from_email = 'noreplay.mtph@gmail.com'
        to_email = ['inmerzouga@gmail.com']

        try:
            # Send email
            send_mail(
                subject,
                plain_message,
                from_email,
                to_email,
                html_message=html_message
            )
            messages.success(request, "Thank you for your message! We'll get back to you soon.")
        except Exception as e:
            messages.error(request, "Sorry, there was an error sending your message. Please try again later.")
            print(f"Email error: {str(e)}")  # For debugging

        # Redirect back to the same page
        return redirect(request.META.get('HTTP_REFERER', 'index'))
    
    # If not POST, redirect to home
    return redirect('index')

def contact_email2(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject_type = request.POST.get('subject')
        message = request.POST.get('message')

        # Validate required fields
        required_fields = {
            'name': name,
            'email': email,
            'subject': subject_type,
            'message': message
        }

        # Check for missing required fields
        missing_fields = [field for field, value in required_fields.items() if not value]
        
        if missing_fields:
            messages.error(request, f"Please fill in the following required fields: {', '.join(missing_fields)}")
            return redirect('contact')

        # Create email subject based on the subject type
        subject_mapping = {
            'booking': 'Tour Booking Inquiry',
            'inquiry': 'General Inquiry',
            'support': 'Customer Support Request',
            'feedback': 'Customer Feedback'
        }
        email_subject = f"{subject_mapping.get(subject_type, 'Contact Form')} from {name}"

        # Create plain text message
        plain_message = (
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Phone: {phone}\n"
            f"Subject: {subject_type}\n"
            f"Message:\n{message}"
        )

        # Create HTML message
        html_message = render_to_string('email_template_contact2.html', {
            'name': name,
            'email': email,
            'phone': phone,
            'subject': subject_type,
            'message': message
        })

        # Email settings
        from_email = 'noreplay.mtph@gmail.com'
        to_email = ['inmerzouga@gmail.com']

        try:
            # Send email
            send_mail(
                email_subject,
                plain_message,
                from_email,
                to_email,
                html_message=html_message
            )
            messages.success(request, "Thank you for contacting us! We'll get back to you shortly.")
        except Exception as e:
            messages.error(request, "Sorry, there was an error sending your message. Please try again later.")
            print(f"Email error: {str(e)}")  # For debugging

        return redirect('contact')
    
    return redirect('contact')

def booking_email(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        tour_type = request.POST.get('tourType')
        group_size = request.POST.get('groupSize')
        start_date = request.POST.get('startDate')
        duration = request.POST.get('duration')
        requirements = request.POST.get('requirements')

        # Validate required fields
        required_fields = {
            'First Name': first_name,
            'Last Name': last_name,
            'Email': email,
            'Phone': phone,
            'Tour Type': tour_type,
            'Group Size': group_size,
            'Start Date': start_date,
            'Duration': duration
        }

        # Check for missing required fields
        missing_fields = [field for field, value in required_fields.items() if not value]
        
        if missing_fields:
            messages.error(request, f"Please fill in the following required fields: {', '.join(missing_fields)}")
            return redirect('book_now')

        # Create email subject
        subject = f"New Booking Request from {first_name} {last_name}"

        # Create plain text message
        plain_message = (
            f"Personal Information:\n"
            f"Name: {first_name} {last_name}\n"
            f"Email: {email}\n"
            f"Phone: {phone}\n\n"
            f"Trip Details:\n"
            f"Tour Type: {tour_type}\n"
            f"Group Size: {group_size}\n"
            f"Start Date: {start_date}\n"
            f"Duration: {duration} Days\n"
            f"Special Requirements:\n{requirements if requirements else 'None'}"
        )

        # Create HTML message
        html_message = render_to_string('email_template_booking.html', {
            'firstName': first_name,
            'lastName': last_name,
            'email': email,
            'phone': phone,
            'tourType': tour_type,
            'groupSize': group_size,
            'startDate': start_date,
            'duration': duration,
            'requirements': requirements
        })

        # Email settings
        from_email = 'noreplay.mtph@gmail.com'
        to_email = ['inmerzouga@gmail.com']

        try:
            # Send email
            send_mail(
                subject,
                plain_message,
                from_email,
                to_email,
                html_message=html_message
            )
            messages.success(request, "Thank you for your booking request! We'll contact you shortly to confirm your tour details.")
        except Exception as e:
            messages.error(request, "Sorry, there was an error sending your booking request. Please try again later.")
            print(f"Email error: {str(e)}")  # For debugging

        return redirect('book_now')
    
    return redirect('book_now')





