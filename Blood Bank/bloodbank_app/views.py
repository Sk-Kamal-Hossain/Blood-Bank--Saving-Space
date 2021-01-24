from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Register
from django.http import HttpResponse
from .models import Camps
from django.core.mail import send_mail
from .models import Donation

# Create your views here.

def indexView(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        send_mail('Contact From',
        name,email,phone,message,
        settings.EMAIL_HOST_USER,
        ['skkamal6301@gmail.com'],
        fail_silently=False)
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
    return render(request, 'homepage.html')

def requestsendView(request):
	return render(request, 'requestsend.html')

def homepageView(request):
    return render(request, 'homepage.html')
    
def profileView(request):
    return render(request, 'profile.html')

def blooddonateView(request):
    return render(request, 'blooddonate.html')

def viewdonationView(request):
    return render(request, 'viewdonation.html')

def viewrequestView(request):
    return render(request, 'viewrequest.html')

def campsView(request):
    obj = Camps.objects.all().order_by('-dat')
    return render(request, 'camps.html',{'obj':obj})

def bloodbanksView(request):
    return render(request, 'bloodbanks.html')

def contactView(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        messages = request.POST['message']

        # send an email
        #send_mail(
        #    name,
        #    message, 
        #    email,    
        #    ['skkamal6301@gmail.com'],
        #    subject,
        #    )

        return render(request, 'contact.html', {'name': name})

    else:
        return render(request, 'contact.html', {})


def search_result(request):
    user_list = Donation.objects.all().order_by('-age')
    context = {'users': user_list}

    if request.method == 'GET':
        keyword = request.GET.get('bloodgroup')
        search_filter = Donation.objects.filter(bloodgroup=keyword)
        context['results'] = search_filter
        context['keyword'] = keyword

    return render(request, 'search_result.html', context)

