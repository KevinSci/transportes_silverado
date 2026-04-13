# home/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from users.models import CustomUser

# Solo administrador o propietario pueden crear usuarios
def can_create_users(user):
    return user.is_authenticated and user.role in ['administrador', 'propietario']

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@user_passes_test(can_create_users, login_url='home')
def create_user(request):
    if request.method == 'POST':
        u_name = request.POST.get('username')
        u_pass = request.POST.get('password')
        u_role = request.POST.get('role')
        u_phone = request.POST.get('phone')

        if CustomUser.objects.filter(username=u_name).exists():
            messages.error(request, "El nombre de usuario ya existe.")
        else:
            CustomUser.objects.create_user(
                username=u_name, 
                password=u_pass, 
                role=u_role, 
                phone_number=u_phone
            )
            messages.success(request, f"Usuario {u_name} creado con éxito.")
            return redirect('home')
    return render(request, 'create_users.html')

# Agregamos las funciones faltantes para que las URLs no rompan
def service(request):
    return render(request, 'service.html')

def plots(request):
    return render(request, 'plots.html')