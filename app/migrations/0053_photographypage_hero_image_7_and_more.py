# Generated by Django 5.1.4 on 2025-02-01 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0052_remove_photographypage_hero_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographypage',
            name='hero_image_7',
            field=models.ImageField(blank=True, help_text='Hero grid image 6', upload_to='photography/hero/grid/'),
        ),
        migrations.AddField(
            model_name='photographypage',
            name='hero_image_8',
            field=models.ImageField(blank=True, help_text='Hero grid image 6', upload_to='photography/hero/grid/'),
        ),
    ]
