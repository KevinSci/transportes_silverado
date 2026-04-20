# home/views.py
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from django.core.paginator import Paginator
from .controllers import users


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

def maintenance(request):
    return render(request, 'maintenance.html')


def service(request):
    return render(request, 'service.html')


def plots(request):
    return render(request, 'plots.html')