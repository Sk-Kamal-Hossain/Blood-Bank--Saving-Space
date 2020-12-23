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

    name = request.POST.get('name')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    bloodgroup = request.POST.get('bloodgroup')
    password = request.POST.get('password')
    passwordr = request.POST.get('passwordr')
    all = [name, gender, age, email, phone, bloodgroup, password, passwordr]

    return render(request, 'login/al/homepage.html', {'all':all})

def profileView(request):

    return render(request, 'al/profile.html')