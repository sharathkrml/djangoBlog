from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User  #model tht will be affected
        fields = ['username','email','password1','password2'] #fields we need in form and the order