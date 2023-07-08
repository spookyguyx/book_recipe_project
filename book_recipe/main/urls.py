from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('recipes', views.recipes),
    path('lanch', views.lanch)

]