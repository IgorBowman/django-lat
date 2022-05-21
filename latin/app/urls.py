from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('app/<int:pk>/', show_category, name='show_cat'),
    # path('app/<int:pk>/', show_category2, name='show_cat'),
    path('add/', CountryCreateView.as_view(), name='create'),
    path('', index, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
