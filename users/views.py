# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import CustomUser # Asegúrate de haber creado el modelo CustomUser primero

def register_view(request):
    # Por ahora, una vista simple para evitar el error de atributo
    if request.method == 'POST':
        # Lógica de registro aquí
        pass
    return render(request, 'register.html')

def login_view(request):
    # Esta es opcional si usas LoginView de Django en urls.py
    return render(request, 'login.html')

def logout_view(request):
    pass

def admin_view(request):
    pass