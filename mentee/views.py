from django.shortcuts import render
from .models import Mentee

# Create your views here.

def mentee(request):
    
    return render(request, "mentee/mentee.html")

# def mentee(request):
#     mentees = Mentee.objects.all()
#     context = {'mentees' : mentees}
#     return render(request, "mentoring/mentee.html", context)