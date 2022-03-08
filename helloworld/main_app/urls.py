from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='Home'),
    path('home', views.homeView, name='Home'),
    path('another/', views.anotherView, name="another"),


]