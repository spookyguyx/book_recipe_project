from django.shortcuts import render
from django.http import HttpResponse
from .forms import RecipeForm
from .models import Recipe


def index(request):
    return render(request, 'main/index.html')


def recipes(request):
    return render(request, 'main/recipes.html')


def breakfast(request):
    return render(request, 'main/breakfast.html')


def lunch(request):
    recipe = Recipe.objects.order_by('-title')

    return render(request, 'main/obedy.html', {'recipe': recipe})


def recipes_launch(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            pass

    form = RecipeForm()

    data = {
        'form': form,

    }

    return render(request, 'main/recipes_launch.html', data)


def recept1(request):
    return render(request, 'main/Recept1.html')


def registration(request):
    return render(request, 'main/registration.html')


def signin(request):
    return render(request, 'main/signIn.html')


def dinner(request):
    return render(request, 'main/dinner.html')


def dessert(request):
    return render(request, 'main/dessert.html')


def drink(request):
    return render(request, 'main/drink.html')


def favorites(request):
    return render(request, 'main/favorites.html')
