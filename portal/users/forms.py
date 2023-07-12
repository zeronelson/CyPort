#from django.forms import ModelForm 
#from django.contrib.auth.models import User
#from . import models

#class UserForm(forms.Form):
#    email = forms.CharField(label='Email', max_length=255, widget= forms.TextInput
#                           (attrs={'placeholder':'Enter email'}))
#    password = forms.CharField(label='Password', max_length=255, widget= forms.TextInput
#                           (attrs={'placeholder':'Enter password'}))
#    repassword = forms.CharField(label='Password', max_length=255, widget= forms.TextInput
#                           (attrs={'placeholder':'Enter password again'}))
#class Meta:
#    model = User


#class UserForm(ModelForm):
#    class Meta:
#        model = models.User


from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'repassword')
        labels = {
            "repassword": ("Repeat password"),
        }
        