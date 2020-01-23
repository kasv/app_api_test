#!/bin/sh

env >> /etc/environment && \
python manage.py migrate --noinput && \
exec gunicorn app_api_test.wsgi:application -b 0.0.0.0:5000 -k=sync -w=5