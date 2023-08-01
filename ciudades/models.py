from django.db import models
from django.utils.translation import gettext_lazy as _


# DEPARTAMENTOS
class Departamentos(models.Model):
  cod_DeptDANE = models.CharField(max_length=3, verbose_name="Código Departamento")
  nombre_departamento = models.CharField(max_length=60, verbose_name="Nombre Departamento")
  # Estado
  class Estado(models.TextChoices):
    ACTIVO = '1', _('Activo')
    INACTIVO = '0', _('Inactivo')
  estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")  
 
 
# CIUDADES 
class Ciudades(models.Model): 
  cod_CiudDANE = models.CharField(max_length=4, verbose_name="Código Ciudad")
  nombre_ciudad = models.CharField(max_length=60, verbose_name="Ciudad")
  cod_DeptDANE = models.ForeignKey(Departamentos, on_delete=models.PROTECT, verbose_name="Código Departamento")
  # Estado
  class Estado(models.TextChoices):
    ACTIVO = '1', _('Activo')
    INACTIVO = '0', _('Inactivo')
  estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")  