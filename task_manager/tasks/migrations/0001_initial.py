# Generated by Django 5.1.6 on 2025-02-10 12:52

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalTask',
            fields=[
                ('id', models.IntegerField(blank=True, db_column='ID', db_index=True)),
                ('nazwa', models.CharField(db_column='Nazwa', default='Zadanie 1', max_length=255)),
                ('status', models.CharField(choices=[('Nowy', 'Nowy'), ('W toku', 'W toku'), ('Rozwiązany', 'Rozwiązany')], db_column='Status', default='Nowy', max_length=50)),
                ('opis', models.TextField(blank=True, db_column='Opis', null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('przypisany_uzytkownik', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical task',
                'verbose_name_plural': 'historical tasks',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nazwa', models.CharField(db_column='Nazwa', default='Zadanie 1', max_length=255)),
                ('status', models.CharField(choices=[('Nowy', 'Nowy'), ('W toku', 'W toku'), ('Rozwiązany', 'Rozwiązany')], db_column='Status', default='Nowy', max_length=50)),
                ('opis', models.TextField(blank=True, db_column='Opis', null=True)),
                ('przypisany_uzytkownik', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='zadania', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tasks',
            },
        ),
    ]
