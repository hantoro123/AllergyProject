from django.urls import path
from . import views 

app_name = 'searchapp'

urlpatterns = [
    path('', views.searchResult, name='searchResult'),
    path('search_detail/', views.Detail, name='Detail')
]

