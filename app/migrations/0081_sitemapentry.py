# Generated by Django 5.1.5 on 2025-03-03 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0080_tour_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteMapEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='my Site map', max_length=200, unique=True)),
                ('content', models.TextField(help_text='Put your site map here:')),
            ],
        ),
    ]
