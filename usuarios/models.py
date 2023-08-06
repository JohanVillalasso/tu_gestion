from django.db import models
from django.utils.translation import gettext_lazy as _
from ciudades.models import Ciudad


# USUARIO
class Usuario(models.Model):
  codigo_nomina = models.CharField(max_length=45, verbose_name="Código nómina")
  cedula = models.CharField(max_length=15, verbose_name="Cédula")
  nombre = models.CharField(max_length=60, verbose_name="Nombre")
  nombre_dos = models.CharField(max_length=60, verbose_name="Segundo nombre")
  apellido = models.CharField(max_length=60, verbose_name="Apellido") 
  apellido_dos = models.CharField(max_length=60, verbose_name="Segundo apellido")
  correo = models.CharField(max_length=100, verbose_name="Correo")
  password = models.CharField(max_length=8, verbose_name="Contraseña")  
  
  # Rol
  class Rol(models.TextChoices):
    Administrador='Administrador', _('Administrador')
    Empleado='Empleado', _('Empleado')    
  rol=models.CharField(max_length=13, choices=Rol.choices, default=Rol.Empleado, verbose_name="Rol")  
  
  # Estado
  class Estado(models.TextChoices):
    ACTIVO = '1', _('Activo')
    INACTIVO = '0', _('Inactivo')
  estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
  
  def __str__(self):
    return "%s %s %s %s" %(self.nombre, self.nombre_dos, self.apellido, self.apellido_dos)
  
  
# PUNTO DE VENTA
class PuntoVenta(models.Model):
  nombre = models.CharField(max_length=60, verbose_name="Nombre")
  direccion = models.CharField(max_length=100, verbose_name="Dirección")
  presupuesto = models.DecimalField(max_digits=8, decimal_places=2)
  
  # Estado
  class Estado(models.TextChoices):
    ACTIVO = '1', _('Activo')
    INACTIVO = '0', _('Inactivo')
  estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")    
  
  cod_CiudDANE = models.ForeignKey(Ciudad, on_delete=models.PROTECT, related_name='CiudadPVenta')  
  
  
  def __str__(self):
    return "%s %s" %(self.nombre, self.direccion)






    