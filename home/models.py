from django.db import models

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