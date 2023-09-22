from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('dashboard/<str:user>/', views.dashboard, name = "dashboard"),
    path('trial', views.trial, name="trial"),
    path('index', views.index, name="trial")
]