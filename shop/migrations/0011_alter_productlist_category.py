# Generated by Django 3.2.18 on 2023-04-15 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20230415_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlist',
            name='category',
            field=models.ManyToManyField(related_name='children', to='shop.ProductCategory'),
        ),
    ]
