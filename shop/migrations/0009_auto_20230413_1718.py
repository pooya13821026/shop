# Generated by Django 3.2.18 on 2023-04-13 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20230413_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='productlist',
            name='category',
        ),
        migrations.RemoveField(
            model_name='productlist',
            name='mainparent',
        ),
        migrations.AddField(
            model_name='productcategory',
            name='mainparent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.mainctegory'),
        ),
        migrations.AddField(
            model_name='productlist',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.productcategory'),
        ),
    ]