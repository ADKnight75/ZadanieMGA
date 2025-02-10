from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Task
from .forms import TaskForm, TaskFilterForm
from .serializers import TaskSerializer, UserSerializer
from django.db.models import Q
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    @action(detail=True, methods=['post'])
    def assign(self, request, pk=None):
        task = self.get_object()
        task.Przypisany_uzytkownik = request.user.username
        task.save()
        return Response({'status': 'assigned'})

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def task_history(request, task_id):
    task = get_object_or_404(Task, ID=task_id)
    history = task.history.all().order_by('-history_date')

    user_filter = request.GET.get('user')
    if user_filter:
        history = history.filter(history_user__icontains=user_filter)

    return render(request, 'tasks/task_history.html', {'task': task, 'history': history})

def delete_task(request, task_id):
    task = get_object_or_404(Task, ID=task_id)
    task.delete()
    return redirect('task_list')  # Przekierowanie do listy zadań po usunięciu

def task_detail(request, task_id):
    task = get_object_or_404(Task, ID=task_id)  # Pobiera zadanie lub zwraca 404
    return render(request, 'tasks/task_detail.html', {'task': task})

def edit_task(request, task_id):
    task = get_object_or_404(Task, ID=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Zmień na nazwę widoku listy zadań
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Zapisz nowe zadanie do bazy danych
            return redirect('task_list')  # Przekieruj na listę zadań
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

def task_list(request):
    tasks = Task.objects.all()
    filter_form = TaskFilterForm(request.GET)

    if filter_form.is_valid():
        if filter_form.cleaned_data.get('ID'):
            tasks = tasks.filter(ID=filter_form.cleaned_data['ID'])
        if filter_form.cleaned_data.get('Nazwa'):
            tasks = tasks.filter(Nazwa__icontains=filter_form.cleaned_data['Nazwa'])
        if filter_form.cleaned_data.get('Opis'):
            tasks = tasks.filter(Opis__icontains=filter_form.cleaned_data['Opis'])
        if filter_form.cleaned_data.get('Status'):
            tasks = tasks.filter(Status=filter_form.cleaned_data['Status'])
        if filter_form.cleaned_data.get('Przypisany_uzytkownik'):
            tasks = tasks.filter(Przypisany_uzytkownik__icontains=filter_form.cleaned_data['Przypisany_uzytkownik'])

    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'filter_form': filter_form})

def task_fields(request):
    # Pobierz nazwy pól z modelu Task
    field_names = [field.name for field in Task._meta.fields]
    return render(request, 'tasks/task_fields.html', {'field_names': field_names})