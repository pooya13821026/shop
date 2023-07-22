from django.contrib.sitemaps import Sitemap
from .models import ProductList


class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1

    def items(self):
        return ProductList.objects.filter(is_active=True, is_delete=False)

    def lastmod(self, obj):
        return obj.create_date
