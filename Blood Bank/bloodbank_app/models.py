from django.db import models

# Create your models here.

class Bloodbank(models.Model):
    location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Distance from {self.location} to {self.destination} is {self.distance} km"


class Register(models.Model):
    name = models.CharField(max_length=150)
    #gender = models.CharField(max_length=200)
    #age = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    #phone = models.CharField(max_length=15)
    #bloodgroup = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    passwordr = models.CharField(max_length=20)

    def __str__(self):
        return self.name
