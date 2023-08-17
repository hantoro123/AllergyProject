from django.urls import path
from .views import UserLoginView, SignupView ,MypageView

app_name = 'signapp'

urlpatterns = [
    path('login/', UserLoginView.as_view() , name='login'),
    path('signup/', SignupView.as_view() , name='signup'), # 회원 가입 URL 패턴
    path('mypage/', MypageView.as_view() , name='mypage'),
]
