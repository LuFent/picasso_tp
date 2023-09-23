#!/bin/sh

until cd /app/picasso_test_project
do
    echo "Waiting for server volume..."
done

celery -A picasso_test_project worker --loglevel=info --concurrency 1 -E
