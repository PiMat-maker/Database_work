#!/bin/sh

echo "$DATABASE_URL"

echo "$DATABASE"

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if [ "$DATABASE_URL" != "" ]
then
    echo "$DATABASE_URL"
    python manage.py create_db
    python manage.py seed_db
fi

while true; do
  sleep 1;
  done

exec "$@"