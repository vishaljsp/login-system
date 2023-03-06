from django.forms import ModelForm
from django import forms 
from django.contrib.auth import get_user_model 
from django.contrib.auth.forms import UserCreationForm
from .models import *

class Myfirstform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        models=get_user_model()
        # fields=["phone"]

class Loginuser(forms.Form):
    username=forms.CharField(max_length=200)
    password=forms.CharField(max_length=200) 