# Generated by Django 3.2.18 on 2023-07-06 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0021_auto_20230529_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(blank=True, editable=False, null=True, verbose_name='تاریخ پرداخت')),
                ('is_order_paid', models.BooleanField(editable=False, verbose_name='پرداخت شده')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'سفارش',
                'verbose_name_plural': 'سفارشات',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_price', models.PositiveIntegerField(blank=True, editable=False, null=True, verbose_name='قیمت نهایی محصول')),
                ('count', models.PositiveIntegerField(editable=False, verbose_name='تعداد')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='سفارش')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.productlist', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'جزئیات سفارش',
                'verbose_name_plural': 'جزئیات سفارشات',
            },
        ),
    ]
