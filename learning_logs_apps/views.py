from django.shortcuts import render

# Create your views here.

def index(request):
    """Домашняя страница приложения learning_logs_apps"""
    return render(request, 'learning_logs_apps/index.html')