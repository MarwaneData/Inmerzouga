from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.conf import settings
import os

class SEOModel(models.Model):
    """
    Abstract base model for comprehensive SEO functionality.
    All fields are optional to give users full control.
    """
    # Basic SEO
    meta_title = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text="Meta title (50-60 characters recommended)"
    )
    meta_description = models.CharField(
        max_length=160,
        blank=True,
        null=True,
        help_text="Meta description (150-160 characters recommended)"
    )
    meta_keywords = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Comma-separated keywords"
    )
    
    # Open Graph (Facebook, LinkedIn)
    og_title = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text="Open Graph title for social media"
    )
    og_description = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Open Graph description for social media"
    )
    og_image = models.ImageField(
        upload_to='seo/og/',
        blank=True,
        null=True,
        help_text="Open Graph image (1200x630px recommended)"
    )
    og_type = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        default='website',
        help_text="Open Graph type (e.g., website, article)"
    )
    
    # Twitter Cards
    twitter_card = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        default='summary_large_image',
        help_text="Twitter card type (summary, summary_large_image)"
    )
    twitter_title = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text="Twitter card title (falls back to OG title)"
    )
    twitter_description = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Twitter card description (falls back to OG description)"
    )
    twitter_image = models.ImageField(
        upload_to='seo/twitter/',
        blank=True,
        null=True,
        help_text="Twitter card image (falls back to OG image)"
    )
    
    # Additional SEO
    canonical_url = models.URLField(
        blank=True,
        null=True,
        help_text="Canonical URL (if different from current URL)"
    )
    robots_index = models.BooleanField(
        default=True,
        null=True,
        help_text="Allow search engines to index this page"
    )
    robots_follow = models.BooleanField(
        default=True,
        null=True,
        help_text="Allow search engines to follow links on this page"
    )
    
  

    class Meta:
        abstract = True

class Tour(SEOModel):
    # Basic Tour Info
    title = models.CharField(max_length=200, help_text="Tour title (e.g. 4 Days Marrakech to Merzouga Desert Tour)")
    short_title = models.CharField(max_length=100, blank=True, null=True, help_text="Shorter version of the title for menus and cards")
    slug = models.SlugField(max_length=255, unique=True, blank=True, help_text="URL-friendly version of the title")
    description = models.TextField(help_text="Main tour description")
    main_image = models.ImageField(upload_to='tours/', help_text="Main header image")
    small_image = models.ImageField(upload_to='tours/thumbnails/', help_text="Small thumbnail image")
    
    # Quick Facts
    duration = models.CharField(max_length=50, help_text="Number of days")
    countries = models.IntegerField(default=1, help_text="Number of countries visited")
    cities = models.IntegerField(help_text="Number of cities visited")
    nights = models.IntegerField(help_text="Number of nights accommodation")
    
    # Meals Count
    breakfast_count = models.IntegerField(default=0, help_text="Total number of breakfasts")
    lunch_count = models.IntegerField(default=0, help_text="Total number of lunches")
    dinner_count = models.IntegerField(default=0, help_text="Total number of dinners")
    
    # Activity Level
    ACTIVITY_CHOICES = [
        ('cultural', 'Cultural & Historical'),
        ('adventure', 'Adventure & Exploration'),
        ('relaxation', 'Relaxation & Wellness'),
        ('photography', 'Photography & Sightseeing'),
        ('mixed', 'Mixed Activities')
    ]
    activity_level = models.CharField(max_length=20, choices=ACTIVITY_CHOICES, help_text="Type of activities included")
    activity_description = models.TextField(help_text="Describe what activities are included")
    
    # Booking Details
    low_deposit = models.DecimalField(max_digits=10, decimal_places=2, help_text="Low deposit amount to secure booking")
    child_discount = models.IntegerField(default=25, help_text="Discount percentage for children")
    
    # Map
    map_image = models.ImageField(upload_to='tours/maps/', help_text="Tour route map")
    
    # Status
    is_active = models.BooleanField(default=True)
    
    # Add the new is_group field
    is_group = models.BooleanField(default=False, help_text="Check if this is a group tour")

    # Add these new fields
    is_day_trip = models.BooleanField(default=False, help_text="Check if this is a day trip")
    day_trip_time = models.CharField(max_length=50, blank=True, null=True, help_text="Time for day trip (e.g. '9:00 AM')")
    day_trip_location = models.CharField(max_length=200, blank=True, null=True, help_text="Location for day trip (e.g. 'Atlas Mountains')")
    max_persons = models.IntegerField(blank=True, null=True, help_text="Maximum number of persons for day trip")
    
    # Add this field
    order = models.IntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def price_from(self):
        """Get the lowest price from all tour prices"""
        lowest_price = self.prices.all().order_by('price').first()
        if lowest_price:
            return lowest_price.price
        return 0  # Or any default value you prefer

    @property
    def is_multi_day(self):
        """Return True if this is a multi-day tour"""
        return not self.is_day_trip

    class Meta:
        verbose_name = "B - Tour"
        verbose_name_plural = "B - Tours"

class TourCustomerPhoto(models.Model):
    tour = models.ForeignKey(Tour, related_name='customer_photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tours/customer_photos/', help_text="Customer photo")
    caption = models.CharField(max_length=200, blank=True, help_text="Optional caption")
    location = models.CharField(max_length=100, blank=True, help_text="Photo location")
    date_taken = models.DateField(blank=True, null=True, help_text="When the photo was taken")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Photo for {self.tour.title} - {self.caption}"

class ExtraActivity(models.Model):
    tour = models.ForeignKey(Tour, related_name='extra_activities', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=50, help_text="e.g. '2 hours', 'Half day'")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='tours/activities/', blank=True)
    is_recommended = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Extra activities"

    def __str__(self):
        return f"{self.title} - ${self.price}"

class TourInclusion(models.Model):
    INCLUSION_TYPES = [
        ('accommodation', 'Accommodation'),
        ('guide', 'Guide'),
        ('meals', 'Meals'),
        ('transport', 'Transport'),
        ('additional', 'Additional Services'),
    ]
    
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='inclusions')
    inclusion_type = models.CharField(max_length=50, choices=INCLUSION_TYPES)
    title = models.CharField(max_length=200)
    description = models.TextField(help_text="Enter each item on a new line")
    icon = models.CharField(max_length=50, default='fas fa-check')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['inclusion_type', 'order']
        verbose_name = "Tour Inclusion"
        verbose_name_plural = "Tour Inclusions"

    def __str__(self):
        return f"{self.get_inclusion_type_display()}: {self.title}"

    @property
    def description_list(self):
        """Returns the description as a list, split by newlines"""
        return [item.strip() for item in self.description.split('\n') if item.strip()]

class TourDay(models.Model):
    tour = models.ForeignKey(Tour, related_name='days', on_delete=models.CASCADE)
    day_number = models.IntegerField(help_text="Day number (1, 2, 3, etc.)")
    title = models.CharField(max_length=200, help_text="Title for this day")
    subtitle = models.CharField(max_length=200, help_text="Optional subtitle", blank=True)
    location = models.CharField(max_length=200, help_text="Location(s) for this day (e.g. Marrakech → Atlas Mountains)")
    description = models.TextField(help_text="Detailed description of the day's activities")
    image = models.ImageField(upload_to='tours/days/', help_text="Main image for this day")
    
    # Accommodation
    hotel_name = models.CharField(max_length=200, help_text="Hotel or accommodation name")
    hotel_link = models.URLField(blank=True, help_text="Link to hotel website (optional)")
    
    # Meals for this day
    breakfast = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)
    
    # Welcome Day
    is_welcome_day = models.BooleanField(default=False, help_text="Is this a welcome day?")

    def __str__(self):
        return f"Day {self.day_number} - {self.title}"

    class Meta:
        ordering = ['day_number']

class TourHighlight(models.Model):
    tour = models.ForeignKey(Tour, related_name='highlights', on_delete=models.CASCADE)
    HIGHLIGHT_TYPES = [
        ('visit', 'Visit'),
        ('discover', 'Discover'),
        ('see', 'See'),
        ('scenic_drive', 'Scenic Drive'),
        ('view', 'View')
    ]
    highlight_type = models.CharField(max_length=20, choices=HIGHLIGHT_TYPES, help_text="Type of highlight")
    description = models.TextField(help_text="What will travelers see/do?")
    icon = models.CharField(max_length=50, default='fas fa-map-marker-alt', help_text="FontAwesome icon class")
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.get_highlight_type_display()}: {self.description[:50]}"

    class Meta:
        ordering = ['order']

class TourExclusion(models.Model):
    tour = models.ForeignKey(Tour, related_name='exclusions', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text="What's not included")
    description = models.TextField(help_text="Details about why it's not included and any recommendations")
    icon = models.CharField(max_length=50, default='fas fa-times', help_text="FontAwesome icon class")
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

class FAQ(models.Model):
    tour = models.ForeignKey(Tour, related_name='faqs', on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['order']

class TourPrice(models.Model):
    tour = models.ForeignKey(Tour, related_name='prices', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, help_text='e.g., "Solo Traveler", "2 Persons", etc.')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    per_person = models.BooleanField(default=False, help_text='Check if price is per person')
    icon_class = models.CharField(max_length=50, help_text='FontAwesome icon class, e.g., "fas fa-user"')
    benefits = models.TextField(help_text='Enter each benefit on a new line')
    order = models.PositiveIntegerField(default=0, help_text='Order in which this price appears')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} - {self.price}€"

class LuxuryCamp(SEOModel):
    # Basic Info
    title = models.CharField(max_length=200, help_text="Main title for the luxury camp")
    slug = models.SlugField(max_length=255, unique=True, blank=True, help_text="URL-friendly version of the title")
    subtitle = models.CharField(max_length=200, help_text="Subtitle describing the experience")
    description = models.TextField(help_text="Main description of the luxury camp experience")
    hero_image = models.ImageField(upload_to='luxury_camp/', help_text="Hero background image")
    
    # Add is_active field
    is_active = models.BooleanField(default=True, help_text="Check to show this camp in navigation")
    
    # Section Images
    main_section_image = models.ImageField(upload_to='luxury_camp/sections/', help_text="Main large image for the section", blank=True, null=True)
    main_section_image_caption = models.CharField(max_length=200, blank=True, help_text="Caption for the main section image")
    section_image_1 = models.ImageField(upload_to='luxury_camp/sections/', help_text="First small image", blank=True, null=True)
    section_image_1_caption = models.CharField(max_length=200, blank=True, help_text="Caption for the first small image")
    section_image_2 = models.ImageField(upload_to='luxury_camp/sections/', help_text="Second small image", blank=True, null=True)
    section_image_2_caption = models.CharField(max_length=200, blank=True, help_text="Caption for the second small image")
    section_image_3 = models.ImageField(upload_to='luxury_camp/sections/', help_text="Third small image", blank=True, null=True)
    section_image_3_caption = models.CharField(max_length=200, blank=True, help_text="Caption for the third small image")
    
    # Hero Features
    hero_feature_1_icon = models.CharField(max_length=50, default='fas fa-moon', help_text="FontAwesome icon class")
    hero_feature_1_text = models.CharField(max_length=100, default='Luxury Comfort')
    hero_feature_2_icon = models.CharField(max_length=50, default='fas fa-star', help_text="FontAwesome icon class")
    hero_feature_2_text = models.CharField(max_length=100, default='Desert Magic')
    hero_feature_3_icon = models.CharField(max_length=50, default='fas fa-compass', help_text="FontAwesome icon class")
    hero_feature_3_text = models.CharField(max_length=100, default='Unique Experience')

    # Quick Facts
    duration = models.CharField(max_length=50, default='24 hours', help_text="Duration of the experience")
    group_size = models.CharField(max_length=50, default='2-4 persons per tent', help_text="Typical group size")
    meals_included = models.CharField(max_length=100, default='Dinner and breakfast included', help_text="Included meals")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "D - Luxury Camp"
        verbose_name_plural = "D - Luxury Camps"

class LuxuryCampInclusion(models.Model):
    camp = models.ForeignKey(LuxuryCamp, related_name='inclusions', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(help_text="Enter each item on a new line")
    icon = models.CharField(max_length=50, default='fas fa-check')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    @property
    def description_list(self):
        return [item.strip() for item in self.description.split('\n') if item.strip()]

class LuxuryCampExclusion(models.Model):
    camp = models.ForeignKey(LuxuryCamp, related_name='exclusions', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(help_text="Enter each item on a new line")
    icon = models.CharField(max_length=50, default='fas fa-times')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    @property
    def description_list(self):
        return [item.strip() for item in self.description.split('\n') if item.strip()]

class LuxuryCampActivity(models.Model):
    camp = models.ForeignKey(LuxuryCamp, related_name='extra_activities', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(help_text="Enter each item on a new line")
    icon = models.CharField(max_length=50, default='fas fa-plus-circle')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Luxury camp activities"

    def __str__(self):
        return self.title

    @property
    def description_list(self):
        return [item.strip() for item in self.description.split('\n') if item.strip()]

class LuxuryCampPrice(models.Model):
    camp = models.ForeignKey(LuxuryCamp, related_name='prices', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, help_text='e.g., "Private Tent", "Double Tent", etc.')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    per_night = models.BooleanField(default=True)
    icon = models.CharField(max_length=50, help_text='FontAwesome icon class, e.g., "fas fa-user"')
    benefits = models.TextField(help_text='Enter each benefit on a new line')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} - {self.price}€"

    @property
    def benefits_list(self):
        return [item.strip() for item in self.benefits.split('\n') if item.strip()]

class LuxuryCampFAQ(models.Model):
    camp = models.ForeignKey(LuxuryCamp, related_name='faqs', on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question

class LuxuryCampPhoto(models.Model):
    camp = models.ForeignKey(LuxuryCamp, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='luxury_camp/photos/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Photo {self.order + 1} for {self.camp.title}"

class LuxuryCampExperience(models.Model):
    camp = models.ForeignKey(LuxuryCamp, related_name='experiences', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=50, default='fas fa-check', help_text="FontAwesome icon class")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Camp Experience"
        verbose_name_plural = "Camp Experiences"

    def __str__(self):
        return self.title

class TourDayOverview(models.Model):
    tour = models.ForeignKey(Tour, related_name='day_overviews', on_delete=models.CASCADE)
    day_number = models.IntegerField(help_text="Day number in the tour")
    title = models.CharField(max_length=100, help_text="Short title for this day")
    description = models.TextField(help_text="Brief description of this day's activities")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'day_number']
        verbose_name = "Tour Day Overview"
        verbose_name_plural = "Tour Day Overviews"

    def __str__(self):
        return f"Day {self.day_number}: {self.title}"

class ActivitiesPage(SEOModel):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=500)
    hero_image = models.ImageField(upload_to='activities/', help_text="Hero background image")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "A - Activities Page"
        verbose_name_plural = "A - Activities Page"

    def __str__(self):
        return self.title

class Activity(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('moderate', 'Moderate'),
        ('challenging', 'Challenging'),
        ('all_levels', 'All Levels'),
    ]

    # Card Information
    title = models.CharField(max_length=200, help_text="Activity title (e.g. Sunset Camel Trek)")
    description = models.TextField(help_text="Short description for the activity card")
    image = models.ImageField(upload_to='activities/', help_text="Activity main image")
    duration = models.CharField(max_length=50, help_text="Duration (e.g. '2 hours')")
    min_group_size = models.IntegerField(help_text="Minimum participants")
    max_group_size = models.IntegerField(help_text="Maximum participants")
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_suffix = models.CharField(max_length=50, default='per person')

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = "C - Activity"
        verbose_name_plural = "C - Activities"

    def __str__(self):
        return self.title

class DayTrip(SEOModel):
    # Basic Info
    title = models.CharField(max_length=200, help_text="Day Trip title")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(help_text="Main description")
    main_image = models.ImageField(upload_to='daytrips/', help_text="Main header image")
    small_image = models.ImageField(upload_to='daytrips/thumbnails/', help_text="Small thumbnail image")
    
    # Day Trip Specific Fields
    duration_hours = models.IntegerField(help_text="Duration in hours")
    city = models.CharField(max_length=100, help_text="City where the day trip takes place")
    is_group = models.BooleanField(default=False, help_text="Is this a group day trip?")
    max_persons = models.IntegerField(help_text="Maximum number of persons")
    start_time = models.CharField(max_length=50, help_text="Start time (e.g. '9:00 AM')")
    
    # Status
    is_active = models.BooleanField(default=True)

    # Add order field
    order = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def price_from(self):
        lowest_price = self.prices.all().order_by('price').first()
        if lowest_price:
            return lowest_price.price
        return 0

    class Meta:
        ordering = ['order']
        verbose_name = "B - Day Trip"
        verbose_name_plural = "B - Day Trips"

class DayTripCustomerPhoto(models.Model):
    daytrip = models.ForeignKey(DayTrip, related_name='customer_photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='daytrips/customer_photos/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

class DayTripActivity(models.Model):
    daytrip = models.ForeignKey(DayTrip, related_name='activities', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

class DayTripInclusion(models.Model):
    daytrip = models.ForeignKey(DayTrip, related_name='inclusions', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='fas fa-check')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

class DayTripExclusion(models.Model):
    daytrip = models.ForeignKey(DayTrip, related_name='exclusions', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='fas fa-times')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

class DayTripHighlight(models.Model):
    daytrip = models.ForeignKey(DayTrip, related_name='highlights', on_delete=models.CASCADE)
    
    HIGHLIGHT_TYPES = [
        ('visit', 'Visit'),
        ('discover', 'Discover'),
        ('see', 'See'),
        ('scenic_drive', 'Scenic Drive'),
        ('view', 'View')
    ]
    
    highlight_type = models.CharField(
        max_length=20, 
        choices=HIGHLIGHT_TYPES, 
        default='visit',
        help_text="Type of highlight"
    )
    description = models.TextField(help_text="What will travelers see/do?")
    icon = models.CharField(max_length=50, default='fas fa-map-marker-alt', help_text="FontAwesome icon class")
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.get_highlight_type_display()}: {self.description[:50]}"

    class Meta:
        ordering = ['order']

class DayTripFAQ(models.Model):
    daytrip = models.ForeignKey(DayTrip, related_name='faqs', on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

class DayTripPrice(models.Model):
    daytrip = models.ForeignKey(DayTrip, related_name='prices', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, help_text='e.g., "Per Person", "Group of 4"')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

class City(SEOModel):
    # Basic Info
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    hero_image = models.ImageField(upload_to='cities/hero/', help_text="Hero header image")
    description = models.TextField(help_text="Main city description")
    
    # Status
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "C - City"
        verbose_name_plural = "C - Cities"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class CitySection(models.Model):
    city = models.ForeignKey(City, related_name='sections', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(help_text="Section content with line breaks")
    image = models.ImageField(upload_to='cities/sections/', blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} - {self.city.title}"

class CityGalleryImage(models.Model):
    city = models.ForeignKey(City, related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cities/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Gallery image for {self.city.title}"

class CityHighlight(models.Model):
    city = models.ForeignKey(City, related_name='highlights', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='fas fa-landmark')
    image = models.ImageField(upload_to='cities/highlights/', blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} - {self.city.title}"

class CityAttraction(models.Model):
    city = models.ForeignKey(City, related_name='attractions', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='cities/attractions/')
    location = models.CharField(max_length=200, blank=True)
    visit_duration = models.CharField(max_length=100, blank=True)
    best_time = models.CharField(max_length=200, blank=True)
    tips = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

class CityNeighborhood(models.Model):
    city = models.ForeignKey(City, related_name='neighborhoods', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='cities/neighborhoods/')
    highlights = models.TextField(help_text="Key points about this neighborhood")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

class LocalExperience(models.Model):
    city = models.ForeignKey(City, related_name='local_experiences', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='cities/experiences/')
    duration = models.CharField(max_length=100)
    price_range = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

class HomePage(SEOModel):
    """Model for the Home/Index page"""
    # Hero Section
    hero_title = models.CharField(
        max_length=200,
        help_text="Main hero title"
    )
    hero_subtitle = models.TextField(
        help_text="Hero subtitle text"
    )
    hero_image = models.ImageField(
        upload_to='home/hero/',
        help_text="Hero background image (1920x1080 recommended)"
    )
    hero_rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=4.8,
        help_text="Rating display in hero (e.g., 4.8)"
    )
    hero_button_text = models.CharField(
        max_length=50,
        default="See all Morocco Tours",
        help_text="Call to action button text"
    )

    class Meta:
        verbose_name = "A - Home Page"
        verbose_name_plural = "A - Home Page"

    def __str__(self):
        return "Home Page Content"

class HomeSlider(models.Model):
    """Model for all home page sliders"""
    SLIDER_TYPES = [
        ('things', 'Things to Do'),
        ('museums', 'Museums'),
        ('food', 'Food'),
    ]

    type = models.CharField(
        max_length=20,
        choices=SLIDER_TYPES,
        help_text="Select which slider this content belongs to"
    )
    title = models.CharField(
        max_length=200,
        help_text="Section title (e.g., 'Best museums in Morocco')"
    )
    subtitle = models.TextField(
        help_text="Section subtitle/description"
    )
    slides = models.JSONField(
        default=list,
        help_text="List of slides. Each slide should have 'title' and 'description'"
    )
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Home Page Slider"
        verbose_name_plural = "Home Page Sliders"

    def __str__(self):
        return f"{self.get_type_display()} Slider"

class ThingsToDoSection(models.Model):
    """Model for Things to Do section items"""
    home_page = models.ForeignKey(
        HomePage,
        related_name='things_to_do',
        on_delete=models.CASCADE,
        null=True,  # Allow null temporarily
        blank=True
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Things to Do Item"
        verbose_name_plural = "Things to Do Items"

    def __str__(self):
        return self.title

class MuseumSection(models.Model):
    """Model for Museum section items"""
    home_page = models.ForeignKey(
        HomePage,
        related_name='museums',
        on_delete=models.CASCADE,
        null=True,  # Allow null temporarily
        blank=True
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Museum Item"
        verbose_name_plural = "Museum Items"

    def __str__(self):
        return self.title

class FoodSection(models.Model):
    """Model for Food section items"""
    home_page = models.ForeignKey(
        HomePage,
        related_name='foods',
        on_delete=models.CASCADE,
        null=True,  # Allow null temporarily
        blank=True
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Food Item"
        verbose_name_plural = "Food Items"

    def __str__(self):
        return self.title

class Contact(SEOModel):
    """Model for essential contact information and social media links"""
    # Contact Information
    phone = models.CharField(max_length=20, null=True, blank=True, help_text="Main contact number")
    whatsapp = models.CharField(max_length=20, null=True, blank=True, help_text="WhatsApp number (include country code)")
    email = models.EmailField(null=True, blank=True, help_text="Contact email address")
    
    # Social Media Links
    instagram = models.URLField(null=True, blank=True, help_text="Instagram profile URL")
    youtube = models.URLField(null=True, blank=True,    help_text="YouTube channel URL")
    
    # Status
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "F - Contact Information"
        verbose_name_plural = "F - Contact Information"

    def __str__(self):
        return "Contact Information"

    def clean(self):
        # Ensure only one instance exists
        if not self.pk and Contact.objects.exists():
            raise ValidationError('Only one Contact instance can be created.')

class Promo(models.Model):
    """Model for promotional popups"""
    title = models.CharField(max_length=100, help_text="Promo title (e.g. 'Special Offer!')")
    discount = models.IntegerField(help_text="Discount percentage (e.g. 20 for 20% off)")
    image = models.ImageField(upload_to='promos/', help_text="Promotional image")
    link = models.URLField(help_text="Link to the tour or page being promoted")
    
    # Features (3 items)
    feature1_text = models.CharField(max_length=100)
    feature2_text = models.CharField(max_length=100)
    feature3_text = models.CharField(max_length=100)
    
    # Control fields
    is_active = models.BooleanField(default=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    class Meta:
        verbose_name = "F - Promotion"
        verbose_name_plural = "F - Promotions"

    def __str__(self):
        return f"{self.title} ({self.discount}% off)"

    def clean(self):
        # Ensure only one active promo at a time
        if self.is_active and Promo.objects.exclude(id=self.id).filter(is_active=True).exists():
            raise ValidationError('Only one promotion can be active at a time.')
        
        # Ensure end date is after start date
        if self.end_date <= self.start_date:
            raise ValidationError('End date must be after start date.')

class PhotographyPage(SEOModel):
    """Single model for the entire photography page"""
    # Page Information
    title = models.CharField(max_length=200, default="Photography Services")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    
    # Hero Section
    hero_title = models.CharField(max_length=200, blank=True)
    hero_subtitle = models.TextField(blank=True)
    
    # Hero Grid Images
    hero_image_1 = models.ImageField(upload_to='photography/hero/grid/', help_text="Hero grid image 1", blank=True)
    hero_image_2 = models.ImageField(upload_to='photography/hero/grid/', help_text="Hero grid image 2", blank=True)
    hero_image_3 = models.ImageField(upload_to='photography/hero/grid/', help_text="Hero grid image 3", blank=True)
    hero_image_4 = models.ImageField(upload_to='photography/hero/grid/', help_text="Hero grid image 4", blank=True)
    hero_image_5 = models.ImageField(upload_to='photography/hero/grid/', help_text="Hero grid image 5", blank=True)
    hero_image_6 = models.ImageField(upload_to='photography/hero/grid/', help_text="Hero grid image 6", blank=True)
    hero_image_7 = models.ImageField(upload_to='photography/hero/grid/', help_text="Hero grid image 7", blank=True)
    hero_image_8 = models.ImageField(upload_to='photography/hero/grid/', help_text="Hero grid image 8", blank=True)
    
    # Gallery Categories
    GALLERY_CATEGORIES = [
        ('landscape', 'Landscape'),
        ('portrait', 'Portrait'),
        ('culture', 'Culture'),
        ('events', 'Events'),
    ]
    
 
    # Timestamps
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = "A - Photography Page"
        verbose_name_plural = "A - Photography Page"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class PhotographyImage(models.Model):
    """Model for photography images"""
    page = models.ForeignKey(
        PhotographyPage, 
        on_delete=models.CASCADE, 
        related_name='gallery_images',
        null=True,
        blank=True
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photography/gallery/')
    category = models.CharField(
        max_length=50, 
        choices=PhotographyPage.GALLERY_CATEGORIES,
        null=True,
        blank=True
    )
    is_hero = models.BooleanField(default=False, help_text="Show in hero section")
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Package(models.Model):
    PACKAGE_TYPES = [
        ('basic', 'Basic Package'),
        ('standard', 'Standard Package'),
        ('popular', 'Most Popular'),
        ('premium', 'Premium Package'),
    ]
    
    title = models.CharField(max_length=200)  
    package_type = models.CharField(max_length=20, choices=PACKAGE_TYPES, default='basic')
    photo_count = models.IntegerField(help_text="Number of photos", default=20)
    editing_hours = models.IntegerField(help_text="Hours of editing", default=2)
    retouches = models.IntegerField(help_text="Number of retouches", default=5)
    digital_delivery = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    order = models.IntegerField(default=0)
    image = models.ImageField(
        upload_to='packages/', 
        help_text="Package display image",
        blank=True
    )
    
    class Meta:
        ordering = ['order']
        verbose_name = "E - Package"
        verbose_name_plural = "E - Packages"
    
    def __str__(self):
        return self.title

    @property
    def package_order(self):
        order_map = {
            'basic': 1,
            'standard': 2,
            'popular': 3,
            'premium': 4
        }
        return order_map.get(self.package_type, 99)

class AboutPage(SEOModel):
    # Hero Section
    hero_title = models.CharField(max_length=200, help_text="Main hero title (e.g. 'Discover the Magic of Merzouga')")
    hero_subtitle = models.TextField(help_text="Hero subtitle/description")
    hero_image = models.ImageField(upload_to='about/', help_text="Hero background image")
    
    # About Section
    about_title = models.CharField(max_length=200, help_text="About section title (e.g. 'About Inmerzouga')")
    about_description = models.TextField(help_text="Main about description")
    about_image = models.ImageField(upload_to='about/', help_text="About section image")
    
    # Statistics
    happy_travelers_count = models.IntegerField(help_text="Number of happy travelers (e.g. 15000)")
    social_followers_count = models.IntegerField(help_text="Number of social media followers")
    
    # Video Section
    video_section_title = models.CharField(max_length=200, help_text="Title for video section")
    video_section_description = models.TextField(help_text="Description for video section")
    video_thumbnail = models.ImageField(upload_to='about/video/', help_text="Video thumbnail image")
    video_url = models.URLField(help_text="YouTube or Vimeo video URL")
    video_type = models.CharField(max_length=20, choices=[
        ('youtube', 'YouTube'),
        ('vimeo', 'Vimeo')
    ], default='youtube', help_text="Type of video platform")

    def get_embed_url(self):
        """Convert video URL to embed URL"""
        if self.video_type == 'youtube':
            # Convert YouTube URL to embed format
            if 'youtube.com/watch?v=' in self.video_url:
                video_id = self.video_url.split('watch?v=')[1].split('&')[0]
                return f'https://www.youtube.com/embed/{video_id}'
            elif 'youtu.be/' in self.video_url:
                video_id = self.video_url.split('youtu.be/')[1]
                return f'https://www.youtube.com/embed/{video_id}'
        elif self.video_type == 'vimeo':
            # Convert Vimeo URL to embed format
            if 'vimeo.com/' in self.video_url:
                video_id = self.video_url.split('vimeo.com/')[1]
                return f'https://player.vimeo.com/video/{video_id}'
        return self.video_url

    class Meta:
        verbose_name = "A - About Page"
        verbose_name_plural = "A - About Page"

    def __str__(self):
        return "About Page Content"

class AboutTestimonial(models.Model):
    about_page = models.ForeignKey(AboutPage, related_name='testimonials', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='about/testimonials/', help_text="Client photo")
    name = models.CharField(max_length=100, help_text="Client name")
    country = models.CharField(max_length=100, help_text="Client's country")
    content = models.TextField(help_text="Testimonial content")
    rating = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating from 1-5 stars"
    )
    order = models.IntegerField(default=0, help_text="Order of appearance")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Testimonial by {self.name}"

class AboutGalleryImage(models.Model):
    about_page = models.ForeignKey(AboutPage, related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='about/gallery/', help_text="Gallery image")
    title = models.CharField(max_length=200, help_text="Image title/alt text")
    location = models.CharField(max_length=100, help_text="Location label (e.g. 'Merzouga Dunes')")
    order = models.IntegerField(default=0, help_text="Order of appearance")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class EventsPage(SEOModel):
    """Model for the Events landing page"""
    title = models.CharField(max_length=200, default="Desert Events")
    subtitle = models.TextField(default="From intimate photoshoots to grand celebrations...")
    is_active = models.BooleanField(default=True)
    
    # Hero Section Images
    hero_image_1 = models.ImageField(upload_to='events/hero/', help_text="First hero slide")
    hero_image_2 = models.ImageField(upload_to='events/hero/', help_text="Second hero slide")
    hero_image_3 = models.ImageField(upload_to='events/hero/', help_text="Third hero slide")
    
    class Meta:
        verbose_name = "A - Events Page"
        verbose_name_plural = "A - Events Page"

    def __str__(self):
        return self.title

class Event(models.Model):
    """Model for individual events"""
    page = models.ForeignKey(
        EventsPage, 
        on_delete=models.CASCADE, 
        related_name='events',
        null=True,
        blank=True
    )
    
    # Basic Information
    type = models.CharField(
        max_length=100,
        help_text="Enter event type (e.g., 'Desert Photography', 'Desert Wedding')",
        default="Desert Photography"
    )
    title = models.CharField(max_length=200)
    description = models.TextField(help_text="e.g., 'Capture the magic of the desert with our professional photography services.'")
    image = models.ImageField(upload_to='events/')
    
    # Event Meta Information
    duration = models.CharField(max_length=50, default="Full Day")
    group_size = models.CharField(max_length=50, default="Custom Size")
    price_info = models.CharField(max_length=50, default="Custom Quote")
    
    # Prices as text field
    prices = models.TextField(
        help_text="Enter each price on a new line (e.g., '1-2 persons: 340€')",
        default="1-2 persons: 340€\n3-4 persons: 440€\n5+ persons: Contact us"
    )
    
    # Included Items
    includes = models.ManyToManyField('EventInclusion', related_name='events')
    
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "E - Event"
        verbose_name_plural = "E - Events"

    def __str__(self):
        return f"{self.type} - {self.title}"
    
    def get_prices_list(self):
        """Convert prices text to list of dictionaries"""
        prices = []
        for line in self.prices.split('\n'):
            if ':' in line:
                people, price = line.split(':', 1)
                prices.append({
                    'people': people.strip(),
                    'price': price.strip()
                })
        return prices

class EventInclusion(models.Model):
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=50, default='fas fa-check')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class SiteMapEntry(models.Model):
    name = models.CharField(max_length=200, unique=True, default="my Site map")
    content = models.TextField(help_text="Put your site map here:")
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)        
        sitemap_file_path = os.path.join(settings.BASE_DIR, 'templates', 'sitemap.xml')        
        with open(sitemap_file_path, 'w', encoding='utf-8') as sitemap_file:
            sitemap_file.write(self.content)