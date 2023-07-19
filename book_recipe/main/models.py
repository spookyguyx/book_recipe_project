from django.db import models
from django.contrib.auth import get_user_model

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
    online = models.BooleanField(default=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.title}'

    def get_absolute_url(self):
        return f'{self.id}'


class Favorite(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    favorite = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.favorite}'
