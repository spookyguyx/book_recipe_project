from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def recipes(request):
    return render(request, 'main/recipes.html')


def breackfast(request):
    return render(request, 'main/breakfast.html')


def lunch(request):
    return render(request, 'main/lunch.html')


def recipes_launch(request):
    return render(request, 'main/recipes_launch.html')


def recept1(request):
    return render(request, 'main/Recept1.html')


def registration(request):
    return render(request, 'main/registration.html')


def signin(request):
    return render(request, 'main/signIn.html')


#def dinner(request):
#    return render(request, 'main/dinner.html')


#def desert(request):
#    return render(request, 'main/desert.html')


#def favourite(request):
#    return render(request, 'main/favourite.html')
