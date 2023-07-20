from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView

from .forms import RecipeForm
from django.views.generic import DetailView, UpdateView
from .models import Recipe


class RecipeEdit(UpdateView):
    model = Recipe
    template_name = 'main/edit.html'
    form_class = RecipeForm


def index(request):
    return render(request, 'main/index.html')


def recipes(request):
    return render(request, 'main/recipes.html')


def breakfast(request):
    if request.method == 'GET':
        recipe = Recipe.objects.order_by('-title')
        data = {
            'recipe': recipe
        }
        return render(request, 'main/breakfast.html', data)


def lunch(request):
    if request.method == 'GET':
        recipe = Recipe.objects.order_by('-title')
        data = {
            'recipe': recipe
        }
        return render(request, 'main/obedy.html', data)


def recipes_launch(request):
    error = ''
    form = RecipeForm()

    if request.method == "GET":
        form = RecipeForm(request.GET)
        data = {
            'form': form
        }
        return render(request, 'main/recipes_launch.html', data)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('/')
        else:
            error = 'Форма была неверно заполнена'

    data = {
        'form': form,
        'error': error

    }
    return render(request, 'main/recipes_launch.html', data)


def recept1(request):
    return render(request, 'main/Recept1.html')


# Ненужное
#
# def registration(request):
#     return render(request, 'main/registration.html')
#
#
# def signin(request):
#     return render(request, 'main/signin.html')


def dinner(request):
    if request.method == 'GET':
        recipe = Recipe.objects.order_by('-title')
        data = {
            'recipe': recipe
        }
    return render(request, 'main/dinner.html', data)


def dessert(request):
    if request.method == 'GET':
        recipe = Recipe.objects.order_by('-title')
        data = {
            'recipe': recipe
        }
        return render(request, 'main/dessert.html', data)


def drink(request):
    if request.method == 'GET':
        recipe = Recipe.objects.order_by('-title')
        data = {
            'recipe': recipe
        }
        return render(request, 'main/drink.html', data)


def favorite_recipe(request, recipe_id):
    if request.method == "POST":
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        if not recipe.favorite.filter(id=request.user.id).exists():
            recipe.favorite.add(request.user)
            recipe.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            recipe.favorite.remove(request.user)
            recipe.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def user_favorite(request):
    user = request.user
    recipes = Recipe.objects.filter(favorite__in=[user])

    context = {'user': user, "recipes": recipes}
    return render(request, "main/favorites.html", context)


class RecipeId(DetailView):
    model = Recipe
    template_name = 'main/recipe_id.html'
    context_object_name = 'Recipe'


def profile1(request):
    if request.method == 'GET':
        recipe = Recipe.objects.filter(user=request.user).order_by('-title')
        data = {
            'recipe': recipe,
        }
        return render(request, 'main/profile1.html', data)
