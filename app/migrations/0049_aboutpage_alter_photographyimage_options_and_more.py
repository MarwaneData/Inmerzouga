# Generated by Django 5.1.4 on 2025-01-31 17:58

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0048_package'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_title', models.CharField(help_text="Main hero title (e.g. 'Discover the Magic of Merzouga')", max_length=200)),
                ('hero_subtitle', models.TextField(help_text='Hero subtitle/description')),
                ('hero_image', models.ImageField(help_text='Hero background image', upload_to='about/')),
                ('about_title', models.CharField(help_text="About section title (e.g. 'About Inmerzouga')", max_length=200)),
                ('about_description', models.TextField(help_text='Main about description')),
                ('about_image', models.ImageField(help_text='About section image', upload_to='about/')),
                ('happy_travelers_count', models.IntegerField(help_text='Number of happy travelers (e.g. 15000)')),
                ('social_followers_count', models.IntegerField(help_text='Number of social media followers')),
                ('video_section_title', models.CharField(help_text='Title for video section', max_length=200)),
                ('video_section_description', models.TextField(help_text='Description for video section')),
                ('video_thumbnail', models.ImageField(help_text='Video thumbnail image', upload_to='about/video/')),
                ('video_url', models.URLField(help_text='YouTube or Vimeo video URL')),
                ('video_type', models.CharField(choices=[('youtube', 'YouTube'), ('vimeo', 'Vimeo')], default='youtube', help_text='Type of video platform', max_length=20)),
            ],
            options={
                'verbose_name': 'About Page',
                'verbose_name_plural': 'About Page',
            },
        ),
        migrations.AlterModelOptions(
            name='photographyimage',
            options={'ordering': ['order']},
        ),
        migrations.RemoveField(
            model_name='photographypage',
            name='about_content',
        ),
        migrations.RemoveField(
            model_name='photographypage',
            name='about_image',
        ),
        migrations.RemoveField(
            model_name='photographypage',
            name='about_title',
        ),
        migrations.RemoveField(
            model_name='photographypage',
            name='contact_button_text',
        ),
        migrations.RemoveField(
            model_name='photographypage',
            name='contact_content',
        ),
        migrations.RemoveField(
            model_name='photographypage',
            name='contact_title',
        ),
        migrations.RemoveField(
            model_name='photographypage',
            name='gallery_description',
        ),
        migrations.RemoveField(
            model_name='photographypage',
            name='gallery_images',
        ),
        migrations.RemoveField(
            model_name='photographypage',
            name='gallery_title',
        ),
        migrations.RemoveField(
            model_name='photographypage',
            name='hero_background',
        ),
        migrations.AddField(
            model_name='photographyimage',
            name='category',
            field=models.CharField(blank=True, choices=[('landscape', 'Landscape'), ('portrait', 'Portrait'), ('culture', 'Culture'), ('events', 'Events')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='photographyimage',
            name='is_hero',
            field=models.BooleanField(default=False, help_text='Show in hero section'),
        ),
        migrations.AddField(
            model_name='photographyimage',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='app.photographypage'),
        ),
        migrations.AddField(
            model_name='photographypage',
            name='featured_packages',
            field=models.ManyToManyField(blank=True, related_name='featured_in_pages', to='app.package'),
        ),
        migrations.AlterField(
            model_name='photographypage',
            name='hero_subtitle',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='photographypage',
            name='hero_title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='photographypage',
            name='meta_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='photographypage',
            name='meta_title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='portfolioimage',
            name='category',
            field=models.CharField(blank=True, choices=[('landscape', 'Landscape'), ('portrait', 'Portrait'), ('culture', 'Culture')], max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='AboutGalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Gallery image', upload_to='about/gallery/')),
                ('title', models.CharField(help_text='Image title/alt text', max_length=200)),
                ('location', models.CharField(help_text="Location label (e.g. 'Merzouga Dunes')", max_length=100)),
                ('order', models.IntegerField(default=0, help_text='Order of appearance')),
                ('about_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='app.aboutpage')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='AboutTestimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Client photo', upload_to='about/testimonials/')),
                ('name', models.CharField(help_text='Client name', max_length=100)),
                ('country', models.CharField(help_text="Client's country", max_length=100)),
                ('content', models.TextField(help_text='Testimonial content')),
                ('rating', models.IntegerField(default=5, help_text='Rating from 1-5 stars', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('order', models.IntegerField(default=0, help_text='Order of appearance')),
                ('about_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testimonials', to='app.aboutpage')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
