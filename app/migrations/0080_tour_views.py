# Generated by Django 5.1.5 on 2025-03-02 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0079_tour_short_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
