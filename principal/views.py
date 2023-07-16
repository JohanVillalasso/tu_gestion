from django.shortcuts import render

def hola_mundo(request):
    nombre = 'Alexander' 
    apellido = 'Corredor'
    context={
      'nombres':nombre,
      'apellidos': apellido
    }
    return render (request, 'index.html', context)