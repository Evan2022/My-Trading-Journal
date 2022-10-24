from django.urls import path 

from . import views

app_name = 'trades'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('journals/', views.JournalsListView.as_view(), name='journals')
]