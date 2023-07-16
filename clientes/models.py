from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Cliente(models.Model):
  
  class Personeria(models.TextChoices):
    NATURAL = '1', _('Natural')
    JURIDICA = '0', _('Jurídica')
  personeria = models.CharField(max_length=1, choices=Personeria.choices, default=Personeria.NATURAL, verbose_name="Tipo de personería")

  class TipoCliente(models.TextChoices):
    REMITENTE = '1', _('Remitente')
    DESTINATARIO = '0', _('Destinatario')
  tipo_cliente = models.CharField(max_length=1, choices=TipoCliente.choices, default=TipoCliente.REMITENTE, verbose_name="Tipos de clientes")
  movil_cliente = models.CharField(max_length=15, verbose_name="Teléfono del cliente")
  direccion_cliente = models.CharField(max_length=100, verbose_name="Dirección del cliente")

  class EstadoCliente(models.TextChoices):
    ACTIVO = '1', _('Activo')
    INACTIVO = '0', _('Inactivo')
  estado_cliente = models.CharField(max_length=1, choices=EstadoCliente.choices, default=EstadoCliente.ACTIVO, verbose_name="Estado del cliente")