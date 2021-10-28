from django.db import models

# Create your models here.
class Enquirys(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    message = models.TextField()
    joining_date = models.DateField()
    visit_types = (
        ('Call', 'c'),
        ('Directly', 'd'),
    )
    visit_type = models.CharField(max_length=10,blank=True, choices=visit_types)

    timming = models.TimeField(auto_now_add=True)
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

