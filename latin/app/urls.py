from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    # path('category/<int:pk>/', show_category, name='show_cat'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
