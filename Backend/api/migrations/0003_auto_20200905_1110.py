# Generated by Django 3.0.3 on 2020-09-05 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200905_1109'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='rating',
            index=models.Index(fields=['stars'], name='api_rating_stars_6ff394_idx'),
        ),
    ]
