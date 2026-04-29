# staff/urls.py
from django.urls import path
from . import views
from django.contrib.auth.decorators import user_passes_test

def is_staff_user(user):
    return user.is_authenticated and user.role == 'staff'

urlpatterns = [
    path('', user_passes_test(is_staff_user)(views.index), name='index_staff'),
    path('maintenance/', user_passes_test(is_staff_user)(views.staff_maintenance_list), name='maintenance_list'),
    path('maintenance/create/', user_passes_test(is_staff_user)(views.create_maintenance_service), name='create_maintenance'),
    path('maintenance/edit/', user_passes_test(is_staff_user)(views.edit_maintenance_service), name='edit_maintenance'),
    path('maintenance/delete/', user_passes_test(is_staff_user)(views.delete_maintenance_service), name='delete_maintenance'),
    
]

