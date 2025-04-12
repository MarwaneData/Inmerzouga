from django.contrib import admin
from django.utils.html import format_html
from django import forms
from .models import (
    Tour, TourDay, TourHighlight, TourInclusion, TourExclusion, 
    FAQ, TourCustomerPhoto, ExtraActivity, TourPrice,
    LuxuryCamp, LuxuryCampInclusion, LuxuryCampExclusion, LuxuryCampActivity, 
    LuxuryCampPrice, LuxuryCampFAQ, LuxuryCampPhoto, LuxuryCampExperience,
    TourDayOverview, ActivitiesPage, Activity,
    DayTrip, DayTripCustomerPhoto, DayTripActivity, 
    DayTripInclusion, DayTripExclusion, DayTripHighlight,
    DayTripFAQ, DayTripPrice,
    City, CityGalleryImage, CityHighlight, CityAttraction, CityNeighborhood, LocalExperience, CitySection,
    PhotographyPage, Package, PhotographyImage,
    AboutPage, AboutTestimonial, AboutGalleryImage,
    EventsPage, Event, EventInclusion,
    HomePage, ThingsToDoSection, MuseumSection, FoodSection,
    Contact, Promo, SiteMapEntry
)

# Customize admin site
admin.site.site_header = 'INMERZOUGA'
admin.site.site_title = 'INMERZOUGA Admin'
admin.site.index_title = 'INMERZOUGA Administration'

class TourDayInline(admin.StackedInline):
    model = TourDay
    extra = 0  # Start with no empty form
    classes = ['collapse']  # Makes it collapsible
    fieldsets = (
        ('Day Information', {
            'classes': ('wide',),
            'fields': (
                'day_number',
                'title',
                'location',
                'description',
            )
        }),
        ('Media', {
            'classes': ('collapse',),
            'fields': (
                'image',
            )
        }),
        ('Accommodation & Meals', {
            'classes': ('collapse',),
            'fields': (
                'hotel_name',
                'hotel_link',
                ('breakfast', 'lunch', 'dinner'),
            )
        }),
    )
    ordering = ['day_number']

class TourHighlightInline(admin.TabularInline):
    model = TourHighlight
    extra = 0
    classes = ['collapse']
    fields = ('highlight_type', 'description', 'icon', 'order')
    ordering = ['order']

class TourInclusionInline(admin.TabularInline):
    model = TourInclusion
    extra = 0
    classes = ['collapse']
    fields = ('inclusion_type', 'title', 'description', 'order')
    ordering = ['order']

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        form = formset.form
        form.base_fields['inclusion_type'].help_text = 'Icons will be automatically assigned based on type'
        return formset

class TourExclusionInline(admin.TabularInline):
    model = TourExclusion
    extra = 0
    classes = ['collapse']
    fields = ('title', 'description', 'icon', 'order')
    ordering = ['order']

class FAQInline(admin.TabularInline):
    model = FAQ
    extra = 0
    classes = ['collapse']
    fields = ('question', 'answer', 'order')
    ordering = ['order']

class TourCustomerPhotoInline(admin.TabularInline):
    model = TourCustomerPhoto
    extra = 0
    classes = ['collapse']
    fields = ('image', 'caption', 'location', 'date_taken', 'order')
    ordering = ['order']

class ExtraActivityInline(admin.StackedInline):
    model = ExtraActivity
    extra = 0
    classes = ['collapse']
    fields = ('title', 'description', 'duration', 'price', 'image', 'is_recommended', 'order')
    ordering = ['order']

class TourPriceInline(admin.TabularInline):
    model = TourPrice
    extra = 1

class LuxuryCampInclusionInline(admin.TabularInline):
    model = LuxuryCampInclusion
    extra = 1

class LuxuryCampExclusionInline(admin.TabularInline):
    model = LuxuryCampExclusion
    extra = 1

class LuxuryCampActivityInline(admin.TabularInline):
    model = LuxuryCampActivity
    extra = 1

class LuxuryCampPriceInline(admin.TabularInline):
    model = LuxuryCampPrice
    extra = 1

class LuxuryCampFAQInline(admin.TabularInline):
    model = LuxuryCampFAQ
    extra = 1

class LuxuryCampPhotoInline(admin.TabularInline):
    model = LuxuryCampPhoto
    extra = 1

class LuxuryCampExperienceInline(admin.TabularInline):
    model = LuxuryCampExperience
    extra = 1
    fields = ('title', 'icon', 'order')
    ordering = ['order']

class TourDayOverviewInline(admin.TabularInline):
    model = TourDayOverview
    extra = 0
    fields = ('day_number', 'title', 'description', 'order')
    ordering = ['order', 'day_number']

class DayTripCustomerPhotoInline(admin.TabularInline):
    model = DayTripCustomerPhoto
    extra = 0
    classes = ['collapse']
    fields = ('image', 'caption', 'order')
    ordering = ['order']

class DayTripActivityInline(admin.StackedInline):
    model = DayTripActivity
    extra = 0
    classes = ['collapse']
    fields = ('title', 'description', 'duration', 'order')
    ordering = ['order']

class DayTripInclusionInline(admin.TabularInline):
    model = DayTripInclusion
    extra = 0
    classes = ['collapse']
    fields = ('title', 'description', 'icon', 'order')
    ordering = ['order']

class DayTripExclusionInline(admin.TabularInline):
    model = DayTripExclusion
    extra = 0
    classes = ['collapse']
    fields = ('title', 'description', 'icon', 'order')
    ordering = ['order']

class DayTripHighlightInline(admin.TabularInline):
    model = DayTripHighlight
    extra = 0
    classes = ['collapse']
    fields = ('highlight_type', 'description', 'icon', 'order')
    ordering = ['order']

class DayTripFAQInline(admin.TabularInline):
    model = DayTripFAQ
    extra = 0
    classes = ['collapse']
    fields = ('question', 'answer', 'order')
    ordering = ['order']

class DayTripPriceInline(admin.TabularInline):
    model = DayTripPrice
    extra = 0
    classes = ['collapse']
    fields = ('title', 'price', 'description', 'order')
    ordering = ['order']

class CitySectionInline(admin.StackedInline):
    model = CitySection
    extra = 1
    classes = ['collapse']
    fields = ('title', 'content', 'image', 'order')

class CityGalleryImageInline(admin.TabularInline):
    model = CityGalleryImage
    extra = 1
    fields = ('image', 'caption', 'is_featured', 'order')

class CityHighlightInline(admin.TabularInline):
    model = CityHighlight
    extra = 1

class CityAttractionInline(admin.StackedInline):
    model = CityAttraction
    extra = 1

class CityNeighborhoodInline(admin.StackedInline):
    model = CityNeighborhood
    extra = 1

class LocalExperienceInline(admin.StackedInline):
    model = LocalExperience
    extra = 1

# First define the inline classes
class AboutTestimonialInline(admin.TabularInline):
    model = AboutTestimonial
    extra = 1
    ordering = ['order']

class AboutGalleryImageInline(admin.TabularInline):
    model = AboutGalleryImage
    extra = 1
    ordering = ['order']

# Then define the main admin class
@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle', 'hero_image')
        }),
        ('About Section', {
            'fields': ('about_title', 'about_description', 'about_image')
        }),
        ('Statistics', {
            'fields': ('happy_travelers_count', 'social_followers_count')
        }),
        ('Video Section', {
            'fields': (
                'video_section_title', 
                'video_section_description',
                'video_thumbnail',
                'video_url',
                'video_type'
            )
        }),
        ('Basic SEO', {
            'classes': ('collapse',),
            'fields': (
                'meta_title',
                'meta_description',
                'meta_keywords',
            ),
            'description': 'Basic SEO settings for search engines'
        }),
        ('Social Media (Open Graph)', {
            'classes': ('collapse',),
            'fields': (
                'og_title',
                'og_description',
                'og_image',
                'og_type',
            ),
            'description': 'Settings for social media sharing (Facebook, LinkedIn)'
        }),
        ('Twitter Cards', {
            'classes': ('collapse',),
            'fields': (
                'twitter_card',
                'twitter_title',
                'twitter_description',
                'twitter_image',
            ),
            'description': 'Settings for Twitter sharing'
        }),
        ('Advanced SEO', {
            'classes': ('collapse',),
            'fields': (
                'canonical_url',
                ('robots_index', 'robots_follow'),
            ),
            'description': 'Advanced SEO settings and custom markup'
        }),
    )
    
    inlines = [AboutTestimonialInline, AboutGalleryImageInline]
    
    def has_add_permission(self, request):
        # Only allow one AboutPage instance
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Basic Information', {
            'fields': (
                'title',
                'short_title',
                'slug',
                'description',
                'main_image',
                'small_image',
                'is_active',
                'is_group',
                'is_day_trip',
                'day_trip_time',
            )
        }),
        ('Quick Facts', {
            'fields': (
                'duration',
                'countries',
                'cities',
                'nights',
            )
        }),
        ('Meals', {
            'fields': (
                'breakfast_count',
                'lunch_count',
                'dinner_count',
            )
        }),
        ('Activity & Booking', {
            'fields': (
                'activity_level',
                'activity_description',
                'low_deposit',
                'child_discount',
                'map_image',
            )
        }),
        ('Basic SEO', {
            'classes': ('collapse',),
            'fields': (
                'meta_title',
                'meta_description',
                'meta_keywords',
            ),
            'description': 'Basic SEO settings for search engines'
        }),
        ('Social Media (Open Graph)', {
            'classes': ('collapse',),
            'fields': (
                'og_title',
                'og_description',
                'og_image',
                'og_type',
            ),
            'description': 'Settings for social media sharing (Facebook, LinkedIn)'
        }),
        ('Twitter Cards', {
            'classes': ('collapse',),
            'fields': (
                'twitter_card',
                'twitter_title',
                'twitter_description',
                'twitter_image',
            ),
            'description': 'Settings for Twitter sharing'
        }),
        ('Advanced SEO', {
            'classes': ('collapse',),
            'fields': (
                'canonical_url',
                ('robots_index', 'robots_follow'),
            ),
            'description': 'Advanced SEO settings and custom markup'
        }),
    )
    
    list_display = ('title', 'short_title', 'duration', 'is_active', 'is_group')
    list_filter = ('is_active', 'is_group', 'activity_level')
    search_fields = ('title', 'description')
    inlines = [
        TourDayOverviewInline,
        TourDayInline,
        TourHighlightInline,
        TourInclusionInline,
        TourExclusionInline,
        ExtraActivityInline,
        FAQInline,
        TourCustomerPhotoInline,
        TourPriceInline
    ]

    def get_fieldsets(self, request, obj=None):
        # Base fieldsets that always show
        fieldsets = super().get_fieldsets(request, obj)
        
        # Only show day trip fields if is_day_trip is True
        if obj and obj.is_day_trip:
            fieldsets += (
                ('Day Trip Details', {
                    'classes': ('wide',),
                    'fields': (
                        'day_trip_time',
                        'day_trip_location',
                        'max_persons',
                    )
                }),
            )
        else:
            # Show regular tour fields
            fieldsets += (
                ('Tour Overview', {
                    'classes': ('wide',),
                    'fields': (
                        ('duration', 'countries', 'cities', 'nights'),
                    )
                }),
            )
        return fieldsets

    def title_with_status(self, obj):
        if obj.is_active:
            return format_html('<span style="color: green;">✓</span> {}', obj.title)
        return format_html('<span style="color: red;">×</span> {}', obj.title)
    title_with_status.short_description = 'Tour Title'
    
    def duration_display(self, obj):
        return format_html('{} days / {} nights', obj.duration, obj.nights)
    duration_display.short_description = 'Duration'
    
    actions = ['duplicate_tour']
    
    def duplicate_tour(self, request, queryset):
        for tour in queryset:
            # Store original title
            original_title = tour.title
            
            # Create new tour
            tour.pk = None
            tour.title = f"Copy of {original_title}"
            tour.slug = None
            tour.save()
            
            # Get both tours
            new_tour = Tour.objects.get(title=f"Copy of {original_title}")
            old_tour = Tour.objects.get(title=original_title)
            
            # Copy all related items
            for day in old_tour.days.all():
                day.pk = None
                day.tour = new_tour
                day.save()
                
            for overview in old_tour.day_overviews.all():
                overview.pk = None
                overview.tour = new_tour
                overview.save()
                
            for highlight in old_tour.highlights.all():
                highlight.pk = None
                highlight.tour = new_tour
                highlight.save()
                
            for inclusion in old_tour.inclusions.all():
                inclusion.pk = None
                inclusion.tour = new_tour
                inclusion.save()
                
            for exclusion in old_tour.exclusions.all():
                exclusion.pk = None
                exclusion.tour = new_tour
                exclusion.save()
                
            for photo in old_tour.customer_photos.all():
                photo.pk = None
                photo.tour = new_tour
                photo.save()
                
            for activity in old_tour.extra_activities.all():
                activity.pk = None
                activity.tour = new_tour
                activity.save()
                
            for price in old_tour.prices.all():
                price.pk = None
                price.tour = new_tour
                price.save()
    
    duplicate_tour.short_description = "Duplicate selected tours"
    
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }
        js = ('admin/js/custom_admin.js',)

@admin.register(TourDay)
class TourDayAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict to hide from admin index
        """
        return {}

    # Keep the existing configuration for when it's accessed through Tour
    list_display = ('day_number', 'tour', 'title', 'location')
    list_filter = ('tour',)
    search_fields = ('title', 'description', 'location')
    ordering = ['tour', 'day_number']
    
    fieldsets = (
        ('Day Information', {
            'fields': (
                ('day_number', 'tour'),
                'title',
                'location',
                'description',
            )
        }),
        ('Media & Details', {
            'classes': ('collapse',),
            'fields': (
                'image',
                'hotel_name',
                'hotel_link',
                ('breakfast', 'lunch', 'dinner'),
            )
        }),
    )

@admin.register(LuxuryCamp)
class LuxuryCampAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'duration', 'group_size')
    search_fields = ('title', 'description', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        ('Basic Information', {
            'fields': (
                'title',
                'slug',
                'subtitle',
                'description',
                'hero_image',
            )
        }),
        ('Section Images', {
            'fields': (
                ('main_section_image', 'main_section_image_caption'),
                ('section_image_1', 'section_image_1_caption'),
                ('section_image_2', 'section_image_2_caption'),
                ('section_image_3', 'section_image_3_caption'),
            ),
            'description': 'Images for the luxury camp section grid'
        }),
        ('Hero Features', {
            'fields': (
                ('hero_feature_1_icon', 'hero_feature_1_text'),
                ('hero_feature_2_icon', 'hero_feature_2_text'),
                ('hero_feature_3_icon', 'hero_feature_3_text'),
            )
        }),
        ('Quick Facts', {
            'fields': (
                'duration',
                'group_size',
                'meals_included',
            )
        }),
    )
    inlines = [
        LuxuryCampExperienceInline,
        LuxuryCampInclusionInline,
        LuxuryCampExclusionInline,
        LuxuryCampActivityInline,
        LuxuryCampPriceInline,
        LuxuryCampFAQInline,
        LuxuryCampPhotoInline,
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['hero_image'].help_text = 'Main hero image displayed at the top of the page (1920x1080 recommended)'
        return form

    actions = ['duplicate_camp']

    def duplicate_camp(self, request, queryset):
        for camp in queryset:
            # Create a copy of the camp
            camp.pk = None
            camp.title = f"{camp.title} (Copy)"
            camp.slug = f"{camp.slug}-copy"
            camp.save()

            # Copy all related objects
            old_camp = LuxuryCamp.objects.get(slug=camp.slug.replace('-copy', ''))
            
            # Copy experiences
            for exp in old_camp.experiences.all():
                exp.pk = None
                exp.camp = camp
                exp.save()

            # Copy inclusions
            for inc in old_camp.inclusions.all():
                inc.pk = None
                inc.camp = camp
                inc.save()

            # Copy exclusions
            for exc in old_camp.exclusions.all():
                exc.pk = None
                exc.camp = camp
                exc.save()

            # Copy activities
            for act in old_camp.activities.all():
                act.pk = None
                act.camp = camp
                act.save()

            # Copy prices
            for price in old_camp.prices.all():
                price.pk = None
                price.camp = camp
                price.save()

            # Copy FAQs
            for faq in old_camp.faqs.all():
                faq.pk = None
                faq.camp = camp
                faq.save()

            # Copy photos
            for photo in old_camp.photos.all():
                photo.pk = None
                photo.camp = camp
                photo.save()

    duplicate_camp.short_description = "Duplicate selected luxury camps"

@admin.register(ActivitiesPage)
class ActivitiesPageAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Page Content', {
            'fields': (
                'title',
                'subtitle',
                'hero_image',
            )
        }),
        ('Basic SEO', {
            'classes': ('collapse',),
            'fields': (
                'meta_title',
                'meta_description',
                'meta_keywords',
            ),
            'description': 'Basic SEO settings for search engines'
        }),
        ('Social Media (Open Graph)', {
            'classes': ('collapse',),
            'fields': (
                'og_title',
                'og_description',
                'og_image',
                'og_type',
            ),
            'description': 'Settings for social media sharing (Facebook, LinkedIn)'
        }),
        ('Twitter Cards', {
            'classes': ('collapse',),
            'fields': (
                'twitter_card',
                'twitter_title',
                'twitter_description',
                'twitter_image',
            ),
            'description': 'Settings for Twitter sharing'
        }),
        ('Advanced SEO', {
            'classes': ('collapse',),
            'fields': (
                'canonical_url',
                ('robots_index', 'robots_follow'),
            ),
            'description': 'Advanced SEO settings and custom markup'
        }),
    )

    def has_add_permission(self, request):
        # Only allow one instance
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'price', 'difficulty', 'is_active')
    list_filter = ('difficulty', 'is_active')
    search_fields = ('title', 'description')
    
    fieldsets = (
        ('Basic Information', {
            'fields': (
                'title',
                'description',
                'image',
                'duration',
                ('min_group_size', 'max_group_size'),
                'difficulty',
                ('price', 'price_suffix'),
                'order',
                'is_active'
            )
        }),
    )

@admin.register(DayTrip)
class DayTripAdmin(admin.ModelAdmin):
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}
    
    list_display = ('title_with_status', 'slug', 'duration_display', 'city', 'is_group')
    list_filter = ('is_active', 'is_group', 'city')
    search_fields = ('title', 'description', 'city', 'slug')
    
    fieldsets = (
        ('Basic Information', {
            'classes': ('collapse',),
            'fields': (
                'title',
                'slug',
                'description',
                'is_active',
                'is_group',
            )
        }),
        ('Media', {
            'classes': ('collapse',),
            'fields': (
                'main_image',
                'small_image',
            )
        }),
        ('Day Trip Details', {
            'classes': ('collapse',),
            'fields': (
                'duration_hours',
                'city',
                'start_time',
                'max_persons',
            ),
            'description': 'Basic day trip details'
        }),
        ('Basic SEO', {
            'classes': ('collapse',),
            'fields': (
                'meta_title',
                'meta_description',
                'meta_keywords',
            ),
            'description': 'Basic SEO settings for search engines'
        }),
        ('Social Media (Open Graph)', {
            'classes': ('collapse',),
            'fields': (
                'og_title',
                'og_description',
                'og_image',
                'og_type',
            ),
            'description': 'Settings for social media sharing (Facebook, LinkedIn)'
        }),
        ('Twitter Cards', {
            'classes': ('collapse',),
            'fields': (
                'twitter_card',
                'twitter_title',
                'twitter_description',
                'twitter_image',
            ),
            'description': 'Settings for Twitter sharing'
        }),
        ('Advanced SEO', {
            'classes': ('collapse',),
            'fields': (
                'canonical_url',
                ('robots_index', 'robots_follow'),
            ),
            'description': 'Advanced SEO settings and custom markup'
        }),
    )
    
    inlines = [
        DayTripPriceInline,
        DayTripHighlightInline,
        DayTripInclusionInline,
        DayTripExclusionInline,
        DayTripActivityInline,
        DayTripCustomerPhotoInline,
        DayTripFAQInline,
    ]

    actions = ['duplicate_daytrip']
    
    def duplicate_daytrip(self, request, queryset):
        from django.utils.text import slugify
        import random
        import string
        
        def generate_unique_slug(title):
            # Generate initial slug
            slug = slugify(title)
            # Add random string to make it unique
            random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
            return f"{slug}-{random_string}"
            
        for daytrip in queryset:
            # Store original title
            original_title = daytrip.title
            
            # Create new daytrip with unique slug
            daytrip.pk = None
            daytrip.title = f"Copy of {original_title}"
            daytrip.slug = generate_unique_slug(daytrip.title)
            daytrip.save()
            
            # Get both daytrips
            new_daytrip = DayTrip.objects.get(slug=daytrip.slug)
            old_daytrip = DayTrip.objects.get(title=original_title)
            
            # Copy all related items
            for highlight in old_daytrip.highlights.all():
                highlight.pk = None
                highlight.daytrip = new_daytrip
                highlight.save()
                
            for inclusion in old_daytrip.inclusions.all():
                inclusion.pk = None
                inclusion.daytrip = new_daytrip
                inclusion.save()
                
            for exclusion in old_daytrip.exclusions.all():
                exclusion.pk = None
                exclusion.daytrip = new_daytrip
                exclusion.save()
                
            for activity in old_daytrip.activities.all():
                activity.pk = None
                activity.daytrip = new_daytrip
                activity.save()
                
            for faq in old_daytrip.faqs.all():
                faq.pk = None
                faq.daytrip = new_daytrip
                faq.save()
                
            for price in old_daytrip.prices.all():
                price.pk = None
                price.daytrip = new_daytrip
                price.save()
                
            for photo in old_daytrip.customer_photos.all():
                photo.pk = None
                photo.daytrip = new_daytrip
                photo.save()
    duplicate_daytrip.short_description = "Duplicate selected day trips"
    def title_with_status(self, obj):
        if obj.is_active:
            return format_html('<span style="color: green;">✓</span> {}', obj.title)
        return format_html('<span style="color: red;">×</span> {}', obj.title)
    title_with_status.short_description = 'Day Trip Title'
    
    def duration_display(self, obj):
        return format_html('{} hours', obj.duration_hours)
    duration_display.short_description = 'Duration'

    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }
        js = ('admin/js/custom_admin.js',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        ('Basic Information', {
            'fields': (
                'title',
                'slug',
                'hero_image',
                'description',
            )
        }),
        ('Settings', {
            'fields': (
                'is_active',
                'order'
            )
        }),
    )
    
    inlines = [
        CitySectionInline,
        CityGalleryImageInline,
    ]

class PhotographyImageInline(admin.TabularInline):
    model = PhotographyImage
    extra = 1
    fields = ('image', 'title', 'category', 'is_hero', 'is_active', 'order')

@admin.register(PhotographyPage)
class PhotographyPageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Page Information', {
            'fields': ('title', 'slug', 'description', 'is_active')
        }),
        ('Hero Section', {
            'fields': (
                'hero_title', 
                'hero_subtitle'
            ),
            'description': 'Configure the hero section text'
        }),
        ('Hero Grid Images', {
            'fields': (
                ('hero_image_1', 'hero_image_2'),
                ('hero_image_3', 'hero_image_4'),
                ('hero_image_5', 'hero_image_6'),
                ('hero_image_7', 'hero_image_8'),
            ),
            'description': 'Upload 8 images for the hero grid'
        }),
        ('Basic SEO', {
            'classes': ('collapse',),
            'fields': (
                'meta_title',
                'meta_description',
                'meta_keywords',
            ),
            'description': 'Basic SEO settings for search engines'
        }),
        ('Social Media (Open Graph)', {
            'classes': ('collapse',),
            'fields': (
                'og_title',
                'og_description',
                'og_image',
                'og_type',
            ),
            'description': 'Settings for social media sharing (Facebook, LinkedIn)'
        }),
        ('Twitter Cards', {
            'classes': ('collapse',),
            'fields': (
                'twitter_card',
                'twitter_title',
                'twitter_description',
                'twitter_image',
            ),
            'description': 'Settings for Twitter sharing'
        }),
        ('Advanced SEO', {
            'classes': ('collapse',),
            'fields': (
                'canonical_url',
                ('robots_index', 'robots_follow'),
            ),
            'description': 'Advanced SEO settings and custom markup'
        }),
    )
    inlines = [PhotographyImageInline]
    list_display = ('title', 'is_active', 'updated_at')

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'package_type', 'photo_count', 'price')
    list_filter = ('package_type',)
    search_fields = ('title',)
    
    fieldsets = (
        ('Package Information', {
            'fields': (
                'title',
                'package_type',
                'price',
                'order',
                'image',
            )
        }),
        ('Photography Features', {
            'fields': (
                'photo_count',
                'editing_hours',
                'retouches',
                'digital_delivery',
            ),
            'description': 'Specify what is included in this package'
        }),
    )
    
    def get_ordering(self, request):
        return ['order', 'package_type']

class EventInclusionInline(admin.TabularInline):
    model = Event.includes.through
    extra = 1
    verbose_name = "Included Item"
    verbose_name_plural = "Included Items"
    fields = ('eventinclusion',)
    ordering = ('eventinclusion__order',)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by('eventinclusion__order')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'duration', 'group_size', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    list_filter = ('is_active',)
    search_fields = ('title', 'description', 'type')
    exclude = ('includes',)
    
    fieldsets = (
        ('Basic Information', {
            'fields': (
                'title',
                'type',
                'description',
            )
        }),
        ('Event Details', {
            'fields': (
                'duration',
                'group_size',
                'price_info',
            )
        }),
        ('Pricing', {
            'fields': ('prices',),
            'description': 'Enter each price on a new line (e.g., "1-2 persons: 340€")'
        }),
        ('Media', {
            'fields': (
                'image',
            ),
            'classes': ('collapse',)
        }),
        ('Settings', {
            'fields': (
                'is_active',
                'order',
                'page',
            ),
            'classes': ('collapse',)
        }),
    )
    
    inlines = [EventInclusionInline]
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['description'].widget.attrs['rows'] = 4
        form.base_fields['prices'].widget.attrs['rows'] = 4
        form.base_fields['page'].widget.attrs['style'] = 'display: none;'
        return form

@admin.register(EventInclusion)
class EventInclusionAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_preview', 'order')
    list_editable = ('order',)
    search_fields = ('title',)
    
    def icon_preview(self, obj):
        return format_html('<i class="{}"></i> {}', obj.icon, obj.icon)
    icon_preview.short_description = 'Icon'
    
    def get_model_perms(self, request):
        """Hide this model from admin index"""
        return {}

@admin.register(EventsPage)
class EventsPageAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Page Information', {
            'fields': (
                'title',
                'subtitle',
                'is_active',
            )
        }),
        ('Hero Section', {
            'fields': (
                'hero_image_1',
                'hero_image_2',
                'hero_image_3',
            ),
            'description': 'Hero section images'
        }),
        ('Basic SEO', {
            'classes': ('collapse',),
            'fields': (
                'meta_title',
                'meta_description',
                'meta_keywords',
            ),
            'description': 'Basic SEO settings for search engines'
        }),
        ('Social Media (Open Graph)', {
            'classes': ('collapse',),
            'fields': (
                'og_title',
                'og_description',
                'og_image',
                'og_type',
            ),
            'description': 'Settings for social media sharing (Facebook, LinkedIn)'
        }),
        ('Twitter Cards', {
            'classes': ('collapse',),
            'fields': (
                'twitter_card',
                'twitter_title',
                'twitter_description',
                'twitter_image',
            ),
            'description': 'Settings for Twitter sharing'
        }),
        ('Advanced SEO', {
            'classes': ('collapse',),
            'fields': (
                'canonical_url',
                ('robots_index', 'robots_follow'),
            ),
            'description': 'Advanced SEO settings and custom markup'
        }),
    )
    
    list_display = ('title', 'is_active')

    def has_add_permission(self, request):
        # Only allow one instance
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

class ThingsToDoInline(admin.TabularInline):
    model = ThingsToDoSection
    extra = 1
    fields = ('title', 'description', 'order', 'is_active')
    ordering = ['order']

class MuseumSectionInline(admin.TabularInline):
    model = MuseumSection
    extra = 1
    fields = ('title', 'description', 'order', 'is_active')
    ordering = ['order']

class FoodSectionInline(admin.TabularInline):
    model = FoodSection
    extra = 1
    fields = ('title', 'description', 'order', 'is_active')
    ordering = ['order']

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Hero Section', {
            'fields': (
                'hero_title',
                'hero_subtitle',
                'hero_image',
                'hero_rating',
                'hero_button_text',
            )
        }),
        ('Basic SEO', {
            'classes': ('collapse',),
            'fields': (
                'meta_title',
                'meta_description',
                'meta_keywords',
            ),
            'description': 'Basic SEO settings for search engines'
        }),
        ('Social Media (Open Graph)', {
            'classes': ('collapse',),
            'fields': (
                'og_title',
                'og_description',
                'og_image',
                'og_type',
            ),
            'description': 'Settings for social media sharing (Facebook, LinkedIn)'
        }),
        ('Twitter Cards', {
            'classes': ('collapse',),
            'fields': (
                'twitter_card',
                'twitter_title',
                'twitter_description',
                'twitter_image',
            ),
            'description': 'Settings for Twitter sharing'
        }),
        ('Advanced SEO', {
            'classes': ('collapse',),
            'fields': (
                'canonical_url',
                ('robots_index', 'robots_follow'),
            ),
            'description': 'Advanced SEO settings and custom markup'
        }),
    )

    inlines = [
        ThingsToDoInline,
        MuseumSectionInline,
        FoodSectionInline
    ]

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

# Hide these models from admin index but keep them registered
@admin.register(ThingsToDoSection)
class ThingsToDoAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """Hide this model from admin index"""
        return {}

@admin.register(MuseumSection)
class MuseumSectionAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """Hide this model from admin index"""
        return {}

@admin.register(FoodSection)
class FoodSectionAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """Hide this model from admin index"""
        return {}

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Contact Information', {
            'fields': (
                'phone',
                'whatsapp',
                'email',
            )
        }),
        ('Social Media', {
            'fields': (
                'instagram',
                'youtube',
            )
        }),
        ('Settings', {
            'fields': ('is_active',),
        }),
    )

    def has_add_permission(self, request):
        # Only allow one instance
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ('title', 'discount', 'is_active', 'start_date', 'end_date')
    list_filter = ('is_active',)
    
    fieldsets = (
        ('Promo Details', {
            'fields': ('title', 'discount', 'image', 'link')
        }),
        ('Features', {
            'fields': (
                'feature1_text',
                'feature2_text',
                'feature3_text',
            )
        }),
        ('Settings', {
            'fields': ('is_active', 'start_date', 'end_date')
        })
    )

class AdminSite(admin.AdminSite):
    def each_context(self, request):
        context = super().each_context(request)
        context['has_permission'] = request.user.is_active and request.user.is_staff
        return context

    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }

# Create a custom admin site instance
admin_site = AdminSite()

# Register your models with the custom admin site
admin_site.register(Tour, TourAdmin)
# ... register other models ...


class SiteMapEntryAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    fields = ('name', 'content')  
    search_fields = ('name',) 

admin.site.register(SiteMapEntry, SiteMapEntryAdmin)