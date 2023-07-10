from django import forms
from users.models import User

class UserForm(forms.ModelForm):
    email = forms.CharField(label="email", required=True)

class PickForm(forms):
    class Meta:
        model=UserForm
