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
    path('blooddonate', views.blooddonateView, name='blooddonate'),
    path('requestsend', views.requestsendView, name='requestsend'),
    path('homepage', views.homepageView, name='homepage'),
    path('profile', views.profileView, name='profile'),
    path('viewdonation', views.viewdonationView, name='viewdonation'),
    path('viewrequest', views.viewrequestView, name='viewrequest'),
    path('camps', views.campsView, name='camps'),
    path('bloodbanks', views.bloodbanksView, name='bloodbanks'),
    path('contact', views.contactView, name='contact'),
]