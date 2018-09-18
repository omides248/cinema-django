from django.contrib import admin
from django.urls import re_path
from .views import RegisterView

urlpatterns = [
    re_path(r'^login-register/$', RegisterView.as_view(), name='login_register'),
]
