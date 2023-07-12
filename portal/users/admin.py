from django.contrib import admin
from .models import User

@admin.register(User)
class Register(admin.ModelAdmin):
    list_display = ['email', 'password']
    

# Register your models here.


