from .models import Recipe
from django.forms import ModelForm, TextInput, Textarea, NumberInput


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'steps', 'image', 'calories']

        widgets = {
            'title': TextInput(attrs={
                "class": 'form-control',
                'placeholder': 'Название блюда'
            }),
            'ingredients': TextInput(attrs={
                "class": 'form-control',
                'placeholder': 'Ингридиенты'
            }),
            'steps': Textarea(attrs={
                "class": 'form-control',
                'placeholder': 'Шаги приготовления'
            }),
            'calories': NumberInput(attrs={
                "class": 'form-control',
                'placeholder': 'Кол-во калорий'
            }),
        }