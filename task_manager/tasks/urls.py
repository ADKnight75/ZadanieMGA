from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserViewSet, RegisterUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.task_list, name='task_list'), # Wyświetlenie listy zadań
    path('add/', views.add_task, name='add_task'),  # Dodawanie do listy zadań
    path('fields/', views.task_fields, name='task_fields'),  # Wyświetlenie nazw pól
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'), # Edycja konkretnego zadania
    path('task/<int:task_id>/', views.task_detail, name='task_detail'), # Szczegóły konkretnego zadania
    path('task/delete/<int:task_id>/', views.delete_task, name='delete_task'), # Usuwanie zadania
    path('task/<int:task_id>/history/', views.task_history, name='task_history'), #historia zmian
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Logowanie i pobieranie tokena JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Odświeżenie access tokena
    path('api/auth/', include('rest_framework.urls')),  # Rejestracja użytkowników
    path('api/register/', RegisterUserView.as_view(), name='register'), # Endpoint rejestracji użytkownika
]