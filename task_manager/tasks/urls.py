from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'), # Wyświetlenie listy zadań
    path('tasks/add/', views.add_task, name='add_task'),  # Dodawanie do listy zadań
    path('fields/', views.task_fields, name='task_fields'),  # Wyświetlenie nazw pól
]