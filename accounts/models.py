from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_mentee = models.BooleanField('is mentee', default=False)
    is_mentor = models.BooleanField('is mentor', default=False)



class Mentee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, )
    career_goal = models.CharField(max_length=255)
    
    def __str__(self):
    	return self.user.username


class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    career_goal = models.CharField(max_length=255)

    def __str__(self):
    	return self.user.username