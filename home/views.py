from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

def create_user(request):
    return render(request, 'create_user.html')

def service(request):
    return render(request, 'service.html')

def plots(request):
    return render(request, 'plots.html')

