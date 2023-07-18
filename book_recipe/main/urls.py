from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('breakfast', views.breakfast),
    path('lunch', views.lunch),
    path('recipes_launch', views.recipes_launch),
    path('recept1', views.recept1),
    # path('registration', views.registration),
    # path('signin', views.signin),
    path('dinner', views.dinner),
    path('dessert', views.dessert),
    path('drink', views.drink),
    path('favorites', views.favorites),
    path('breakfast/<int:pk>', views.RecipeId.as_view(), name='recipe_detail'),
    path('breakfast/<int:pk>', views.RecipeId.as_view(), name='add_post')


]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)