from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def is_staff_user(user):
    return user.is_authenticated and user.role == 'staff'

@user_passes_test(is_staff_user, login_url='login')
def staff_home(request):
    return render(request, 'staff_dashboard.html')