from django.shortcuts import render
from .models import Mentee



# Create your views here.
def home(request):
    
    return render(request, "mentoring/home.html")

def mentee(request):
    mentees = Mentee.objects.all()
    context = {'mentees' : mentees}
    return render(request, "mentoring/mentee.html", context)