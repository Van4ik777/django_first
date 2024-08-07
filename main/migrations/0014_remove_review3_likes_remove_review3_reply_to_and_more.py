# Generated by Django 5.0.4 on 2024-06-01 09:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_review_pizza_type_alter_review_likes_review2_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review3',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='review3',
            name='reply_to',
        ),
        migrations.RemoveField(
            model_name='review3',
            name='user',
        ),
        migrations.AddField(
            model_name='review',
            name='pizza_type',
            field=models.CharField(default='Pizza1', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_reviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Review2',
        ),
        migrations.DeleteModel(
            name='Review3',
        ),
    ]
