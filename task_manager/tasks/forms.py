from django import forms
from .models import Task

class TaskForm(forms.ModelForm): # Dodawanie i edycja
    class Meta:
        model = Task
        fields = ['Nazwa', 'Status', 'Przypisany_uzytkownik', 'Opis']  # Pola, które będą w formularzu
        widgets = {
            'Nazwa': forms.TextInput(attrs={'class': 'form-control'}),
            'Status': forms.Select(attrs={'class': 'form-control'}),
            'Przypisany_uzytkownik': forms.Select(attrs={'class': 'form-control'}),
            'Opis': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class TaskFilterForm(forms.Form): # Filtracja
    ID = forms.IntegerField(required=False, label="ID", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Nazwa = forms.CharField(required=False, label="Nazwa", widget=forms.TextInput(attrs={'class': 'form-control'}))
    Status = forms.ChoiceField(
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
    Przypisany_uzytkownik = forms.CharField(
        required=False,
        label="Użytkownik",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    Opis = forms.CharField(required=False, label="Opis", widget=forms.TextInput(attrs={'class': 'form-control'}))
