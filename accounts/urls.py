from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginpage, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('logout/', views.logout_view, name = 'logout'),
    path('password_reset/', views.password_reset, name = 'password_reset'),

]
