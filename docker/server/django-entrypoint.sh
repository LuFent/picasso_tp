#!/bin/sh

until cd /app/picasso_test_project
do
    echo "Waiting for server volume..."
done


until python manage.py makemigrations
do
    echo "Waiting for makemigrations"
    sleep 2
done

until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done


python manage.py collectstatic --noinput

gunicorn picasso_test_project.wsgi --bind 0.0.0.0:8000
