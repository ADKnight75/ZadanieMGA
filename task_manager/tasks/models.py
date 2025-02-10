from django.db import models
from simple_history.models import HistoricalRecords

class Task(models.Model):
    STATUS_CHOICES = [
        ('Nowy', 'Nowy'),
        ('W toku', 'W toku'),
        ('Rozwiązany', 'Rozwiązany'),
    ]

    USER_CHOICES = [
        ('Adam', 'Adam'),
        ('Daniel', 'Daniel'),
        ('Michał', 'Michał'),
        ('Paweł', 'Paweł'),
        ('Angelika', 'Angelika'),
    ]

    id = models.AutoField(db_column='ID', primary_key=True)  # AutoField odpowiada PostgreSQL SERIAL
    nazwa = models.CharField(db_column='Nazwa', max_length=255, null=False, default='Zadanie 1')  # character varying(255) NOT NULL
    status = models.CharField(db_column='Status', max_length=50, choices=STATUS_CHOICES, default='Nowy', null=False)  # character varying(50) NOT NULL
    przypisany_uzytkownik = models.CharField(db_column='Przypisany_uzytkownik', max_length=50, choices=USER_CHOICES, blank=True, null=True)  # character varying[] -> JSONField w Django
    opis = models.TextField(db_column='Opis', blank=True, null=True)  # text
    
    history = HistoricalRecords()  # Dodanie historii zmian

    class Meta:
        db_table = 'tasks'  # Wskazanie istniejącej tabeli w PostgreSQL

    def __str__(self):
        return self.Nazwa

