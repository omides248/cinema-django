from django.contrib import admin
from django.urls import re_path
from .views import RegisterView, LoginView

urlpatterns = [
    re_path(r'^login-register/$', RegisterView.as_view(), name='login_register'),
    re_path(r'^login_register/$', LoginView.as_view(), name='login_register'),
]
