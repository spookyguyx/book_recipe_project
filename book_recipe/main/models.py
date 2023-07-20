from django.db import models

from django.contrib.auth.models import User
from django.shortcuts import reverse

CATEGORY_CHOICES = (
    ('breakfast', 'BREAKFAST'),
    ('lunch', 'LUNCH'),
    ('dinner', 'DINNER'),
    ('dessert', 'DESSERT'),
    ('drink', 'DRINK'),
)


class Recipe(models.Model):
    title = models.CharField('Название блюда', max_length=50)
    image = models.ImageField(upload_to='image/')
    ingredients = models.CharField('Ингредиенты', max_length=300)
    calories = models.IntegerField()
    steps = models.TextField('Шаги приготовления')
    time_cooking = models.IntegerField(default=0)
    comments = models.TextField('Комментарии')
    rating = models.IntegerField(default=0)
    category = models.CharField(max_length=9, choices=CATEGORY_CHOICES, default='breakfast')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('breakfast_detail', args=[str(self.pk)])


# Комментарии, но для слабых
class Reviews(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='review')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=160, null=True)
    time = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.recipe.title}-{str(self.user.username)}"
