from django.urls import path
from . import views


urlpatterns = [
    path('signin/', views.sign_in, name='signin'),
    path('logout/', views.sign_out, name='logout'),
    path('signup/', views.sign_up, name='signup'),
    path('profile', views.profile),
    path('profile1', views.profile1),
]
