"""Определяет схемы url для learning_logs_apps."""

from django.urls import path

from . import views

app_name = 'learning_logs_apps'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index')
]