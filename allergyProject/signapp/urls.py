from django.urls import path
from .views import UserLoginView, SignupView ,MypageView

app_name = 'signapp'

urlpatterns = [
    path('login/', UserLoginView.as_view() , name='login'),
    path('signup/', SignupView.as_view() , name='signup'),
    path('mypage/', MypageView.as_view() , name='mypage'),
]
