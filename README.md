# Django Dishes
## Инструкция по запуску
1. Установить виртуальное окружение.
```commandline
pip install virtualenv
```
```commandline
python -m venv venv
```
2. Установить зависимости.
```commandline
pip install -r requirements.txt
```
3. Установить миграции и создать таблицу для кэша.
```commandline
python manage.py migrate
```
```commandline
python manage.py createcachetable
```
4. Запустить Django сервер.
```commandline
python manage.py runserver
```
---
## Запуск с Docker
```commandline
docker build -f Dockerfile --tag light-it-docker:latest .
```
```commandline
docker run -d -p 8082:8000 light-it-docker
```
---
- Создать супер пользователя, container_id - id текущего контейнера
```commandline
docker exec -it container_id python manage.py createsuperuser
```