from django.contrib.sitemaps import Sitemap
from .models import Country


class CountrySitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.9

    def items(self):
        return Country.objects.all()

    # def lastmod(self, obj):
    #     return obj.pub_date
