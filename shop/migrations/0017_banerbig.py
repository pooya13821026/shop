# Generated by Django 3.2.18 on 2023-05-14 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_alter_baner_url_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='BanerBIg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='baner')),
                ('url_img', models.URLField(max_length=100)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'بنر بزرگ',
                'verbose_name_plural': 'بنر بزرگ ها',
            },
        ),
    ]