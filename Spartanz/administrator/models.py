from django.db import models


# Create your models here.
class Enquirys(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    message = models.TextField()
    joining_date = models.DateField()
    When = models.DateTimeField(auto_now_add=True)