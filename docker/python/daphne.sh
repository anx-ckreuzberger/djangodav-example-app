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
if not User.objects.filter(username='foo').exists():
    user = User.objects.create_user('foo', password='bar')

END

# run daphne
daphne -b 0.0.0.0 -p 5000 example_app.asgi:application -v 2 --proxy-headers $*
