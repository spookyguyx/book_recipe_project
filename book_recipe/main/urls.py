from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('recipes_launch', views.recipes_launch),
    path('recept1', views.recept1),
    path('favorites', views.favorites),

    # vv ListView vv
    path('breakfast', views.breakfast, name="breakfast_list"),
    path('lunch', views.lunch, name="lunch_list"),
    path('dinner', views.dinner, name="dinner_list"),
    path('dessert', views.dessert, name="dessert_list"),
    path('drink', views.drink, name="drink_list"),

    # vv DetailView vv
    path('breakfast/<int:pk>', views.RecipeDetail.as_view(), name='breakfast_detail'),
    path('lunch/<int:pk>', views.RecipeDetail.as_view(), name='lunch_detail'),
    path('dinner/<int:pk>', views.RecipeDetail.as_view(), name='dinner_detail'),
    path('dessert/<int:pk>', views.RecipeDetail.as_view(), name='dessert_detail'),
    path('drink/<int:pk>', views.RecipeDetail.as_view(), name='drink_detail'),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)