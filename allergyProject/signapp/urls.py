from django.urls import path
from .views import LoginView, SignupView ,MypageView

app_name = 'signapp'

urlpatterns = [
    path('login/', LoginView.as_view() , name='login'),
    path('signup/', SignupView.as_view() , name='signup'),
    path('mypage/', MypageView.as_view() , name='mypage'),
]
