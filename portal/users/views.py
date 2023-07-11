from django.shortcuts import render
from django.http import HttpResponse
from users.forms import UserForm
from django.template import loader

def users(request):
    return HttpResponse("Welcome to this new app!")

def register(request):
    #template = loader.get_template('register.html')
    #return HttpResponse(template.render())
    form = " no email yet"
    if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                repassword = form.cleaned_data['repassword']
                #form.save()
            else: 
                form = UserForm()
    form = UserForm(request.GET)
    form
    return render(request, 'register.html', {"form": form})

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


