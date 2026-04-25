from django.db import models
from django.conf import settings

class Asset(models.Model):
    ASSET_TYPE_CHOICES = [
        ('tracto', 'Tracto'),
        ('caja', 'Caja'),
    ]

    # Campos Comunes
    asset_type = models.CharField(
        max_length=10, 
        choices=ASSET_TYPE_CHOICES,
        verbose_name="Tipo de Activo"
    )
    number = models.CharField(max_length=50, unique=True, verbose_name="Número Económico")
    observations = models.TextField(blank=True, null=True, verbose_name="Observaciones")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Datos específicos para Tractos
    brand = models.CharField(max_length=100, blank=True, null=True, verbose_name="Marca")
    model_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Modelo")
    transmission = models.CharField(max_length=100, blank=True, null=True, verbose_name="Transmisión")
    operator = models.CharField(max_length=150, blank=True, null=True, verbose_name="Operador")
    operator_number = models.CharField(max_length=50, blank=True, null=True, verbose_name="Número de Operador")
    engine = models.CharField(max_length=100, blank=True, null=True, verbose_name="Motor")

    # Datos específicos para Cajas
    plates = models.CharField(max_length=20, blank=True, null=True, verbose_name="Placas")
    dimensions = models.CharField(max_length=100, blank=True, null=True, verbose_name="Dimensiones")
    state = models.CharField(max_length=100, blank=True, null=True, verbose_name="Estado")
    condition = models.CharField(max_length=100, blank=True, null=True, verbose_name="Condición")

    class Meta:
        verbose_name = "Activo"
        verbose_name_plural = "Activos"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_asset_type_display()} - {self.number}"
    

class MaintenanceService(models.Model):
    STATUS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('esperando_insumos', 'Esperando Cotización/Insumos'),
        ('terminado', 'Terminado'),
    ]

    SERVICE_TYPES = [
        ('preventivo', 'Preventivo'),
        ('correctivo', 'Correctivo'),
    ]

    title = models.CharField(max_length=150, verbose_name="Título del Servicio")
    description = models.TextField(verbose_name="Descripción del Problema/Servicio")
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES, default='correctivo')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pendiente')
    
    # Relaciones
    asset = models.ForeignKey('Asset', on_delete=models.CASCADE, related_name='services', verbose_name="Activo")
    reported_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='reported_services')
    
    # Fechas
    start_date = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Inicio")
    end_date = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Término")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'home_maintenance_service'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.asset.number}"


class ServiceSupply(models.Model):
    service = models.ForeignKey(MaintenanceService, on_delete=models.CASCADE, related_name='supplies')
    name = models.CharField(max_length=150, verbose_name="Nombre del Insumo")
    quantity = models.DecimalField(max_digits=8, decimal_places=2, default=1.0)
    brand = models.CharField(max_length=100, null=True, blank=True, verbose_name="Marca")
    model = models.CharField(max_length=100, null=True, blank=True, verbose_name="Modelo")
    
    needs_purchase = models.BooleanField(default=False, verbose_name="¿Requiere Compra?")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Precio Unitario (Admin)")
    
    def get_total_cost(self):
        if self.unit_price and self.quantity:
            return self.unit_price * self.quantity
        return 0

    class Meta:
        db_table = 'home_service_supply'