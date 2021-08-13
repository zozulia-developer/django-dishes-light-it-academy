# Django Dishes
## Инструкция по запуску
1. Установить виртуальное окружение.
   * pip install virtualenv
   * python -m venv venv
2. Установить зависимости.
   * pip install -r requirements.txt
3. Установить миграции и создать таблицу для кэша.
   * python manage.py migrate
   * python manage.py createcachetable
4. Запустить Django сервер.
   * python manage.py runserver