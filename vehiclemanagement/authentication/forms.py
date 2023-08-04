from django import forms
from .models import CustUser
from django.contrib.auth.forms import UserCreationForm



class LogForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)

class RegForm(UserCreationForm):
    class Meta:
        model=CustUser
        fields=["user_type","username","password1","password2"]