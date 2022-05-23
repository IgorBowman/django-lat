from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('app/<int:pk>/', CountryRegionView.as_view(), name='show_cat'),
    #path('add/', CountryCreateView.as_view(), name='create'), # does not work
    path('add/', add_and_save, name='create'), # does not work
    path('', index, name='home'),
    #path('detail/<int:pk>/', CountryDetailView.as_view(), name='detail'),
    path('<int:pk>/', CountryDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', CountryEditView.as_view(), name='edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
