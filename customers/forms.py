from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserForm(UserCreationForm):
    model = User
    fields = ('phone_number')
    error_css_class = 'error'
