from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from .views import toggle_favorite

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
    path('profile', views.profile, name="profile"),
    path('breakfast/<int:pk>', views.RecipeId.as_view(), name='recipe_detail'),
    path('lunch/<int:pk>', views.RecipeId.as_view(), name = 'recipe_detail1'),
    path('dinner/<int:pk>', views.RecipeId.as_view(), name='recipe_detail2'),
    path('dessert/<int:pk>', views.RecipeId.as_view(), name='recipe_detail3'),
    path('drink/<int:pk>', views.RecipeId.as_view(), name='recipe_detail4'),
    #path('recipe/<int:recipe_id>/toggle_favorite/', toggle_favorite, name='toggle_favorite'),
    #path('recipe/<int:recipe_id>/add_to_favorites/', views.add_to_favorites, name='add_to_favorites'),
    #path('recipe/<int:recipe_id>/remove_from_favorites/', views.remove_from_favorites, name='remove_from_favorites'),
    path('profile/', views.profile, name='profile'),
    path('<int:pk>/edit', views.RecipeEdit.as_view(), name='recipe_edit'),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)