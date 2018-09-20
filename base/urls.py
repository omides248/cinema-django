from django.contrib import admin
from django.urls import re_path
from .views import IndexView, MovieDetailView

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),
    re_path(r'^movie-detail/$', MovieDetailView.as_view(), name='movie-detail')
]