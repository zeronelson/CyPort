from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from users.forms import UserForm
from django.template import loader
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from .models import Profile
from django.contrib.auth.models import User



def users(request):
    return HttpResponse("Welcome to this new app!")

def update_user_data(user):
    Profile.objects.update_or_create(user=user)

def signup(request):
    form = "null"
    if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save(commit=True)
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = User.object.createUser(username, raw_password)
                user.save()
                messages.success(request, ("Successfully added"))
                return HttpResponseRedirect('/') # Redirect to index after form submission 
    form = SignUpForm()
    return render(request, 'signup.html', {"form": form})

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

#def login(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
    form = SignUpForm()
    return render(request, "login.html", {"form": form})
