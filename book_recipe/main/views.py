from django.shortcuts import render
from django.http import HttpResponse
from .forms import RecipeForm
def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

def recipes(request):
    return render(request, 'main/recipes.html')

def lanch(request):
    return render(request, 'main/lanch.html')

def recipes_launch(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма заполнена неверно'

    form = RecipeForm()

    data = {
        'form': form,
    }

    return render(request, 'main/recipes_launch.html', data)

