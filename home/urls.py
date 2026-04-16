from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_admin, name='index_admin'),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('users/', views.show_users, name='users'),
    path('service/', views.service, name='service'),
    path('plots/', views.plots, name='plots'),
]
