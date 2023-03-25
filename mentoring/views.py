from django.shortcuts import render
from .models import student



# Create your views here.
def home(request):
    students = student.objects.all()
    context = {'students' : students}
    return render(request, "mentoring/home.html", context)

def find_a_mentor(request):
    return render(request, "mentoring/mentee.html")