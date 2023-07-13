from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('breakfast', views.breakfast),
    path('lunch', views.lunch),
    path('recipes_launch', views.recipes_launch),
    path('recept1', views.recept1),
    path('registration', views.registration),
    path('signIn', views.signin),
    path('dinner', views.dinner),
    path('dessert', views.dessert),
    path('drink', views.drink),
    path('favorites', views.favorites),
    path('breakfast/<int:pk>', views.recipe_id.as_view(), name='recipe_detail'),
    path('lunch/<int:pk>', views.recipe_id.as_view(), name = 'recipe_detail'),
    path('dinner/<int:pk>', views.recipe_id.as_view(), name='recipe_detail'),
    path('dessert/<int:pk>', views.recipe_id.as_view(), name='recipe_detail'),
    path('drink/<int:pk>', views.recipe_id.as_view(), name='recipe_detail'),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)