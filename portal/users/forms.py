#from django import forms
#from .models import User

#class UserForm(forms.ModelForm):
#    class Meta:
#        model = User
#        fields = ('email', 'password', 'repassword')
#        labels = {
#            "repassword": ("Repeat password"),
#        }

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )