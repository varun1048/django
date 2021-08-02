from django.db import models

# Create your models here.
class Music(models.Model):
    song = models.CharField(max_length=200)
    artist=models.CharField(max_length=200)
