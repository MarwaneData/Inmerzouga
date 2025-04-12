# app/migrations/0008_remove_low_deposit.py

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='deposit',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='deposit_percentage',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='low_deposit_amount',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='low_deposit',  # ✅ suppression propre du champ problématique
        ),
        migrations.AlterField(
            model_name='tour',
            name='activity_description',
            field=models.TextField(help_text='Describe what activities are included'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='activity_level',
            field=models.CharField(
                choices=[
                    ('cultural', 'Cultural & Historical'),
                    ('adventure', 'Adventure & Exploration'),
                    ('relaxation', 'Relaxation & Wellness'),
                    ('photography', 'Photography & Sightseeing'),
                    ('mixed', 'Mixed Activities')
                ],
                help_text='Type of activities included',
                max_length=20
            ),
        ),
    ]
