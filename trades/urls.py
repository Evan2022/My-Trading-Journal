from django.urls import path 

from . import views

app_name = 'trades'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('journals/', views.JournalListView.as_view(), name='journals'),
    path('journals/add/', views.JournalCreateView.as_view(), name='add_journal'),
    path('journals/<int:pk>', views.TradeView.as_view(), name='trade_view')

]

