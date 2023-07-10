# All views for user app
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from users.models import User
from portal.forms import UserForm

def users(request):
    return HttpResponse("Welcome to this new app!")

def register(request):
    template = loader.get_template('register.html')
    #form = UserForm()
    #return render(request, "register.html", {"form":form})

    return HttpResponse(template.render())