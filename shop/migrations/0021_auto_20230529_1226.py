# Generated by Django 3.2.18 on 2023-05-29 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_productbrand'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlist',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.productbrand', verbose_name='برند محصول'),
        ),
        migrations.AlterField(
            model_name='productbrand',
            name='url_tital',
            field=models.SlugField(max_length=300, verbose_name='عنوان در url'),
        ),
    ]
