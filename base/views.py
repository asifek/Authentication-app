from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.views.generic.list import ListView


# Create your views here.

class LoginViewPage(LoginView):
    template_name = 'base/login.html'
    redirect_authenticated_user = False
    # context_object_name = 'tasks'


class RegisterViewPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterViewPage, self).form_valid(form)


class ProfileViewPage(LoginView):
    template_name = 'base/profile.html'
    redirect_authenticated_user = False


