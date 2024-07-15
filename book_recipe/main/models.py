import uuid

from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model



CATEGORY_CHOICES = (
    ('breakfast', 'BREAKFAST'),
    ('lunch', 'LUNCH'),
    ('dinner', 'DINNER'),
    ('dessert', 'DESSERT'),
    ('drink', 'DRINK'),
)

STARS_CHOISES = (
    ('1', "ONE"),
    ('2', "TWO"),
    ('3', "THREE"),
    ('4', "FOUR"),
    ('5', "FIVE"),
)


class Recipe(models.Model):
    title = models.CharField('Название блюда', max_length=50)
    image = models.ImageField(upload_to='image/')
    ingredients = models.CharField('Ингредиенты', max_length=300)
    calories = models.IntegerField()
    steps = models.TextField('Шаги приготовления')
    time_cooking = models.CharField('Время приготовления', max_length=30)
    rating = models.IntegerField(default=0)
    category = models.CharField(max_length=9, choices=CATEGORY_CHOICES, default='breakfast')
    online = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite = models.ManyToManyField(User, related_name='favorite', blank=True)

    def __str__(self):
        return f'{self.user.username}: {self.category} - "{self.title}"'

    def get_absolute_url(self):
        return f'/{self.category}/{self.id}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)



class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    stars = models.CharField(max_length=8, choices=STARS_CHOISES, default=STARS_CHOISES[0])

    class Meta:
        ordering = ['-time']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.text
