from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.utils.http import urlsafe_base64_decode

app_name = "usuarios"

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path("registro/", views.registro, name="registro"),
    path('logout/', views.logout_view, name='logout'),
]