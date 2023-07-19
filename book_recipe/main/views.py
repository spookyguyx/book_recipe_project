from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import RecipeForm
from .models import Recipe
from django.views.generic import DetailView


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


def favorites(request):
    return render(request, 'main/favorites.html')

'''
def add_to_favorites(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.is_favorite = True
    recipe.save()
    return redirect('recipe_detail', recipe_id=recipe_id)


def remove_from_favorites(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.is_favorite = False
    recipe.save()
    return redirect('recipe_detail', recipe_id=recipe_id)#}
'''


def toggle_favorite(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    user = request.user

    if user in recipe.users_favorite.all():
        recipe.users_favorite.remove(user)  # Удалить статью из избранного
    else:
        recipe.users_favorite.add(user)  # Добавить статью в избранное

    return redirect('recipe_detail', pk=recipe_id)


def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})


class RecipeId(DetailView):
    model = Recipe
    template_name = 'main/recipe_id.html'
    context_object_name = 'Recipe'
