# home/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest
from django.contrib import messages
from django.core.paginator import Paginator
from .controllers import users


# Solo los admins pueden acceder a las vistas
def is_admin_user(user):
    return user.is_authenticated and user.role in ['administrador', 'propietario']

@user_passes_test(is_admin_user, login_url='login')
def index_admin(request):
    return render(request, 'index.html')

# =========== Usuarios =========== #

@user_passes_test(is_admin_user, login_url='login')
def show_users(request: HttpRequest):
    search_query = request.GET.get('q', '')
    page_number = request.GET.get('page', 1)
    all_users = users.show_users_controller(search_query)
    paginator = Paginator(all_users, 10)
    page_obj = paginator.get_page(page_number)
    return render(request, 'users/users.html', {'users': page_obj, 'search_query': search_query})



@user_passes_test(is_admin_user, login_url='login')
def create_user(request: HttpRequest):
    if request.method == 'POST':
        try:
            users.create_user_controller(request.POST)
            messages.success(request, f"Usuario creado con éxito.")
            return redirect('users')
        except Exception as e:
            messages.error(request, e.message)
    return render(request, 'users/create_user.html')


def delete_users(request: HttpRequest):
    pass

def edit_users(request: HttpRequest):
    pass

@user_passes_test(is_admin_user, login_url='login')
def maintenance(request):
    return render(request, 'maintenance.html')

@user_passes_test(is_admin_user, login_url='login')
def service(request):
    return render(request, 'service.html')

@user_passes_test(is_admin_user, login_url='login')
def plots(request):
    return render(request, 'plots.html')