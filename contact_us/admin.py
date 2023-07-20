from django.contrib import admin

from contact_us.models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['subject', 'email', 'create_date']


admin.site.register(ContactUs, ContactUsAdmin)
