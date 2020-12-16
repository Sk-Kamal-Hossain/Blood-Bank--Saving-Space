from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def indexView(request):
    return render(request, 'index.html')

def loginView(request):
    return render(request, 'login.html')

def registerView(request):
    return render(request, 'register.html')

def requestsendView(request):
	return render(request, 'requestsend.html')

def homepageView(request):
    return render(request, 'login/al/homepage.html')

def profileView(request):
    return render(request, 'al/profile.html')