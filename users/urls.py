# users/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import RoleBasedLoginView

urlpatterns = [
    # Usamos nuestra vista basada en clase personalizada
    path('login/', RoleBasedLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # Se eliminó la ruta 'register' intencionalmente.
]