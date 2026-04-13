# users/views.py
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class RoleBasedLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        user = self.request.user
        
        # Redirección basada en el rol
        if user.role in ['administrador', 'propietario']:
            return reverse_lazy('home')  # Nombre de la URL de tu dashboard
        elif user.role == 'staff':
            # Asumimos que crearás una vista y URL llamada 'staff_home' en el módulo staff
            return reverse_lazy('staff_home') 
        
        # Fallback de seguridad
        return reverse_lazy('login')