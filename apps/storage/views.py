from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'CarritoLibroMujercitas.html')

def contacto(request):
    return render(request, 'Contacto.html')
