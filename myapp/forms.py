from django import forms
from .models import *

class RegisterForm(forms.ModelForm):

    class Meta:
        model = RegisteredUser
        exclude = [""]
        