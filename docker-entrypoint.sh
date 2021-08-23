#!/bin/bash
echo "Database migration"
python manage.py migrate
echo "Creating cache table"
python manage.py createcachetable
echo "Start server"
python manage.py runserver 0.0.0.0:8000