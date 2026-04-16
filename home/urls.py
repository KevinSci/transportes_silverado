from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_admin, name='index_admin'),
    path('users/', views.show_users, name='users'),
    path('users/create_user/', views.create_user, name='create_user'),
    path('users/delete/<int:user_id>/', views.delete_users, name='delete_user'),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('service/', views.service, name='service'),
    path('plots/', views.plots, name='plots'),
]
