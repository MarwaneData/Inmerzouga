# Generated by Django 5.1.5 on 2025-02-20 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0073_alter_photographypage_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='schema_markup',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='sitemap_changefreq',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='sitemap_priority',
        ),
    ]
