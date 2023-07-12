from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from users.forms import UserForm
from django.template import loader
from django.contrib import messages

def users(request):
    return HttpResponse("Welcome to this new app!")

def register(request):
    form = " no data yet"
    if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                #email = form.cleaned_data["email"]
                #password = form.cleaned_data["password"]
                #repassword = form.cleaned_data['repassword']
                answers = form.save(commit=False)
                answers.save()
                messages.success(request, ("Successfully added"))
                return HttpResponseRedirect('/') # Redirect to index after form submission 
    form = UserForm()
    return render(request, 'signup.html', {"form": form})

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def login(request):
    #template = loader.get_template('login.html')
    #return HttpResponse(template.render())
    form = " no data yet"
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    form = UserForm()
    return render(request, "login.html", {"form": form})
