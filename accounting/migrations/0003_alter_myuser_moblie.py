# Generated by Django 3.2.18 on 2023-04-05 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_auto_20230405_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='moblie',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
