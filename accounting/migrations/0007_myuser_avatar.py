# Generated by Django 3.2.18 on 2023-04-30 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0006_alter_myuser_moblie'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar'),
        ),
    ]