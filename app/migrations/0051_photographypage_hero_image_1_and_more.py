# Generated by Django 5.1.4 on 2025-02-01 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0050_remove_photographypage_featured_packages_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographypage',
            name='hero_image_1',
            field=models.ImageField(blank=True, help_text='Hero grid image 1', upload_to='photography/hero/grid/'),
        ),
        migrations.AddField(
            model_name='photographypage',
            name='hero_image_2',
            field=models.ImageField(blank=True, help_text='Hero grid image 2', upload_to='photography/hero/grid/'),
        ),
        migrations.AddField(
            model_name='photographypage',
            name='hero_image_3',
            field=models.ImageField(blank=True, help_text='Hero grid image 3', upload_to='photography/hero/grid/'),
        ),
        migrations.AddField(
            model_name='photographypage',
            name='hero_image_4',
            field=models.ImageField(blank=True, help_text='Hero grid image 4', upload_to='photography/hero/grid/'),
        ),
        migrations.AddField(
            model_name='photographypage',
            name='hero_image_5',
            field=models.ImageField(blank=True, help_text='Hero grid image 5', upload_to='photography/hero/grid/'),
        ),
        migrations.AddField(
            model_name='photographypage',
            name='hero_image_6',
            field=models.ImageField(blank=True, help_text='Hero grid image 6', upload_to='photography/hero/grid/'),
        ),
    ]
