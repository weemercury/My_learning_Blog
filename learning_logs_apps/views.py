from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """Домашняя страница приложения learning_logs_apps"""
    return render(request, 'learning_logs_apps/index.html')

def topics(request):
    """Выводит список тем."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs_apps/topics.html', context)