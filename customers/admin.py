from django.contrib import admin
from customers.models import Order
from .models import User


admin.site.register(User)
admin.site.register(Order)
