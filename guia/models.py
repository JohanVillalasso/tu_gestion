from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from clientes.models import Cliente
from ciudades.models import Ciudad
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
      BODEGA_ORIGEN = 'En Bodega Origen', _('En Bodega Origen')
      BODEGA_DESTINO = 'En Bodega Destino', _('En Bodega Destino')
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
  estado = models.CharField(max_length=1, choices=EstadoLiquidador.choices, default=EstadoLiquidador.ACTIVO, verbose_name="Estado del liquidador")
  
  fecha_tarifa = models.DateField(auto_now=True, verbose_name="Fecha tarifas", help_text="MM/DD/AAAA")
  #foreignkey
  cod_CiudDANE = models.ForeignKey(Ciudad, on_delete=models.CASCADE, related_name='ciudadLiquidador')
  id_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, verbose_name="Servicio", related_name='servicioLiquidador')

#GUÍA DESPACHO
class GuiaDespacho(models.Model):
  hora = models.TimeField(auto_now=True, verbose_name="Hora captura guía")
  fecha = models.DateField(auto_now=True, verbose_name="Fecha cambio estado guiía", help_text="MM/DD/AAAA")
  destinatario = models.CharField(max_length=60, verbose_name="Datos destino")
  movil_destino = models.CharField(max_length=45, verbose_name="Número destino")
  direccion = models.CharField(max_length=100, verbose_name="Dirección de destino")
  unidades = models.IntegerField(validators=[MinValueValidator(1)], verbose_name="Cantidad unidades")
  peso = models.DecimalField(max_digits=15, decimal_places=2)
  
class Recogida(models.TextChoices):
    SI = '1', _('Si')
    NO = '0', _('No')
recogida = models.CharField(max_length=1, choices=Recogida.choices, default=Recogida.NO, verbose_name="Recogida?")
#foreignkey
id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuarioDespacho')
id_liquidador = models.ForeignKey(Liquidador, on_delete=models.CASCADE, verbose_name="Liquidador", related_name='liquidadorGuiaD')

#GUIA_ESTADO
class GuiaEstado(models.Model):
  fecha_modificacion = models.DateField(auto_now=True, verbose_name="Fecha cambio estado guia", help_text="MM/DD/AAAA")
    #foreignkey
  id_guia = models.ForeignKey(GuiaDespacho, on_delete=models.CASCADE, verbose_name="Guía", related_name='guiaEstado')
  id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, verbose_name="Estado", related_name='estadoGuia')
  
#DESPACHO CIUDAD
class DespachoCiudad(models.Model):
    class TipoCiudad(models.TextChoices):
      ORIGEN = 'Origen', _('Origen')
      DESTINO = 'Destino', _('Destino')
      
    tipo_ciudad = models.CharField(max_length=45, choices=TipoCiudad.choices, default=TipoCiudad.ORIGEN, verbose_name="Ciudad Origen Destino")
    #foreignkey
    id_guia = models.ForeignKey(GuiaDespacho, on_delete=models.CASCADE, verbose_name="Guia", related_name='guiaDespacho')
    cod_CiudDANE = models.ForeignKey(Ciudad, on_delete=models.CASCADE, related_name='CiudadDespacho')
    
#GUIA_CLIENTE
class GuiaCliente(models.Model):
  #foreignkey
  id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='clienteGuia')
  id_guia = models.ForeignKey(GuiaDespacho, on_delete=models.CASCADE, verbose_name="Guia", related_name='guiaCliente')
  
#GUIA SERVICIO
class GuiaServicio(models.Model):
  #foreignkey
  id_guia = models.ForeignKey(GuiaDespacho, on_delete=models.CASCADE, verbose_name="Guia", related_name='guiaServicio')
  id_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, verbose_name="Servicio", related_name='ServicioGuia')