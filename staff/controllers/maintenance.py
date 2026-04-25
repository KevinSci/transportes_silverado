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
        # 1. Crear el servicio principal
        service = MaintenanceService.objects.create(
            title=data.get('title'),
            description=data.get('description'),
            service_type=data.get('service_type'),
            asset_id=data.get('asset'),
            reported_by=user,
            start_date=data.get('start_date') or timezone.now(),
            status='pendiente'
        )

        # 2. Extraer listas dinámicas
        names = data.getlist('supply_names[]')
        qtys = data.getlist('supply_qtys[]')
        needs_purchase = data.getlist('supply_needs_purchase[]')

        has_purchases = False
        supplies = []

        for i in range(len(names)):
            if not names[i].strip(): continue
            
            is_purchase = needs_purchase[i] == "true"
            if is_purchase: has_purchases = True

            supplies.append(ServiceSupply(
                service=service,
                name=names[i],
                quantity=qtys[i] or 1,
                needs_purchase=is_purchase
            ))

        if supplies:
            ServiceSupply.objects.bulk_create(supplies)

        # 3. Ajustar estatus si requiere compras para alertar al admin
        if has_purchases:
            service.status = 'esperando_insumos'
            service.save()
            
    return service

