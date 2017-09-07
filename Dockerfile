FROM python:3.5
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ADD . /app
WORKDIR /app
ENV PYTHONUNBUFFERED 1
