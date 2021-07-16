#!/bin/bash

python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
exec gunicorn library.wsgi:application -b 0.0.0.0:8000 --reload