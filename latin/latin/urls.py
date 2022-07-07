from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from app.sitemaps import CountrySitemap

sitemaps = {'countries': CountrySitemap, }

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('', include('app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
