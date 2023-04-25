from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserCreation

from django.contrib import messages

 


def loginpage(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None and user.is_active:
                login(request, user)
                if user.is_mentee:
                    return redirect('mentee')
                elif user.is_mentor:
                    return redirect('mentor')
            elif user is None:
                messages.error(request, 'Invalid login credentials.')
            else:
                messages.error(request, 'Your account is not active.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreation()
    return render(request, 'accounts/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

