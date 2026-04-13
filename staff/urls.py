# staff/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.staff_home, name='staff_home'),
]