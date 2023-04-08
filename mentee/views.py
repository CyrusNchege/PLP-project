from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


# @login_required(login_url='login')
def mentee(request):
    
    return render(request, "mentee/mentee.html")

# def mentee(request):
#     mentees = Mentee.objects.all()
#     context = {'mentees' : mentees}
#     return render(request, "mentoring/mentee.html", context)