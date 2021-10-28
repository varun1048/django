from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    shirt_sizes =(
    ('S','SMALL'),
    ('M','Medium'),
    ('L','large'),
    )
    shirt_sizes_instance = models.CharField(max_length=1,choices=shirt_sizes)
    def __str__(self) -> str:
        return f"{first_name}"


class Musician(models.Model):
    musician_name = models.CharField(max_length=15)
    instrument = models.CharField(max_length=20)

class Album(models.Model):
    artist  = models.ForeignKey(Musician,on_delete=models.CASCADE)
    artust_name = models.CharField(max_length=15)
    nums_star = models.IntegerField()
    date = models.DateField
     