from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hola(request):
    return HttpResponse('Hola Mundo!!!')

def vader(request):
    return HttpResponse('Hola DartVader!!!')

def starWars(request):
    return HttpResponse('Hola StarWars!!!')