from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class Register(admin.ModelAdmin):
    list_display = [field.name for field in
Profile._meta.get_fields()]
    


