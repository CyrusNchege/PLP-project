from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.loginpage, name = 'login'),
    # path('', auth_views.LoginView.as_view(template_name = "accounts/login.html"), name = 'login'),
    # path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
]
