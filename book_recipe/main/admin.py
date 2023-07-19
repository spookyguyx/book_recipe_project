from django.contrib import admin
from .models import Recipe, Favorite
# Register your models here.

admin.site.register(Recipe)
admin.site.register(Favorite)