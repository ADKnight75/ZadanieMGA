# Import necessary libraries
from django.contrib.auth.models import User
from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import action
from rest_framework_simplejwt.authentication import JWTAuthentication

# Define Task model
class Task(models.Model):
    STATUS_CHOICES = [
        ('Nowy', 'Nowy'),
        ('W toku', 'W toku'),
        ('Rozwiązany', 'Rozwiązany')
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Nowy')
    assigned_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Define Task serializer
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

# Define Task history tracking model
class TaskHistory(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='history')
    changed_at = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()

# Signal to track changes and save to TaskHistory
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

@receiver(pre_save, sender=Task)
def track_task_history(sender, instance, **kwargs):
    if instance.pk:
        previous_task = Task.objects.get(pk=instance.pk)
        TaskHistory.objects.create(task=instance, data={
            'name': previous_task.name,
            'description': previous_task.description,
            'status': previous_task.status,
            'assigned_user': previous_task.assigned_user_id
        })

# Define Task viewset
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', 'status', 'assigned_user']

    @action(detail=True, methods=['get'])
    def history(self, request, pk=None):
        task = self.get_object()
        history = task.history.all()
        return Response({
            'history': [
                {
                    'changed_at': h.changed_at,
                    'data': h.data
                } for h in history
            ]
        })

# Setup Django Router
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

# URLs configuration
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls')),
]