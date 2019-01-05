FROM python:3.6-alpine

# from https://github.com/pydanny/cookiecutter-django/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/docker/django/Dockerfile

ENV PYTHONUNBUFFERED 1

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi \
  # lxml dependencies
  && apk add libxml2-dev libxslt-dev \
  # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
  && apk add postgresql-client \
  # git and bash
  && apk add bash git

RUN addgroup -S django \
    && adduser -S -G django django

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt \
  && pip install --no-cache-dir psycopg2-binary \
  && pip install --no-cache-dir gunicorn daphne channels

COPY ./docker/python/gunicorn.sh /gunicorn.sh
RUN chmod +x /gunicorn.sh

COPY ./docker/python/daphne.sh /daphne.sh
RUN chmod +x /daphne.sh

COPY ./docker/python/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./docker/python/create_developer_user.sh /create_developer_user.sh
RUN chmod +x /create_developer_user.sh

WORKDIR /app/app

ENTRYPOINT ["/entrypoint.sh"]
