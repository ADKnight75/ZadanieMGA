from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'), # Wyświetlenie listy zadań
    path('add/', views.add_task, name='add_task'),  # Dodawanie do listy zadań
    path('fields/', views.task_fields, name='task_fields'),  # Wyświetlenie nazw pól
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'), # Edycja konkretnego zadania
    path('task/<int:task_id>/', views.task_detail, name='task_detail'), # Szczegóły konkretnego zadania
    path('task/delete/<int:task_id>/', views.delete_task, name='delete_task'), # Usuwanie zadania
    path('task/<int:task_id>/history/', views.task_history, name='task_history'), #historia zmian
]