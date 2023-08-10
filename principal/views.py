from django.shortcuts import render


def hola_mundo(request):
    nombre = 'Johan' 
    apellido = 'Villarreal'
    telefono = '3196424443'
    context={
      'nombres':nombre,
      'apellidos': apellido,
      'telefono': telefono
    }
    return render (request, 'index.html', context)