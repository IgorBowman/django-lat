from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView
from django.urls import path

from .views import *

urlpatterns = [
    path('app/<int:pk>/', CountryRegionView.as_view(), name='show_cat'),
    path('add/', CountryCreateView.as_view(), name='create'), # does not work
    # path('add/', add_and_save, name='create'), # does not work
    path('', CountrylistView.as_view(), name='home'),
    path('<int:pk>/', CountryDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', CountryEditView.as_view(), name='edit'),
    path('delete/<int:pk>/', CountryDeleteView.as_view(), name='delete'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),

    path('accounts/password_change/', PasswordChangeView.as_view(
        template_name='registration/change_password.html'),
         name='password_change'),
    path('accounts/password_change/done/', PasswordChangeDoneView.as_view(
        template_name='registration/password_changed.html'),
         name='password_change_done'),
    path('accounts/password_reset/', PasswordResetView.as_view(
        template_name='registration/reset_password.html',
        subject_template_name='registration/reset_subject.txt',
        email_template_name='registration/reset_email.txt'),
         name='password_reset'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
