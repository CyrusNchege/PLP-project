from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    is_mentee = models.BooleanField('is mentee', default=False)
    is_mentor = models.BooleanField('is mentor', default=False)



# class Mentee(User):
#     career_goal = models.CharField(max_length=255)

# class Mentor(User):
#     career_goal = models.CharField(max_length=255)