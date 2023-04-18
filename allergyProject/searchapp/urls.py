from django.urls import path
from . import views as searchviews

app_name = 'searchapp'

urlpatterns = [
    path('search/', searchviews.searchResult, name='searchResult'),
    path('detail/', searchviews.Detail, name='Detail')
]

