from django.contrib import admin
from .models import Recipe, Post, RatingStar, Favorite
# Register your models here.

admin.site.register(Recipe)
admin.site.register(Post)
admin.site.register(RatingStar)
admin.site.register(Favorite)


