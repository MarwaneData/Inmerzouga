# Generated by Django 5.1.4 on 2025-01-18 12:31

import colorfield.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_remove_tourinclusion_tour_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('subtitle', models.TextField()),
                ('description', models.TextField()),
                ('featured_image', models.ImageField(help_text='Small featured image', upload_to='tours/featured/')),
                ('hero_image', models.ImageField(help_text='Large header image', upload_to='tours/hero/')),
                ('hero_overlay_color', colorfield.fields.ColorField(default='#000000', image_field=None, max_length=25, samples=None)),
                ('hero_overlay_opacity', models.DecimalField(decimal_places=2, default=0.5, max_digits=3)),
                ('available_years', models.JSONField(default=list, help_text='List of years tour is available')),
                ('current_year', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('duration_days', models.IntegerField()),
                ('countries_visited', models.IntegerField(default=1)),
                ('cities_visited', models.IntegerField()),
                ('nights_accommodation', models.IntegerField()),
                ('deposit_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('has_deposit_protection', models.BooleanField(default=True)),
                ('has_free_cancellation', models.BooleanField(default=True)),
                ('cancellation_days', models.IntegerField(default=60)),
                ('deposit_percentage', models.IntegerField(default=20)),
                ('booking_features', models.JSONField(default=list, help_text='List of booking features with icons and descriptions')),
                ('map_image', models.ImageField(upload_to='tours/maps/')),
                ('start_location', models.CharField(max_length=200)),
                ('end_location', models.CharField(max_length=200)),
                ('route_description', models.TextField()),
                ('visited_locations', models.JSONField(default=list, help_text='List of locations with coordinates and details')),
                ('map_zoom_default', models.IntegerField(default=8)),
                ('map_center_lat', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('map_center_lng', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('breakfast_count', models.IntegerField()),
                ('lunch_count', models.IntegerField()),
                ('dinner_count', models.IntegerField()),
                ('has_vegetarian_option', models.BooleanField(default=True)),
                ('has_vegan_option', models.BooleanField(default=True)),
                ('dietary_notes', models.TextField(blank=True)),
                ('meal_features', models.JSONField(default=list, help_text='Special meal features and options')),
                ('activity_level', models.CharField(choices=[('easy', 'Easy'), ('moderate', 'Moderate'), ('challenging', 'Challenging')], max_length=20)),
                ('activity_description', models.TextField()),
                ('physical_rating', models.IntegerField(default=2, help_text='1-5 rating of physical difficulty')),
                ('activity_features', models.JSONField(default=list, help_text='List of activity features and requirements')),
                ('currency', models.CharField(default='EUR', max_length=10)),
                ('solo_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duo_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('small_group_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('large_group_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('child_discount_percentage', models.IntegerField(default=25)),
                ('high_season_supplement', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('price_notes', models.JSONField(default=list, help_text='Additional pricing notes with icons')),
                ('price_includes', models.JSONField(default=list, help_text='Detailed list of what price includes')),
                ('seasonal_pricing', models.JSONField(default=dict, help_text='Pricing variations by season')),
                ('recommended_age', models.CharField(blank=True, max_length=100)),
                ('max_group_size', models.IntegerField()),
                ('min_group_size', models.IntegerField(default=1)),
                ('available_languages', models.JSONField(default=list, help_text='List of available languages with flags')),
                ('tour_category', models.CharField(blank=True, max_length=100)),
                ('tour_style', models.CharField(blank=True, max_length=100)),
                ('tour_code', models.CharField(blank=True, max_length=50)),
                ('accommodation_types', models.JSONField(default=list, help_text='List of accommodation types with details')),
                ('room_types', models.JSONField(default=list, help_text='Available room types with descriptions')),
                ('accommodation_features', models.JSONField(default=list, help_text='Special accommodation features')),
                ('transport_types', models.JSONField(default=list, help_text='Types of transport with details')),
                ('transport_features', models.JSONField(default=list, help_text='Special transport features')),
                ('meta_title', models.CharField(blank=True, max_length=200)),
                ('meta_description', models.TextField(blank=True)),
                ('meta_keywords', models.CharField(blank=True, max_length=500)),
                ('social_image', models.ImageField(blank=True, upload_to='tours/social/')),
                ('social_title', models.CharField(blank=True, max_length=200)),
                ('social_description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.TextField()),
                ('order', models.IntegerField(default=0)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faqs', to='app.tour')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='TourDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('price_modifier', models.DecimalField(decimal_places=2, default=1.0, max_digits=5)),
                ('is_guaranteed', models.BooleanField(default=False)),
                ('available_seats', models.IntegerField()),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dates', to='app.tour')),
            ],
            options={
                'ordering': ['start_date'],
            },
        ),
        migrations.CreateModel(
            name='TourExclusion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('icon', models.CharField(default='fas fa-times', max_length=50)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exclusions', to='app.tour')),
            ],
        ),
        migrations.CreateModel(
            name='TourHighlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlight_type', models.CharField(choices=[('visit', 'Visit'), ('discover', 'Discover'), ('see', 'See'), ('scenic_drive', 'Scenic Drive'), ('view', 'View')], max_length=20)),
                ('description', models.TextField()),
                ('icon', models.CharField(default='fas fa-map-marker-alt', max_length=50)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='highlights', to='app.tour')),
            ],
        ),
        migrations.CreateModel(
            name='TourInclusion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inclusion_type', models.CharField(choices=[('accommodation', 'Accommodation'), ('guide', 'Guide'), ('meals', 'Meals'), ('transport', 'Transport'), ('activities', 'Activities'), ('additional', 'Additional Services')], max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('items', models.TextField()),
                ('icon', models.CharField(default='fas fa-check-circle', max_length=50)),
                ('has_dietary_options', models.BooleanField(default=False)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inclusions', to='app.tour')),
            ],
        ),
        migrations.CreateModel(
            name='TourItineraryDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_number', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(blank=True, max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('main_image', models.ImageField(upload_to='tours/itinerary/')),
                ('gallery_images', models.JSONField(default=list, help_text='Additional day images with captions')),
                ('accommodation', models.CharField(max_length=200)),
                ('accommodation_link', models.URLField(blank=True)),
                ('accommodation_details', models.JSONField(default=dict, help_text='Detailed accommodation information')),
                ('included_meals', models.JSONField(default=list, help_text='List of included meals with details')),
                ('distance_covered', models.CharField(blank=True, max_length=100)),
                ('travel_time', models.CharField(blank=True, max_length=100)),
                ('elevation_gain', models.CharField(blank=True, max_length=100)),
                ('is_welcome_day', models.BooleanField(default=False)),
                ('activities', models.JSONField(default=list, help_text='List of activities with details')),
                ('highlights', models.JSONField(default=list, help_text='Day highlights with icons')),
                ('transport_modes', models.JSONField(default=list, help_text='Transport modes with icons')),
                ('weather_info', models.JSONField(blank=True, default=dict, help_text='Typical weather conditions')),
                ('special_notes', models.TextField(blank=True)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itinerary_days', to='app.tour')),
            ],
            options={
                'ordering': ['day_number'],
            },
        ),
        migrations.CreateModel(
            name='TourPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='tours/photos/')),
                ('caption', models.CharField(max_length=200)),
                ('alt_text', models.CharField(max_length=200)),
                ('is_featured', models.BooleanField(default=False)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('category', models.CharField(blank=True, max_length=200)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='app.tour')),
            ],
        ),
    ]
