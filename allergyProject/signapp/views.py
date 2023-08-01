from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView
from signapp.models import User
# Create your views here.

class UserLoginView (LoginView):
    template_name = 'signapp/login.html'
    success_url = reverse_lazy("mainapp:home")

class SignupView (CreateView):
    template_name = 'signapp/signup.html'
    model = User
    fields = "__all__"
    success_url = reverse_lazy("signapp:login")

class MypageView (TemplateView):
    template_name = 'signapp/mypage.html'