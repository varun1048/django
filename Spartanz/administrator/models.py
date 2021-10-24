from django.db import models

# Create your models here.
class Enquirys(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    message = models.TextField()
    joining_date = models.DateField()
    When = models.DateTimeField(auto_now_add=True)

class Member(models.Model):

    name        =models.CharField(max_length=100)
    # number      =models.IntegerField()
    # message     =models.TextField()
    # Gender      =models.TextField()
    # goal        =models.TextField()
    
    image       = models.ImageField(null=True,blank=True)


    expiry_package = models.DateTimeField(auto_now=True) 
    joining_date = models.DateTimeField(auto_now_add=True)

