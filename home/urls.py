from django.urls import path
from django.contrib.auth.decorators import user_passes_test
from . import views

def is_admin_user(user):
    return user.is_authenticated and user.role in ['administrador', 'propietario']

urlpatterns = [
    # Usuarios
    path('', user_passes_test(is_admin_user)(views.index_admin), name='index_admin'),
    path('users/', user_passes_test(is_admin_user)(views.show_users), name='users'),
    path('users/create_user/', user_passes_test(is_admin_user)(views.create_user), name='create_user'),
    path('users/delete/<int:user_id>/', user_passes_test(is_admin_user)(views.delete_users), name='delete_user'),
    # Activos
    path('assets/', user_passes_test(is_admin_user)(views.show_assets), name='assets'),
    path('assets/create_asset/', user_passes_test(is_admin_user)(views.create_asset), name='create_asset'),
    path('assets/delete/<int:asset_id>/', user_passes_test(is_admin_user)(views.delete_asset), name='delete_asset'),
    path('assets/edit/<int:asset_id>/', user_passes_test(is_admin_user)(views.edit_asset), name='edit_asset'),
    # Mantenimiento
    path('maintenance/', user_passes_test(is_admin_user)(views.maintenance), name='maintenance'),
    path('service/', user_passes_test(is_admin_user)(views.service), name='service'),
    path('plots/', user_passes_test(is_admin_user)(views.plots), name='plots'),
]
