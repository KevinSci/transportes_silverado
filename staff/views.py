from django.shortcuts import render, redirect
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
            return redirect('staff:maintenance_list')
        except Exception as e:
            messages.error(request, f"Error al procesar: {str(e)}")

    return render(request, 'maintenance/create_form.html', {
        'assets': Asset.objects.all(),
        'now': timezone.now()
    })

def edit_maintenance_service(request: HttpRequest):
    pass

def delete_maintenance_service(request: HttpRequest):
    pass

