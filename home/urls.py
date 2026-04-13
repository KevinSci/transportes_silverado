from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='home'),
    path('create_user/', views.create_user, name='create_user'),
    path('service/', views.service, name='service'),
    path('plots/', views.plots, name='plots'),
]
