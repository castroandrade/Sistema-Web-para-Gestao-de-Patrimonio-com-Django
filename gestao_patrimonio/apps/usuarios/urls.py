from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.utils.http import urlsafe_base64_decode

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]