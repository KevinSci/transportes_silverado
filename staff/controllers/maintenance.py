# staff/controllers/maintenance.py
from django.core.exceptions import ValidationError
from django.db import transaction
from django.utils import timezone
from home.models import MaintenanceService, Asset, ServiceSupply

def get_active_services_for_staff():
    """
    Retorna los servicios que no están terminados, 
    optimizando la consulta trayendo el activo relacionado.
    """
    return MaintenanceService.objects.select_related('asset').exclude(status='terminado').order_by('-created_at')

def create_maintenance_service_controller(data, user):
    with transaction.atomic():
        service = MaintenanceService.objects.create(
            # ... (campos del servicio se mantienen igual)
        )

        names = data.getlist('supply_names[]')
        brands = data.getlist('supply_brands[]')
        models = data.getlist('supply_models[]')
        qtys = data.getlist('supply_qtys[]')
        needs_purchase = data.getlist('supply_needs_purchase[]')

        supplies = []
        for i in range(len(names)):
            if not names[i].strip(): continue
            
            supplies.append(ServiceSupply(
                service=service,
                name=names[i],
                brand=brands[i] if i < len(brands) else '',
                model=models[i] if i < len(models) else '',
                quantity=qtys[i] or 1,
                needs_purchase=needs_purchase[i] == "true"
            ))

        if supplies:
            ServiceSupply.objects.bulk_create(supplies)
    return service

