from django.urls import path
from guia.views import guia

urlpatterns = [
    path('',guia, name="Guía"),
]