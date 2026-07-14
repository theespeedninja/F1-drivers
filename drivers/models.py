from django.db import models
from django.utils import timezone

# Create your models here.
class Driver(models.Model):
    firstname = models.CharField(max_length= 255)
    lastname = models.CharField(max_length = 255)
    F1Team = models.CharField(max_length=100, default="F1")
    Nationality = models.CharField(max_length=100, default="World-Country" )
    Points = models.IntegerField(null=True, default=0)
    lastRace_date=models.DateField(null=True,default=timezone.now)
    