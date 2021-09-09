from django.urls import path
from . import views

urlpatterns = [
    path('',views.hola, name = 'hola'),
    path('vader/',views.vader, name = 'vader'),
    path('starwars',views.starWars,name = 'starwars')
]