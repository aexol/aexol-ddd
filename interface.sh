#!/bin/bash
cd /app \
&& python manage.py collectstatic --noinput \
&& python manage.py migrate --noinput \
&& uwsgi /app/ddd/uwsgi.ini
