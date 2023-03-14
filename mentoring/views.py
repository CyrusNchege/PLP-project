from django.shortcuts import render
# from http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")