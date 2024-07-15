from .models import Recipe, Comment
from django import forms


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'steps', 'calories', 'time_cooking', 'category', 'image', 'online']
        widgets = {
            'title': forms.TextInput(attrs={
                "class": 'form-control',
                'placeholder': 'Название блюда'
            }),
            'ingredients': forms.TextInput(attrs={
                "class": 'form-control',
                'placeholder': 'Ингридиенты'
            }),
            'steps': forms.Textarea(attrs={
                "class": 'form-control',
                'placeholder': 'Шаги приготовления'
            }),
            'calories': forms.NumberInput(attrs={
                "class": 'form-control',
                'placeholder': 'Кол-во калорий'
            }),
            'time_cooking': forms.TextInput(attrs={
                "class": 'form-control',
                'placeholder': 'Время приготовления'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'stars')

        labels = {
            'text': 'Ваш комментарий'
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
