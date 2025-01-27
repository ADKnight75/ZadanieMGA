from django.db import models

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

    ID = models.AutoField(db_column='ID', primary_key=True)  # AutoField odpowiada PostgreSQL SERIAL
    Nazwa = models.CharField(db_column='Nazwa', max_length=255, null=False, default='Zadanie 1')  # character varying(255) NOT NULL
    Status = models.CharField(db_column='Status', max_length=50, choices=STATUS_CHOICES, default='Nowy', null=False)  # character varying(50) NOT NULL
    Przypisany_uzytkownik = models.CharField(db_column='Przypisany_uzytkownik', max_length=50, choices=USER_CHOICES, blank=True, null=True)  # character varying[] -> JSONField w Django
    Opis = models.TextField(db_column='Opis', blank=True, null=True)  # text

    class Meta:
        db_table = 'tasks'  # Wskazanie istniejącej tabeli w PostgreSQL

    def __str__(self):
        return self.Nazwa

