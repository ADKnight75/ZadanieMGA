from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['Nazwa', 'Status', 'Przypisany_uzytkownik', 'Opis']  # Pola, które będą w formularzu
        widgets = {
            'Nazwa': forms.TextInput(attrs={'class': 'form-control'}),
            'Status': forms.Select(attrs={'class': 'form-control'}),
            'Przypisany_uzytkownik': forms.Select(attrs={'class': 'form-control'}),
            'opis': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
