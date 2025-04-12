# Generated by Django 5.1.4 on 2025-02-01 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0062_foodsection_homeslider_museumsection_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodsection',
            name='home_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='app.homepage'),
        ),
        migrations.AddField(
            model_name='museumsection',
            name='home_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='museums', to='app.homepage'),
        ),
        migrations.AddField(
            model_name='thingstodosection',
            name='home_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='things_to_do', to='app.homepage'),
        ),
    ]
