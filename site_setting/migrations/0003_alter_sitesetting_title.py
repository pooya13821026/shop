# Generated by Django 3.2.18 on 2023-04-16 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setting', '0002_sitesetting_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
