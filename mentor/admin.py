from django.contrib import admin
from .models import Mentor

# Register your models here.
@admin.register(Mentor) 
class  postAdmin(admin.ModelAdmin):
    list_display = ['name']