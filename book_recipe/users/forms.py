from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SignInForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Адрес электронной почты")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
