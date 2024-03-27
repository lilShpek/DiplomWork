from django.contrib import admin
from .models import *

class RegisteredUserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RegisteredUser._meta.fields]
    list_filter = ['name']
    search_fields = ['name', 'email']


    class Meta:
        model = RegisteredUser


admin.site.register(RegisteredUser, RegisteredUserAdmin)
