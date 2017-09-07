#!/bin/bash
cd /app \
&& python manage.py collectstatic --noinput \
&& python manage.py migrate --noinput \
&& python manage.py runscript csu.py \
&& python manage.py runscript slugifyall \
&& python manage.py runscript initialconfig \
&& python manage.py runscript numbervalues \
&& uwsgi /app/buildapp/uwsgi.ini
