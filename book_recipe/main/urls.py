from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('recipes', views.breackfast),
    path('lunch', views.lunch),
    path('recipes_launch', views.recipes_launch),
    path('recept1', views.recept1),
    path('registration', views.registration),
    path('signIn', views.signin),
    #path('dinner', views.dinner),
    #path('desert', views.desert),
    #path('favourite', views.favourite)



]