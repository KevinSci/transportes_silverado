from django.shortcuts import get_object_or_404, render, redirect
from .controllers import maintenance as maintenance_ctrl
from django.http import HttpRequest
from django.contrib import messages
from django.utils import timezone
from home.models import Asset


def index(request):
    return render(request, 'index_staff.html')

def staff_maintenance_list(request):
    active_services = maintenance_ctrl.get_active_services_for_staff()
    
    return render(request, 'maintenance/maintenance_list.html', {
        'services': active_services
    })

def create_maintenance_service(request: HttpRequest):
    if request.method == 'POST':
        try:
            maintenance_ctrl.create_maintenance_service_controller(request.POST, request.user)
            messages.success(request, "Servicio iniciado correctamente.")
            return redirect('maintenance_list')
        except Exception as e:
            messages.error(request, f"Error al procesar: {str(e)}")

    return render(request, 'maintenance/create_form.html', {
        'assets': Asset.objects.all(),
        'now': timezone.now()
    })

def edit_maintenance_service(request: HttpRequest, service_id: int):
    service = get_object_or_404(maintenance_ctrl.MaintenanceService, id=service_id)

    if request.method == 'POST':
        data = {
            'title': request.POST.get('title'),
            'description': request.POST.get('description'),
            'status': request.POST.get('status'),
        }
        
        try:
            maintenance_ctrl.edit_maintenance_service_controller(service_id, data)
            messages.success(request, "Servicio de mantenimiento actualizado correctamente.")
            return redirect('maintenance_list') 
        except ValueError as error:
            messages.error(request, str(error))

    return render(request, 'maintenance/edit_service.html', {
        'service': service
    })

def delete_maintenance_service(request: HttpRequest, service_id: int):
    if request.method == 'POST':
        try:
            maintenance_ctrl.delete_maintenance_service_controller(service_id)
            messages.success(request, "Servicio de mantenimiento eliminado.")
        except ValueError as error:
            messages.error(request, str(error))
            
        return redirect('maintenance_list')

    return redirect('maintenance_list')

