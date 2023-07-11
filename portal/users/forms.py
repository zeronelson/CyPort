from django import forms 
from django.contrib.auth.models import User

class UserForm(forms.Form):
    email = forms.CharField(label='Email', max_length=255, widget= forms.TextInput
                           (attrs={'placeholder':'Enter email'}))
    password = forms.CharField(label='Password', max_length=255, widget= forms.TextInput
                           (attrs={'placeholder':'Enter password'}))
    repassword = forms.CharField(label='Password', max_length=255, widget= forms.TextInput
                           (attrs={'placeholder':'Enter password again'}))
    
class Meta:
    model = User