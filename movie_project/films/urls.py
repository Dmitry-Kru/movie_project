from django.urls import path
from . import views

app_name = 'films'

urlpatterns = [
    path('add/', views.add_film, name='add_film'),
    path('list/', views.films_list, name='films_list'),
    path('', views.films_list, name='home'),
]