from django.contrib import admin
from django.urls import path, include
from principal.views import hola_mundo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hola_mundo, name='inicio'),
    path('usuarios/',include('usuarios.urls')),
    path('ciudades/',include('ciudades.urls')),
    path('clientes/',include('clientes.urls')),
    path('guia/',include('guia.urls')),
]
