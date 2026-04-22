from django.core.exceptions import ValidationError
from users.models import CustomUser
from django.db.models import Q

def create_user_controller(data):
    username = data.get('username')
    role = data.get('role')
    phone = data.get('phone')
    password = data.get('password')

    if CustomUser.objects.filter(username=username).exists():
        raise ValidationError("El nombre de usuario ya existe.")

    return CustomUser.objects.create_user(
        username=username,
        password=password,
        role=role,
        phone_number=phone
    )

def show_users_controller(search_query: str = None):
    users = CustomUser.objects.all().order_by('-date_joined')
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query)
        )
    return users

def delete_users_controller(user_id: int, current_user: CustomUser):
    try:
        user_to_delete = CustomUser.objects.get(id=user_id)
        if user_to_delete == current_user:
             raise ValidationError("Por seguridad, no puedes eliminar tu propia cuenta activa.")
        user_to_delete.delete()
        return True
    except CustomUser.DoesNotExist:
        raise ValidationError("El usuario no existe.")

def edit_users_controller():
    pass