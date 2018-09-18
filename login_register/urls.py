from django.contrib import admin
from django.urls import re_path
from .views import RegisterLoginView

urlpatterns = [
    re_path(r'^login-register/$', RegisterLoginView.as_view(), name='login_register'),
]
