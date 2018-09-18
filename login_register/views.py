from django.shortcuts import render
from django.views import View
from .forms import RegisterForm, LoginForm


class RegisterLoginView(View):
    template_name = 'login_register/login_register.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'register_form': RegisterForm(), 'login_form': LoginForm()})
