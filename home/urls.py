from django.urls import path
from django.contrib.auth.decorators import user_passes_test
from . import views

def is_admin_user(user):
    return user.is_authenticated and user.role in ['administrador', 'propietario']

urlpatterns = [
    path('', user_passes_test(is_admin_user)(views.index_admin), name='index_admin'),
    path('users/', user_passes_test(is_admin_user)(views.show_users), name='users'),
    path('users/create_user/', user_passes_test(is_admin_user)(views.create_user), name='create_user'),
    path('users/delete/<int:user_id>/', user_passes_test(is_admin_user)(views.delete_users), name='delete_user'),
    path('maintenance/', user_passes_test(is_admin_user)(views.maintenance), name='maintenance'),
    path('service/', user_passes_test(is_admin_user)(views.service), name='service'),
    path('plots/', user_passes_test(is_admin_user)(views.plots), name='plots'),
]
