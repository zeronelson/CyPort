# Specific file for the users application 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.users, name = 'users'),
    path('signup/', views.signup, name='signup'),
    #path('accounts/login/', views.login, name ='login')
]