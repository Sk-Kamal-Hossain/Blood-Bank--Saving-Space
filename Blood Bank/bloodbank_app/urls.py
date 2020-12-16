# This urls created by sk kamal

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('login/', views.loginView, name='login'),
    path('register', views.registerView, name='register'),
    path('requestsend', views.requestsendView, name='requestsend'),
    path('al/homepage', views.homepageView, name='homepage'),
    path('al/profile', views.profileView, name='profile'),
]