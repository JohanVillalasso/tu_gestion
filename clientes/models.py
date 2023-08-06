from django.db import models
from django.utils.translation import gettext_lazy as _
from ciudades.models import Ciudad

 
# PERSONA NATURAL   
class PersonaNatural(models.Model):
  id_documento = models.CharField(max_length=45, verbose_name="Céd Cliente") 
  nombre_uno = models.CharField(max_length=60, verbose_name="Pri Nom Cliente") 
  nombre_dos = models.CharField(max_length=60, verbose_name="Seg Nom cliente") 
  apellido_uno = models.CharField(max_length=60, verbose_name="Pri Ape Cliente") 
  apellido_dos = models.CharField(max_length=60, verbose_name="Seg Ape Cliente") 
  
  def __str__(self):
    return "%s %s %s %s %s" %(self.id_documento, self.nombre_uno, self.nombre_dos, self.apellido_uno, self.apellido_dos)

# PERSONA JURIDICA   
class PersonaJuridica(models.Model):
  nit = models.CharField(max_length=45, verbose_name="NIT") 
  razon_social = models.CharField(max_length=100, verbose_name="Razón Social")  
  
  def __str__(self):
    return "%s %s %s %s" %(self.nit, self.razon_social)  
  
  
# CLIENTE
class Cliente(models.Model):
  movil_cliente = models.CharField(max_length=15, verbose_name="Número celular cliente")
  direccion_cliente = models.CharField(max_length=100, verbose_name="Dirección del cliente")    
  
  class Personeria(models.TextChoices):
    PersonaNatural='Persona Natural', _('Persona Natural')
    PersonaJuridica='Persona Jurídica', _('Persona Jurídica')    
  personeria=models.CharField(max_length=45, choices=Personeria.choices, default=Personeria.PersonaNatural, verbose_name="Personería")   
  
  class TipoCliente(models.TextChoices):
    Remitente='Remitente', _('Remitente')
    Destinatario='Destinatario', _('Destinatario')    
  tipo_cliente=models.CharField(max_length=45, choices=TipoCliente.choices, default=TipoCliente.Remitente, verbose_name="Tipo de cliente")  
 
  class Estado(models.TextChoices):
    ACTIVO = '1', _('Activo')
    INACTIVO = '0', _('Inactivo')
  estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")  
  
  cod_CiudDANE = models.ForeignKey(Ciudad, on_delete=models.CASCADE, related_name='clienteCiudad') 
  id_natural = models.ForeignKey(PersonaNatural, on_delete=models.CASCADE, verbose_name="Id persona natural", related_name='PerNatural')
  id_juridica = models.ForeignKey(PersonaJuridica, on_delete=models.CASCADE, verbose_name="Id persona jurídica", related_name='PerJuridica')
  
  
  def __str__(self):
    return "%s %s %s %s" %(self.movil_cliente, self.direccion_cliente, self.tipo_cliente, self.personeria)  