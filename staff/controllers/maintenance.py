# staff/controllers/maintenance.py
from django.core.exceptions import ValidationError
from django.db import transaction
from django.utils import timezone
from home.models import MaintenanceService, Asset, ServiceSupply

def get_active_services_for_staff():
    return MaintenanceService.objects.select_related('asset').exclude(status='terminado').order_by('-created_at')

def create_maintenance_service_controller(data, user):
    with transaction.atomic():
        # 1. Determinar el estado inicial basado en los insumos
        needs_purchase_list = data.getlist('supply_needs_purchase[]')
        # Si alguno es "true", el estado es 'esperando_insumos'
        status_inicial = 'esperando_insumos' if "true" in needs_purchase_list else 'pendiente'

        # 2. Crear el servicio con datos reales del POST
        service = MaintenanceService.objects.create(
            asset_id=data.get('asset_id'),
            title=data.get('title'),
            description=data.get('description'),
            service_type=data.get('service_type', 'correctivo'),
            start_date=data.get('start_date') or timezone.now(),
            reported_by=user,
            status=status_inicial
        )

        # 3. Procesar y guardar los insumos
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


def edit_maintenance_service_controller(service_id: int, data: dict):
    service = MaintenanceService.objects.filter(id=service_id).first()
    
    if not service:
        raise ValueError("El servicio de mantenimiento no existe.")

    if not data.get('title') or str(data.get('title')).strip() == '':
        raise ValueError("El título del servicio no puede estar vacío.")

    service.title = data.get('title')
    service.description = data.get('description', '') 
    service.status = data.get('status')    
    service.save()
    return service

def delete_maintenance_service_controller(service_id: int):
    service = MaintenanceService.objects.filter(id=service_id).first()
    if not service:
        raise ValueError("El servicio que intentas eliminar no fue encontrado.")
        
    service.delete()
    return True

