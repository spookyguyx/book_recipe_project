from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import SignInForm, SignUpForm
from main.models import Recipe


def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        form = SignInForm()
        context = {
            'form': form,
        }
        return render(request, 'users/signin.html', context)

    elif request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            pword = form.cleaned_data['password']
            user = authenticate(request, username=uname, password=pword)
            if user:
                login(request, user)
                messages.success(request, 'Вход был произведён успешно')
                return redirect('/')
        else:
            messages.error(request, f'Имя или пароль были введены неправильно')
        context = {
            'form': form
        }
    return render(request, 'users/signin.html', context)


def sign_out(request):
    logout(request)
    messages.success(request, f'Вы вышли из учётной записи')
    return redirect('/')


def sign_up(request):
    if request.method == 'GET':
        form = SignUpForm()
        context = {
            'form': form
        }
        return render(request, 'users/registration.html', context)

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Регистрация прошла успешно')
            login(request, user)
            return redirect('/')
        else:
            context = {
                'form': form
            }
            return render(request, 'users/registration.html', context)


def profile1(request):
    if request.method == 'GET':
        recipe = Recipe.objects.filter(user=request.user).order_by('-title')
        data = {
            'recipe': recipe,
        }
        return render(request, 'users/profile1.html', data)


def profile(request):
    user = request.user
    return render(request, 'users/profile.html', {'user': user})


