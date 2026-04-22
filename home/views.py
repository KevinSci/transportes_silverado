# home/views.py
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from django.core.paginator import Paginator
from .controllers import users, assets


# Solo los admins pueden acceder a las vistas

def index_admin(request):
    return render(request, 'index.html')

# =========== Usuarios =========== #

def show_users(request: HttpRequest):
    search_query = request.GET.get('q', '')
    page_number = request.GET.get('page', 1)
    all_users = users.show_users_controller(search_query)
    paginator = Paginator(all_users, 10)
    page_obj = paginator.get_page(page_number)
    return render(request, 'users/users.html', {'page_obj': page_obj, 'search_query': search_query})

def create_user(request: HttpRequest):
    if request.method == 'POST':
        try:
            users.create_user_controller(request.POST)
            messages.success(request, f"Usuario creado con éxito.")
            return redirect('users')
        except Exception as e:
            messages.error(request, e.message)
    return render(request, 'users/create_user.html')

def delete_users(request: HttpRequest, user_id: int):
    if request.method == 'POST':
        try:
            users.delete_users_controller(user_id, request.user)
            messages.success(request, f"Usuario eliminado con éxito.")
        except Exception as e:
            messages.error(request, e.message)
    return redirect('users')

def edit_users(request: HttpRequest):
    pass

# =========== Activos =========== #

def show_assets(request: HttpRequest):
    search_query = request.GET.get('q', '')
    page_number = request.GET.get('page', 1)
    all_assets = assets.show_assets_controller(search_query)
    paginator = Paginator(all_assets, 10)
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'assets/assets.html', {
        'page_obj': page_obj, 
        'search_query': search_query
    })

def create_asset(request: HttpRequest):
    if request.method == 'POST':
        try:
            assets.create_asset_controller(request.POST)
            messages.success(request, f"Activo creado con éxito.")
            return redirect('assets')
        except Exception as e:
            messages.error(request, e.message)
    return render(request, 'assets/create_asset.html')

def delete_asset(request: HttpRequest, asset_id: int):
    if request.method == 'POST':
        try:
            assets.delete_asset_controller(asset_id)
            messages.success(request, "Activo eliminado con éxito.")
        except Exception as e:
            messages.error(request, getattr(e, 'message', str(e)))
    return redirect('assets')

def edit_asset(request: HttpRequest, asset_id: int):
    try:
        # Recuperamos el activo para pre-llenar el formulario
        asset = assets.Asset.objects.get(id=asset_id)
    except assets.Asset.DoesNotExist:
        messages.error(request, "El activo no existe.")
        return redirect('assets')

    if request.method == 'POST':
        try:
            assets.edit_asset_controller(asset_id, request.POST)
            messages.success(request, "Activo actualizado correctamente.")
            return redirect('assets')
        except Exception as e:
            messages.error(request, getattr(e, 'message', str(e)))
            
    return render(request, 'assets/edit_asset.html', {'asset': asset})



def maintenance(request):
    return render(request, 'maintenance.html')


def service(request):
    return render(request, 'service.html')


def plots(request):
    return render(request, 'plots.html')