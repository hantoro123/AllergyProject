from django.urls import path
from .views import BoardView, DetailView, BoardCreateView

app_name = 'board'

urlpatterns = [
    path('', BoardView.as_view(), name='board_list'),
    path('board_create/', BoardCreateView.as_view(), name='board_create'),
    path('board_detail/<int:pk>', DetailView.as_view(), name='board_detail'),
]

