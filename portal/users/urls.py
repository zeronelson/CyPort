# Specific file for the users application 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('users/', views.users, name = 'users'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name ='login')
]