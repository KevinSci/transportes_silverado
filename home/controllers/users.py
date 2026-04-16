from django.core.exceptions import ValidationError
from users.models import CustomUser
from django.db.models import Q

def create_user_controller(data):
        username = data.get('username')
        role = data.get('role')
        phone =data.get('phone')
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