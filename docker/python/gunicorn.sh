#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

# collect static files
python manage.py collectstatic --noinput
# make sure to migrate
python manage.py migrate --noinput

# create a demo user if it doesnt exist
python manage.py shell << END
from django.contrib.auth.models import User
user = User.objects.create_user('foo', password='bar')
END

# run gunicorn
gunicorn -b 0.0.0.0:5000 example_app.wsgi --workers ${GUNICORN_WORKERS} --timeout ${GUNICORN_TIMEOUT} $*
