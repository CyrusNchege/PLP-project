from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from mentor.models import Mentor
from mentee.models import Mentee

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            print('Username does not exist')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('mentee')
            # if user.is_mentor:
            #     return redirect('mentor')
            # elif user.is_mentee:
            #     return redirect('mentee')
        else:
            messages.success(request, 'Invalid username or password')
    return render(request, 'accounts/login.html')
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
