from django.contrib import admin
from order.models import Order, OrderDetail


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'payment_date', 'is_order_paid']


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['product', 'count']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
