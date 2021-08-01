from os import name
from django.db import models

# Create your models here.
class reviewModels(models.Model):
    name = models.CharField(max_length=100)
    review = models.CharField(max_length=500)