from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    username = models.CharField(max_length=250, null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    

    def __str__(self):
        return self.name
