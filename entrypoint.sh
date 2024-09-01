#!/bin/bash

if [ -f "$SECRET_KEY_FILE" ]; then
    export SECRET_KEY=$(cat $SECRET_KEY_FILE)
fi

if [ -f "$POSTGRES_PASSWORD_FILE" ]; then
    export POSTGRES_PASSWORD=$(cat $POSTGRES_PASSWORD_FILE)
fi

poetry run python manage.py migrate

poetry run gunicorn holycard_server.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level info \
    --timeout 30
