from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Register
#from django.http import HttpResponse

# Create your views here.

def indexView(request):
    return render(request, 'index.html')

def loginView(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']

        user = auth.authenticate(username=name, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect("homepage")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def registerView(request):
    if request.method == 'POST':
        name = request.POST['name']
        #gender = request.POST['gender']
        #age = request.POST['age']
        email = request.POST['email']
        #phone = request.POST['phone']
        #bloodgroup = request.POST['bloodgroup']
        password = request.POST['password']
        passwordr = request.POST['passwordr']

        if password==passwordr:
            if User.objects.filter(username=name).exists():
                messages.info(request, 'Username Taken')
                return redirect('homepage')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('homepage')
            else:
                user = User.objects.create_user(username=name, email=email, password=passwordr)
                user.save()
                print('user created')
    
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
            #return redirect('/')

    else:
        return render(request, 'register.html')

def requestsendView(request):
	return render(request, 'requestsend.html')

def homepageView(request):
    return render(request, 'homepage.html')
    
def profileView(request):
    return render(request, 'profile.html')

def viewdonationView(request):
    return render(request, 'viewdonation.html')

def viewrequestView(request):
    return render(request, 'viewrequest.html')
