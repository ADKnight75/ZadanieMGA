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
   curl -X POST http://127.0.0.1:8000/api/token/ \
      -H "Content-Type: application/json" \
      -d '{"username": "twoj_login", "password": "twoje_haslo"}'
```
W odpowiedzi otrzymasz `access` i `refresh` token.


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
