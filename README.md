# Django Dishes
## Инструкция по запуску без Docker
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
## Запуск с Docker-compose
```commandline
docker-compose build
```
```commandline
docker-compose up -d
```
```commandline
docker exec dish_order python manage.py migrate
```
```commandline
docker exec dish_order python manage.py createcachetable
```
```commandline
docker exec -it dish_order python manage.py createsuperuser
```