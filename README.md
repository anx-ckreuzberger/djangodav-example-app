# DjangoDav Example App

This repo provides an example app for the [DjangoDav repo](https://github.com/anx-ckreuzberger/djangodav).

## Getting started

We recommend using the included docker image. For a quickstart, just do:

``docker-compose up``

You can find the dav server under ``http://0.0.0.0:8000/fsdav/`` aswell as ``http://0.0.0.0:8000/webdav/``.

You can log in with the following credentials:

* Username: ``foo``
* Password: ``bar``

## Developer Infos

The Django Server runs at port 5000, and on port 8000 an nginx server acts as a proxy. It is recommend to always access
the page via the proxy, as it handles static files, efficient file uploads and efficient file downloads.

When executing ``python manage.py`` commands, it is recommended to use the included docker image.

* Create Superuser: ``docker-compose run --rm python python manage.py createsuperuser``
* Makemigrations: ``docker-compose run --rm python python manage.py makemigrations``
* Migrate: ``docker-compose run --rm python python manage.py migrate``
* Collectstatic: ``docker-compose run --rm python python manage.py collectstatic``
