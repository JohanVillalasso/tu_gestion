from django.db import models
from django.utils.translation import gettext_lazy as _


# DEPARTAMENTOS
class Departamento(models.Model):
  cod_DeptDANE = models.CharField(max_length=3, verbose_name="CódDepartamento")
  nombre_departamento = models.CharField(max_length=60, verbose_name="NomDepartamento")
  # Estado
  class Estado(models.TextChoices):
    ACTIVO = '1', _('Activo')
    INACTIVO = '0', _('Inactivo')
  estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")  
 
 
# CIUDADES - En singular
class Ciudad(models.Model): 
  cod_CiudDANE = models.CharField(max_length=4, verbose_name="CódCiudad")
  nombre_ciudad = models.CharField(max_length=60, verbose_name="Ciudad")  
  
  cod_DeptDANE = models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name="CódDepartamento", related_name='ciudadDpto')
  
  # Estado  
  class Estado(models.TextChoices):
    ACTIVO = '1', _('Activo')
    INACTIVO = '0', _('Inactivo')
  estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")