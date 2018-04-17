#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

python manage.py collectstatic --noinput
gunicorn -b 0.0.0.0:5000 example_app.wsgi --workers ${GUNICORN_WORKERS} --timeout ${GUNICORN_TIMEOUT} $*
