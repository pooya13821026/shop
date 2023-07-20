from django.contrib import admin
from shop.models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'is_delete']
    list_editable = ['is_active', 'is_delete']
    prepopulated_fields = {'slug': ('title',)}


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'is_active', 'is_delete']


class SeenProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'viewer_ip', 'user']


class PorductComentAdmin(admin.ModelAdmin):
    list_display = ['product', 'create_date', 'user']


class PorductGalleryAdmin(admin.ModelAdmin):
    list_display = ['product']


admin.site.register(ProductList, ProductAdmin)
admin.site.register(SeenProduct, )
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductComment, PorductComentAdmin)
admin.site.register(Baner)
admin.site.register(BanerBIg)
admin.site.register(ProductBrand)
admin.site.register(Discount)
admin.site.register(Gallery, PorductGalleryAdmin)
