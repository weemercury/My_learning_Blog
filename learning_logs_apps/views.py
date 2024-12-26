from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    """Домашняя страница приложения learning_logs_apps"""
    return render(request, 'learning_logs_apps/index.html')

def topics(request):
    """Выводит список тем."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs_apps/topics.html', context)

def topic(request, topic_id):
    """Выводит одну тему и все ее записи."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs_apps/topic.html', context)

def new_topic(request):
    """Определяет новую тему."""
    if request.method != 'POST':
        # Данные не отправлялись, создается пустая форма.
        form = TopicForm()
    else:
        # Отправлены данные POST - обработать данные.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs_apps:topics')
        
    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'learning_logs_apps/new_topic.html', context)

def new_entry(request, topic_id):
    """Добавляет новую запись по конкретной теме."""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # Данные не отправлялись, создается пустая форма.
        form = EntryForm()
    else:
        # Отправлены данные POST - обработать данные.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs_apps:topic', topic_id=topic_id)
        
    # Вывести пустую или недействительную форму.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs_apps/new_entry.html', context)