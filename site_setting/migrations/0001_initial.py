# Generated by Django 3.2.18 on 2023-04-16 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='site_logo')),
                ('number1', models.IntegerField(max_length=11)),
                ('number2', models.IntegerField(max_length=11)),
                ('slogan', models.CharField(max_length=50)),
                ('footer_about', models.CharField(max_length=100)),
                ('youtube_url', models.URLField()),
                ('github_url', models.URLField()),
                ('instagram_url', models.URLField()),
                ('linkdin_url', models.URLField()),
                ('twitter_url', models.URLField()),
                ('coptright', models.CharField(max_length=50)),
                ('main_setting', models.BooleanField()),
            ],
            options={
                'verbose_name': 'تنظیمات',
                'verbose_name_plural': 'لیست تنظیمات',
            },
        ),
    ]