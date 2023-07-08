from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

def recipes(request):
    return render(request, 'main/recipes.html')

def lanch(request):
    return render(request, 'main/lanch.html')

