from django.contrib import admin
from .models import Mentee

# Register your models here.
@admin.register(Mentee) 
class  postAdmin(admin.ModelAdmin):
    list_display = ['name']