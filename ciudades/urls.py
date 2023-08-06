from django.urls import path
from ciudades.views import ciudades

urlpatterns = [
    path('',ciudades, name="Ciudades"),
]