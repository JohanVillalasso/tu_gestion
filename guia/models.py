from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from clientes.models import Cliente
from ciudades.models import Ciudades
from usuarios.models import Usuario

#SERVICIO
class Servicio(models.Model):
  nombre_servicio = models.CharField(max_length=60, verbose_name="Nombre o tipo de servicio")

#ESTADO
class Estado(models.Model):
    class EstadoGuia(models.TextChoices):
      PRODUCIDA = 'Producida', _('Producida')
      GENERADA = 'Generada', _('Generada')
      DESPACHADA = 'Despachada', _('Despachada')
      EN_BODEGA_ORIGEN = 'En Bodega Origen', _('En Bodega Origen')
      EN_BODEGA_DESTINO = 'En Bodega Destino', _('En Bodega Destino')
      ANULADA = 'Anulada', _('Anulada')
      
    estado_guia = models.CharField(max_length=45, choices=EstadoGuia.choices, default=EstadoGuia.GENERADA, verbose_name="Estado de la guía")
    
    class Novedad(models.TextChoices):
      DIRECCION_DESTINO_NO_EXISTE = 'Direccion destino no existe', _('Direccion Destino no existe')
      CLIENTE_DESTINO_NO_SE_ENCONTRABA = 'Cliente destino no se encontraba', _('Cliente destino no se encontraba')
      INCONVENIENTES_OPERATIVOS = 'Inconvenientes operativos', _('Inconvenientes Operativos')
      
    novedad_guia = models.CharField(max_length=45, choices=Novedad.choices, default=Novedad.INCONVENIENTES_OPERATIVOS, verbose_name="Novedad que presenta la guía")

#LIQUIDADOR
class Liquidador(models.Model):
  precio_ciudad = models.DecimalField(max_digits=15, decimal_places=2)
  
  class EstadoLiquidador(models.TextChoices):
    ACTIVO = '1', _('Activo')
    INACTIVO = '0', _('Inactivo')
  estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado del liquidador")
  
  fecha_tarifas = models.DateField(auto_now=True, verbose_name="Fecha de las tarifas", help_text="MM/DD/AAAA")
  #foreignkey
  cod_CiudDANE = models.ForeignKey(Ciudades, on_delete=models.PROTECT, related_name='Ciudades')
  id_servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT, verbose_name="Servicio")

#GUÍA DESPACHO
class GuiaDespacho(models.Model):
  hora = models.TimeField(auto_now=True, verbose_name="Hora de captura de la guía")
  fecha = models.DataField(auto_now=True, verbose_name="Fecha de cambio del estado de la guiía", help_text="MM/DD/AAAA")
  destinatario = models.CharField(max_length=60, verbose_name="Datos de destinatario")
  movil_destinatario = models.CharField(max_length=45, verbose_name="Número de teléfono de destinatario")
  direccion = models.CharField(max_length=100, verbose_name="Dirección de destino")
  unidades = models.IntegerField(validators=[MinValueValidator(1)], verbose_name="Cantidad de unidades por despacho")
  peso = models.DecimaField(max_digits=15, decimal_places=2)
  
class Recogida(models.TextChoices):
    SI = '1', _('Si')
    NO = '0', _('No')
recogida = models.CharField(max_length=1, choices=Recogida.choices, default=Recogida.NO, verbose_name="El cliente solicitó servicio de recogida?")
#foreignkey
id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='Usuario')
id_liquidador = models.ForeignKey(Liquidador, on_delete=models.PROTECT, verbose_name="Liquidador")

#GUIA_ESTADO
class GuiaEstado(models.Model):
  fecha_modificacion = models.DateField(auto_now=True, verbose_name="Fecha de cambio del estado de la guia", help_text="MM/DD/AAAA")
    #foreignkey
  id_guia = models.ForeignKey(GuiaDespacho, on_delete=models.PROTECT, verbose_name="Guia")
  id_estado = models.ForeignKey(Estado, on_delete=models.PROTECT, verbose_name="estado")
  
#DESPACHO CIUDAD
class DespachoCiudad(models.Model):
    class TipoCiudad(models.TextChoices):
      ORIGEN = 'Origen', _('Origen')
      DESTINO = 'Destino', _('Destino')
      
    tipo_ciudad = models.CharField(max_length=45, choices=TipoCiudad.choices, default=TipoCiudad.ORIGEN, verbose_name="Ciudad Origen o Destino")
    #foreignkey
    id_guia = models.ForeignKey(GuiaDespacho, on_delete=models.PROTECT, verbose_name="Guia")
    cod_CiudDANE = models.ForeignKey(Ciudades, on_delete=models.PROTECT, related_name='Ciudades')
    
#GUIA_CLIENTE
class GuiaCliente(models.Model):
  #foreignkey
  id_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='Cliente')
  id_guia = models.ForeignKey(GuiaDespacho, on_delete=models.PROTECT, verbose_name="Guia")
  
#GUIA SERVICIO
class GuiaServicio(models.Model):
  #foreignkey
  id_guia = models.ForeignKey(GuiaDespacho, on_delete=models.PROTECT, verbose_name="Guia")
  id_servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT, verbose_name="Servicio")