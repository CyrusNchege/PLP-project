from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "mentoring/home.html")

def find_a_mentor(request):
    return render(request, "mentoring/mentee.html")