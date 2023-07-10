from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def recipes(request):
    return render(request, 'main/recipes.html')


def breackfast(request):
    return render(request, 'main/breakfast.html')


def lanch(request):
    return render(request, 'main/lanch.html')