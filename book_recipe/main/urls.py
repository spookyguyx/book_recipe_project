from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('recipes', views.breackfast),
    path('lanch', views.lanch),
   # path('recipes_launch', views.recipes_launch)
]