# Generated by Django 3.2.18 on 2023-07-10 18:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0021_auto_20230529_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlist',
            name='dislike',
            field=models.ManyToManyField(blank=True, null=True, related_name='dislikes', to=settings.AUTH_USER_MODEL, verbose_name='دیس لایک'),
        ),
        migrations.AddField(
            model_name='productlist',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='لایک'),
        ),
    ]
