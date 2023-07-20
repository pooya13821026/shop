from django.contrib import admin

from site_setting.models import *


class SiteAdmin(admin.ModelAdmin):
    list_display = ['title', 'main_setting']


class FooterAdmin(admin.ModelAdmin):
    list_display = ['title']


class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'footer_link_tital']


class SliderAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(SiteSetting, SiteAdmin)
admin.site.register(FooterTital, FooterAdmin)
admin.site.register(FooterLink, FooterLinkAdmin)
admin.site.register(Slider, SliderAdmin)
