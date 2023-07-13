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
    path('favorites', views.favorites)

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)