from django.forms import ModelForm
from django import forms
from .models import User
from django.contrib.auth.forms import UserChangeForm

class RegistrationForm(ModelForm):
    class Meta:
        model=User
        fields=("first_name","last_name","password","phone_number","email")
      

class UserEditForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=("first_name","last_name","password","phone_number","email")

