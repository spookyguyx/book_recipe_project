from typing import Any
from django.forms import BaseModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import RecipeForm, CommentForm
from .models import Recipe, Comment


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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            # messages.success(request, _('Спасибо за отзыв!'))
        else:
            print("спс")
            # messages.error(request, _('Пожалуйста войдите в аккаунт'))
    else:
        form = CommentForm()
    return render(request, 'main/Recept1.html', {'form': form})


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
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        kwargs["form"] = CommentForm()
        kwargs["comments"] = Comment.objects.all()
        return super().get_context_data(**kwargs)
    
    def post(self, request, pk):
        form = CommentForm(request.POST)
        recipe = get_object_or_404(Recipe, pk=pk)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.recipe = recipe
            obj.author = self.request.user
            obj.save()
            return redirect(f"{recipe.category}_detail", pk)
        
        return reverse_lazy(f"{recipe.category}_detail", pk)
    

def recipe_id(request, pk):
    recipe_model = Recipe
    comment_model = Comment
    comment_form = CommentForm
    template = 'main/recipe_id.html'
    context = {}

    if request.method == "GET":
        context["Recipe"] = get_object_or_404(recipe_model, pk=pk)
        context["comments"] = comment_model.objects.filter(recipe_id__id=pk)
        context["form"] = comment_form()
        return render(request, template, context)
    
    if request.method == "POST":
        form = comment_form(request.POST)
        recipe = get_object_or_404(recipe_model, pk=pk)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.recipe = recipe
            obj.author = request.user
            obj.save()
            return redirect(f"{recipe.category}_detail", pk)
    
    return HttpResponse("Не правильно")



    

def profile1(request):
    if request.method == 'GET':
        recipe = Recipe.objects.filter(user=request.user).order_by('-title')
        data = {
            'recipe': recipe,
        }
        return render(request, 'main/profile1.html', data)

