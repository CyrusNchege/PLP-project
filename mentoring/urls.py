from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('mentee/', views.find_a_mentor, name = "mentee"),

]
