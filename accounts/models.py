from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
# Create your models here.

class CustomUser(AbstractUser):
    is_mentee = models.BooleanField(default=False)
    is_mentor = models.BooleanField(default=False)
    def __str__(self):
        return self.username
    
    #to prevent user for being is_mentee and is_mentor at the same time
    def save(self, *args, **kwargs):
        if self.is_mentee and self.is_mentor:
            raise ValidationError("User can't be both mentee and mentor")
        super().save(*args, **kwargs)
