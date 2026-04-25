# staff/controllers/maintenance.py
from home.models import MaintenanceService

def get_active_services_for_staff():
    """
    Retorna los servicios que no están terminados, 
    optimizando la consulta trayendo el activo relacionado.
    """
    return MaintenanceService.objects.select_related('asset').exclude(status='terminado').order_by('-created_at')

def create_maintenance_service_controller(data, user):
    """
    Aquí iría la lógica para procesar el formulario de creación,
    incluyendo la creación dinámica de los Insumos (ServiceSupply).
    """
    pass # Lo implementaremos a detalle cuando hagamos el formulario de guardado

