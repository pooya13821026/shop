# Generated by Django 3.2.18 on 2023-04-05 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'verbose_name': 'کاربر', 'verbose_name_plural': 'کاربران'},
        ),
        migrations.AddField(
            model_name='myuser',
            name='moblie',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True),
        ),
    ]