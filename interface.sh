#!/bin/bash
cd /app \
&& python manage.py collectstatic --noinput \
&& python manage.py migrate --noinput \
&& python manage.py runscript csu \
&& uwsgi /app/ddd/uwsgi.ini
