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
            user = authenticate (request, 
                                 username = cd['username'], 
                                 password = cd['password'])
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'You have been logged in.')
                    return redirect ('mentee')
                else:
                    messages.error(request, 'Your account is not active.')
            else:
                messages.error(request, 'Invalid login credentials.')
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

# @login_required(login_url='/accounts/login/')
# def mentor_dashboard(request):
#     return render(request, 'accounts/mentor_dashboard.html')

# @login_required(login_url='/accounts/login/')
# def mentee_dashboard(request):
#     return render(request, 'accounts/mentee_dashboard.html')




# if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         try:
#             user = User.objects.get(username=username)
#         except:
#             print('Username does not exist')
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             # return redirect('mentee')
#             if user.is_mentor:
#                 return redirect('mentor')
#             elif user.is_mentee:
#                 return redirect('mentee')
#         else:
#             messages.success(request, 'Invalid username or password')

# def login_view(request):
#     if request.method == 'POST':
#         # handle form submission
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('accounts/login.html')
#         else:
#             # display error message
#             return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})
#     else:
#         # display login form
#         return render(request, 'accounts/login.html')

# def register_view(request):
#     if request.method == 'POST':
#         # handle form submission
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(request, username=username, password=password)
#             login(request, user)
#             return redirect('home')
#         else:
#             # display error message
#             return render(request, 'register.html', {'form': form})
#     else:
#         # display registration form
#         form = UserRegistrationForm()
#         return render(request, 'register.html', {'form': form})
