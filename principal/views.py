from django.shortcuts import render

def hola_mundo(request):
    nombre = "Johan Esteban"
    apellido = "Villarreal Lasso"
    telefono = "123456789"
    context={
        'nombres' :nombre,
        'apellidos' :apellido,
        'telefono' :telefono
    }
    return render (request, 'index.html', context)