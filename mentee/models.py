# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class User(AbstractUser):
#     is_mentee = models.BooleanField('is mentee', default=False)
    

# # class Mentee(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mentee')
# #     email = models.EmailField(unique=True)
# #     first_name = models.CharField(max_length=30, blank=True)
# #     last_name = models.CharField(max_length=30, blank=True)
# #     is_active = models.BooleanField(default=True)
# #     bio = models.TextField(blank=True)


# # from django.db import models
# # from django.contrib.auth.models import User
# # from django.contrib.auth.models import AbstractUser


# # # Create your models here.


# # class Mentee(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
# #     is_mentor = models.BooleanField(default=False)
# #     name = models.CharField(max_length=250, null=True, blank=True)
# #     email = models.EmailField(unique=True, null=True, blank=True)
# #     username = models.CharField(max_length=250, null=True, blank=True)
# #     bio = models.TextField(max_length=500, blank=True)
    

# #     def __str__(self):
# #         return self.name

  