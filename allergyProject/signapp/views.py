from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from signapp.models import User
# Create your views here.

class LoginView (TemplateView):
    template_name = 'signapp/login.html'

class SignupView (CreateView):
    model = User
    fields = "__all__"
    success_url = reverse_lazy("mainapp:home")

class MypageView (TemplateView):
    template_name = 'signapp/mypage.html'