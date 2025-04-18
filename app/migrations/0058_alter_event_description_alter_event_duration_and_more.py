# Generated by Django 5.1.4 on 2025-02-01 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0057_alter_event_description_alter_event_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(help_text="e.g., 'Capture the magic of the desert with our professional photography services.'"),
        ),
        migrations.AlterField(
            model_name='event',
            name='duration',
            field=models.CharField(default='Full Day', max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='group_size',
            field=models.CharField(default='Custom Size', max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='price_info',
            field=models.CharField(default='Custom Quote', max_length=50),
        ),
        migrations.AlterField(
            model_name='eventprice',
            name='people',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='eventprice',
            name='price',
            field=models.CharField(max_length=50),
        ),
    ]
