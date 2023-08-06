from django.shortcuts import render


def hola_mundo(request):
    nombre = 'Johan' 
    apellido = 'Villarreal'
    context={
      'nombres':nombre,
      'apellidos': apellido
    }
    return render (request, 'index.html', context)