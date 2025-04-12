# Generated by Django 5.1.5 on 2025-01-27 17:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_remove_city_best_season_remove_city_best_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='hero_image',
        ),
        migrations.RemoveField(
            model_name='city',
            name='hero_subtitle',
        ),
        migrations.RemoveField(
            model_name='city',
            name='overview_content',
        ),
        migrations.RemoveField(
            model_name='city',
            name='overview_title',
        ),
        migrations.CreateModel(
            name='CityImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cities/')),
                ('title', models.CharField(max_length=200)),
                ('is_main', models.BooleanField(default=False, help_text='Is this the main image for the city?')),
                ('order', models.IntegerField(default=0)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.city')),
            ],
            options={
                'verbose_name_plural': 'City Images',
                'ordering': ['order'],
            },
        ),
    ]
