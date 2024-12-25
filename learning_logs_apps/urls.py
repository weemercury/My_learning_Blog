"""Определяет схемы url для learning_logs_apps."""

from django.urls import path

from . import views

app_name = 'learning_logs_apps'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница со списком всех тем.
    path('topics/', views.topics, name='topics'),
    # Страница с подробной информацией по отдельной теме
]