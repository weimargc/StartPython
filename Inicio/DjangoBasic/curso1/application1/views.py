from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AgregarTarea

# Create your views here.

tareas = []

def home(request):
    context = {'tareas' : tareas}
    return render(request,'application1/home.html',context)

def hola(request):
    return HttpResponse('Hola mundo')

def ted(request):
    return HttpResponse('Hola ted')

# def saludo(request, nombre):
#     return HttpResponse (f'Hola {nombre} !!!!')

def saludo(request, nombre):
    context = {'name':nombre}
    return render (request, 'application1/saludo.html',context)

# Para retornar un template html
def page1(request):
    return render(request,'application1/index.html')

def moneda (request):
    num=1
    context = {'num':num}
    return render(request,'application1/moneda.html',context)

def add(request):
    if request.method == 'POST':
        #Leer lo que hay en loas campos con el objeto request
        form = AgregarTarea(request.POST)
        if form.is_valid():
            #['tarea'] este nombre es la variable en forms.py
            tarea = form.cleaned_data['tarea']
            tareas.append(tarea)
            return redirect('home')
    else:
        form = AgregarTarea()

    context = {'form' : form}
    return render (request, 'application1/add.html',context)

