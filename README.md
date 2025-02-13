## Django Task Manager API

### Wymagania
- Python 3.x
- pip
- PostgreSQL
- Django 5.1.5
- Django REST Framework
- Simple JWT (dla autoryzacji)
- virtualenv (opcjonalnie)

### Instalacja
1. Klonowanie repozytorium
```sh
   git clone: https://github.com/ADKnight75/ZadanieMGA.git
   cd task_manager
```
2. Tworzenie i aktywacja wirtualnego środowiska
```sh
   python -m venv venv
   source venv/bin/activate  # Unix/macOS
   venv\Scripts\activate  # Windows
```
3. Instalacja zależności
```sh
   pip install -r requirements.txt
```
4. Konfiguracja bazy danych w `.env`
```
   DB_NAME=nazwa_bazy
   DB_USER=uzytkownik
   DB_PASSWORD=haslo
   DB_HOST=localhost
   DB_PORT=5432
```
5. Migracja bazy danych
```sh
   python manage.py makemigrations
   python manage.py migrate
```
6. Tworzenie superużytkownika
```sh
   python manage.py createsuperuser
```
7. Uruchomienie serwera
```sh
   python manage.py runserver
```

## Uzyskanie tokena JWT
Aby korzystać z API, musisz uzyskać token dostępu. 
```sh
   curl -X POST http://127.0.0.1:8000/api/token/ 
      -H "Content-Type: application/json"
      -d '{"username": "twoj_login", "password": "twoje_haslo"}'
```
W odpowiedzi otrzymasz tokeny JWT do autoryzacji żądań:
```json
{
    "refresh": "TWÓJ_REFRESH_TOKEN",
    "access": "TWÓJ_ACCESS_TOKEN"
}
```


### API

- **Pobranie listy zadań**
```sh
curl -X GET "http://127.0.0.1:8000/api/tasks/" -H "Authorization: Bearer TWÓJ_ACCESS_TOKEN"
```
- **Pobranie szczegółów zadania**
```sh
curl -X GET http://127.0.0.1:8000/api/tasks/1/ -H "Authorization: Bearer TWÓJ_ACCESS_TOKEN"
```
- **Dodanie nowego zadania**
```sh
curl -X POST "http://127.0.0.1:8000/api/tasks/" -H "Authorization: Bearer TWÓJ_ACCESS_TOKEN" -H "Content-Type: application/json" -d "{\"Nazwa\": \"Nowe Zadanie\", \"Status\": \"Nowy\", \"Przypisany_uzytkownik\": \"Michał\", \"Opis\": \"To jest nowe zadanie."}"
```
### **Usunięcie zadania**
```sh
curl -X DELETE http://127.0.0.1:8000/api/tasks/1/ -H "Authorization: Bearer TWÓJ_ACCESS_TOKEN"
```
### **Odświeżenie tokena JWT**
```sh
curl -X POST http://127.0.0.1:8000/api/token/refresh/ -H "Content-Type: application/json"  -d '{"refresh": "TWÓJ_REFRESH_TOKEN"}'
```

## **Dodawanie użytkowników do systemu**
Jeśli chcesz dodać nowego użytkownika do systemu przez API, użyj:
```sh
curl -X POST "http://127.0.0.1:8000/api/register/" 
     -H "Content-Type: application/json" 
     -d "{\"username\": \"nowy_user\", \"password\": \"haslo123\", \"email\": \"test@example.com\"}"
```
W odpowiedzi otrzymasz potwierdzenie utworzenia użytkownika:
```json
{
    "id": 2,
    "username": "nowy_user",
    "email": "test@example.com"
}
```

### **Logowanie użytkownika i pobranie tokena JWT**
Aby zalogować się jako istniejący użytkownik i pobrać token JWT:
```sh
curl -X POST "http://127.0.0.1:8000/api/token/" 
     -H "Content-Type: application/json" 
     -d "{\"username\": \"nowy_user\", \"password\": \"haslo123\"}"
```

W odpowiedzi otrzymasz tokeny JWT do autoryzacji żądań:
```json
{
    "refresh": "TWÓJ_REFRESH_TOKEN",
    "access": "TWÓJ_ACCESS_TOKEN"
}
```

## **Uruchamianie aplikacji przy użyciu Gunicorn**
Gunicorn jest serwerem HTTP przeznaczonym do uruchamiania aplikacji Django w środowisku produkcyjnym.

### **Uruchomienie aplikacji przy użyciu Gunicorn**
```sh
gunicorn task_manager.wsgi:application --bind 0.0.0.0:8000
```

### **Uruchomienie Gunicorn na Windowsie**
Gunicorn nie działa natywnie na Windowsie, ale można użyć `uvicorn` jako alternatywy:
```sh
pip install uvicorn
uvicorn task_manager.asgi:application --host 0.0.0.0 --port 8000
```