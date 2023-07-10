# All views for user app
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def users(request):
    return HttpResponse("Welcome to this new app!")

def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())