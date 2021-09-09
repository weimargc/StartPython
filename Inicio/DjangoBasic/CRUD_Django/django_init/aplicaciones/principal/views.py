from django.shortcuts import render
from .models import PersonTemp

# Create your views here.
def inicio(request):
    return render(request,'index.htm')