# Generated by Django 3.2.18 on 2023-04-08 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlist',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
        migrations.AddField(
            model_name='productlist',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
    ]
