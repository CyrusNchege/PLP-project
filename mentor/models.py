from django.db import models


# Create your models here.
class Mentor(models.Model):
    menteename = models.CharField(max_length=250)
    menteeage = models.CharField(max_length=100)