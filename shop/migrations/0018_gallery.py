# Generated by Django 3.2.18 on 2023-05-24 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_banerbig'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(upload_to='gallery')),
                ('img2', models.ImageField(upload_to='gallery')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.productlist')),
            ],
            options={
                'verbose_name': 'گالری',
                'verbose_name_plural': 'گالری ها',
            },
        ),
    ]
