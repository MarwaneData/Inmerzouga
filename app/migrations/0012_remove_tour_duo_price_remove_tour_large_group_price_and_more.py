# Generated by Django 5.1.4 on 2025-01-18 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_tourprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='duo_price',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='large_group_price',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='small_group_price',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='solo_price',
        ),
    ]
