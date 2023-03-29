from django.db import models


# Create your models here.
class Mentee(models.Model):
    
    menteename = models.CharField(max_length=250)
    menteeage = models.CharField(max_length=100)
    bio = models.TextField(max_length=500, blank=True)
    interests = models.CharField(max_length=200)
    campus = models.CharField(max_length=100)

    def __str__(self):
        return self.menteename

  