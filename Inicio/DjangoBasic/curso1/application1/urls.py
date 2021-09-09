from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('index/',views.hola, name='hola'),
    path('ted/',views.ted, name='ted'),
    # path('<str:nombre>',views.saludo, name='saludo'),
    path('page1/',views.page1, name='page1'),
     path('moneda/',views.moneda, name='moneda'),
     path('add/',views.add, name='add'),
]