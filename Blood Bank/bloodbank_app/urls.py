# This urls created by sk kamal

from django.contrib import admin
from django.urls import path
from . import views

# Django Admin Header Customization

admin.site.header = "Log In Saving Space"
admin.site.site_title = "Welcome to Saving Space Dashboard"
admin.site.index_title = "Welcome To This Portal" 

urlpatterns = [
    path('', views.indexView, name='index'),
    path('login', views.loginView, name='login'),
    path('register', views.registerView, name='register'),
    path('requestsend', views.requestsendView, name='requestsend'),
    path('homepage', views.homepageView, name='homepage'),
    path('profile', views.profileView, name='profile'),
    path('search', views.search_result, name='search'),
]