from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    path('', views.Home, name="home"),
    path('clients/', views.Clients, name="clients"),
]