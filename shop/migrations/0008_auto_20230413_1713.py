# Generated by Django 3.2.18 on 2023-04-13 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_mainctegory_mainparent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainctegory',
            name='mainparent',
        ),
        migrations.AddField(
            model_name='productlist',
            name='mainparent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.mainctegory'),
        ),
    ]
