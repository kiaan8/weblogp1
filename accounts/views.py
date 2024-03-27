from django.shortcuts import render, HttpResponse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User


class SignUpView(generic.CreateView):

    form_class = UserCreationForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('login')
    print('hello')

