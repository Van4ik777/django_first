# Generated by Django 5.0.4 on 2024-05-04 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_review_stars'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='reply_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='main.review'),
        ),
    ]
