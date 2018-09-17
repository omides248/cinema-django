from django.shortcuts import render
from django.views import View
from .forms import MessageForm


class LoginView(View):
    template_name = 'login_register/login_register.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': MessageForm()})
