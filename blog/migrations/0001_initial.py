# Generated by Django 3.2.18 on 2023-04-23 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=25)),
                ('subtitle', models.TextField()),
                ('band1', models.TextField()),
                ('band2', models.TextField()),
                ('img', models.ImageField(upload_to='blog')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('is_active', models.BooleanField()),
                ('author', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقاله ها',
            },
        ),
    ]
