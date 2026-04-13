# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('staff', 'Staff'),
        ('administrador', 'Administrador'),
        ('propietario', 'Propietario'),
    ]
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='staff')
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'auth_user' # Opcional: para mantener compatibilidad si ya tenías datos