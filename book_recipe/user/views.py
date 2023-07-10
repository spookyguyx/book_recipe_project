from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm


def register_page(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Был создан аккаунт ' + user)
            return redirect('login')
        else:
            messages.info(request, 'Что-то не так')

    context = {'form': form}
    return render(request, 'user/register.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
        else:
            messages.info(request, 'Имя пользователя или пароль введены неправильно')
    context = {}
    return render(request, 'user/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')
