from django.contrib import admin
from .models import Comment, Genre, Picture, Movie

# Register your models here.
admin.site.register(Comment)
admin.site.register(Genre)
admin.site.register(Picture)
admin.site.register(Movie)