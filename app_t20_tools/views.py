from django.shortcuts import render
from .models import racas

def home(request):
    return render(request, "menu/home.html")

def racas(request):
   
    return render(request, "menu/racas.html")