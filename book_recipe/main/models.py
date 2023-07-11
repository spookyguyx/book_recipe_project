from django.db import models


class Recipe(models.Model):
    title = models.CharField('Название блюда', max_length=25)
    image = models.ImageField(upload_to='image/')
    ingredients = models.CharField('Ингредиенты', max_length=50)
    calories = models.IntegerField()
    steps = models.TextField('Шаги приготовления')
    time_cooking = models.IntegerField()
    comments = models.TextField('Комментарии')
    rating = models.IntegerField()

    def __str__(self):
        return self.title