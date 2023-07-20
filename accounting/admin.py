from django.contrib import admin
from .models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_staff', 'is_active']


admin.site.register(MyUser, MyUserAdmin)
