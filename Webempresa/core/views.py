from django.shortcuts import render

# Create your views here.

def home (request): 
    return render(request, 'core/home.html')

def som (request): 
    return render(request, 'core/som.html')

def història(request): 
    return render(request, 'core/història.html')

def galeria(request): 
    return render(request, 'core/galeria.html')


def amics(request): 
    return render(request, 'core/amics.html')

def export(request): 
    return render(request, 'core/export.html')  

