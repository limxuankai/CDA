from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('dashboard/<str:user>/', views.dashboard, name = "dashboard")
]