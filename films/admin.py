from django.contrib import admin
from .models import Film, Genre, Picture, Comment, People

admin.site.register(Film)
admin.site.register(Genre)
admin.site.register(Picture)
admin.site.register(Comment)
admin.site.register(People)