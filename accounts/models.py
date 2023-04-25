from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    is_mentee = models.BooleanField(default=False)
    is_mentor = models.BooleanField(default=False)
    def __str__(self):
        return self.username
    

class Mentee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return self.user.username

class Mentor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return self.user.username