from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .forms import RecipeForm, ReviewForm
from .models import Recipe, Reviews
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.contrib import messages


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


class RecipeDetail(DetailView, FormMixin):
    model = Recipe
    template_name = 'main/recipe_id.html'
    context_object_name = 'Recipe'
    form_class = ReviewForm

    def get_absolute_url(self):
        return reverse('breakfast_detail', args=[str(self.pk)])

    def get_success_url(self):
        return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super(RecipeDetail, self).get_context_data(**kwargs)
        context["reviews"] = self.object.review.filter(approved=True)
        context["form"] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.recipe = self.object
        form.save()
        return super().form_valid(form)
