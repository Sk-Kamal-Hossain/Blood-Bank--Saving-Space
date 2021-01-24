from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Measurement(models.Model):
    location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Distance from {self.location} to {self.destination} is {self.distance} km" 


class Register(models.Model):
    name = models.CharField(max_length=150)
    #gender = models.BooleanField(default=False)
    #age = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    #phone = models.CharField(max_length=15)
    #bloodgroup = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    passwordr = models.CharField(max_length=20)

    def __str__(self):
        return self.name

#class Sendrequest(models.Model):
    #name = models.CharField(max_length=150)
    #gender = models.CharField(max_length=200)
    #age = models.CharField(max_length=100)
    #email = models.CharField(max_length=200)
    #phone = models.CharField(max_length=15)
    #bloodgroup = models.CharField(max_length=100)

    #def __str__(self):
    #    return self.name

class Camps(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics/')
    desc = models.TextField()
    dat = models.DateField()

    def __str__(self):
        return self.name


class Donation(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)

    BLOOD_CHOICE =(
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),

    )
    bloodgroup = models.CharField(max_length=100, choices=BLOOD_CHOICE)

    GENDER_CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )

    gender = models.CharField(max_length=100, choices=GENDER_CHOICE)

    def __str__(self):
        return self.name