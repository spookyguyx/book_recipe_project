from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('favorites/', views.user_favorite, name='user_favorite'),
    path('recipes_launch', views.recipes_launch),
    path('recept1', views.recept1),
    path('profile1', views.profile1),
    path('<int:pk>/edit', views.RecipeEdit.as_view(), name='recipe_edit'),
    # path('recipe/<int:recipe_id>/toggle_favorite/', toggle_favorite, name='toggle_favorite'),
    # path('recipe/<int:recipe_id>/add_to_favorites/', views.add_to_favorites, name='add_to_favorites'),
    # path('recipe/<int:recipe_id>/remove_from_favorites/', views.remove_from_favorites, name='remove_from_favorites'),

    # Recipes listed
    path('breakfast', views.breakfast, name='breakfast'),
    path('lunch', views.lunch, name='lunch'),
    path('dinner', views.dinner, name='dinner'),
    path('dessert', views.dessert, name='dessert'),
    path('drink', views.drink, name='drink'),

    # Recipes detailed
    path('breakfast/<int:pk>', views.RecipeId.as_view(), name='breakfast_detail'),
    path('lunch/<int:pk>', views.RecipeId.as_view(), name='lunch_detail'),
    path('dinner/<int:pk>', views.RecipeId.as_view(), name='dinner_detail'),
    path('dessert/<int:pk>', views.RecipeId.as_view(), name='dessert_detail'),
    path('drink/<int:pk>', views.RecipeId.as_view(), name='drink_detail'),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
