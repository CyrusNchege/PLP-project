from django.shortcuts import render

# Create your views here.
def mentor(request):
    return render(request, "mentor/mentor.html")