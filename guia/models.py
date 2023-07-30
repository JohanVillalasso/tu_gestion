from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

# Create your models here.
class Cliente(models.Model):
  fecha = models.DateField(verbose_name="Fecha de captura de la guia")
  destinatario = models.CharField(max_length=60, verbose_name="Datos de destinatario")
  movil_destinatario = models.CharField(max_length=45, verbose_name="Número de teléfono de destinatario")
  unidades = models.IntegerField(verbose_name="Cantidad de unidades por despacho")
  

class Recogida(models.TextChoices):
    SI = '1', _('Si')
    NO = '0', _('No')
recogida = models.CharField(max_length=1, choices=Recogida.choices, default=Recogida.NO, verbose_name="El cliente solicitó servicio de recogida?")

class Estado(models.TextChoise):
  hora_guia = models.TimeField(auto_now=True, verbose_name="Hora de captura de la guía")
  fecha_guia = models.DateField(auto_now=True, verbose_name="Fecha de cambio del estado de la guia", help_text="MM/DD/AAAA")
  unidades = models.IntegerField(validators=[MinValueValidator(1)], verbose_name="Cantidad de unidades por despacho")
  peso = models.DecimalField(max_digits=15, decimal_places=2)

class GuiaEstado(models.Model):
  fecha_modificacion = models.DateField(auto_now=True, verbose_name="Fecha de cambio del estado de la guia", help_text="MM/DD/AAAA")

class EstadoGuia(models.Model):
    class EstadoGuia(models.TextChoices):
      PRODUCIDA = 'Producida', _('Producida')
      GENERADA = 'Generada', _('Generada')
      
    estado_guia = models.CharField(max_length=45, choices=EstadoGuia.choices, default=EstadoGuia.GENERADA, verbose_name="Estado de la guía")