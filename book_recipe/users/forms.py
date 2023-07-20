from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import FileInput

from .models import Profile


class SignInForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Адрес электронной почты")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username',
                  'summary', 'about', 'image'
                  ]
        labels = {
            'name': 'Имя и фамилия',
            'email': 'Email',
            'username': 'Логин',
            'summary': 'В двух словах о себе',
            'about': 'Подробнее о себе',
            'image': 'Изменить фото профиля',
        }
        widgets = {
            'image': FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
