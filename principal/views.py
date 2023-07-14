from django.shortcuts import render

def hola_mundo(request):
    context={}
    return render (request, 'index.html', context)