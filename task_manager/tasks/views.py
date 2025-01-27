from django.shortcuts import render, redirect
from .models import Task

from .forms import TaskForm

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Zapisz nowe zadanie do bazy danych
            return redirect('task_list')  # Przekieruj na listę zadań
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_fields(request):
    # Pobierz nazwy pól z modelu Task
    field_names = [field.name for field in Task._meta.fields]
    return render(request, 'tasks/task_fields.html', {'field_names': field_names})