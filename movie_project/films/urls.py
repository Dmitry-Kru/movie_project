from django.urls import path
from . import views

app_name = 'films'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_film, name='add_film'),
    path('list/', views.films_list, name='films_list'),
]