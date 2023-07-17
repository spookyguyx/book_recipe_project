from .models import Recipe, Post
from django.forms import ModelForm, TextInput, Textarea, NumberInput, FileInput


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'steps', 'calories', 'category', 'image', 'time_cooking']
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

            'time_cooking': NumberInput(attrs={
                "class": 'form-control',
                'placeholder': 'Время в минутах'
            }),

        #     'image': FileInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Фото лицевой стороны монеты',
        #         'accept': 'image'
        # }),
        }

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['body']