from django.contrib import admin
from customers.models import Order
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Order)
