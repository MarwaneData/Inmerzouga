# Generated by Django 5.1.5 on 2025-01-25 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_activitiespage_activities_section_subtitle_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitiespage',
            name='activities_section_subtitle',
        ),
        migrations.RemoveField(
            model_name='activitiespage',
            name='activities_section_title',
        ),
        migrations.RemoveField(
            model_name='activitiespage',
            name='contact_text',
        ),
        migrations.RemoveField(
            model_name='activitiespage',
            name='contact_title',
        ),
        migrations.RemoveField(
            model_name='activitiespage',
            name='intro_text',
        ),
        migrations.RemoveField(
            model_name='activitiespage',
            name='show_contact_section',
        ),
        migrations.RemoveField(
            model_name='activitiespage',
            name='social_description',
        ),
        migrations.RemoveField(
            model_name='activitiespage',
            name='social_image',
        ),
        migrations.RemoveField(
            model_name='activitiespage',
            name='social_title',
        ),
    ]
