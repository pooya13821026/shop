from django.contrib.sitemaps import Sitemap
from .models import Blog


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1

    def items(self):
        return Blog.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.create_time
