from django import forms
from .models import Task

class TaskForm(forms.ModelForm): # Dodawanie i edycja
    class Meta:
        model = Task
        fields = ['nazwa', 'status', 'przypisany_uzytkownik', 'opis']  # Pola, które będą w formularzu
        widgets = {
            'nazwa': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'przypisany_uzytkownik': forms.Select(attrs={'class': 'form-control'}),
            'opis': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class TaskFilterForm(forms.Form): # Filtracja
    id = forms.IntegerField(required=False, label="ID", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    nazwa = forms.CharField(required=False, label="Nazwa", widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(
        required=False,
        label="Status",
        choices=[
            ('', '--- Wybierz status ---'),
            ('Nowy', 'Nowy'),
            ('W toku', 'W toku'),
            ('Rozwiązane', 'Rozwiązane'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    przypisany_uzytkownik = forms.CharField(
        required=False,
        label="Użytkownik",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    opis = forms.CharField(required=False, label="Opis", widget=forms.TextInput(attrs={'class': 'form-control'}))
