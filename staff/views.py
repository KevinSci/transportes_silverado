from django.shortcuts import render
from .controllers import maintenance as maintenance_ctrl
from django.http import HttpRequest


def index(request):
    return render(request, 'index_staff.html')

def staff_maintenance_list(request):
    """Vista para listar servicios activos en la vista mobile del staff"""
    active_services = maintenance_ctrl.get_active_services_for_staff()
    
    return render(request, 'maintenance/maintenance_list.html', {
        'services': active_services
    })

def create_maintenance_service(request: HttpRequest):
    pass

def edit_maintenance_service(request: HttpRequest):
    pass

def delete_maintenance_service(request: HttpRequest):
    pass

