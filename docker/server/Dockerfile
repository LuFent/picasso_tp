FROM python:3.10

WORKDIR /app
RUN pip install --upgrade pip

ADD ./requirements.txt /app/
RUN pip install -r requirements.txt

ADD ./picasso_test_project /app/picasso_test_project
ADD ./docker /app/docker

RUN chmod +x /app/docker/server/celery-entrypoint.sh
RUN chmod +x /app/docker/server/django-entrypoint.sh
