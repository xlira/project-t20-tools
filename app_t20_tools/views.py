from django.shortcuts import render

def home(request):
    return render(request, "menu/home.html")

def classe(request):
    return render(request, "menu/classe.html")