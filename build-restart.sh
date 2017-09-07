#!/bin/bash
pip freeze > requirements.txt \
&& docker-compose build \
&& docker-compose down \
&& docker-compose up -d
