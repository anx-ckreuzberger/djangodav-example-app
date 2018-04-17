#!/bin/bash

# from https://github.com/pydanny/cookiecutter-django/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/compose/production/django/entrypoint.sh

set -o errexit
set -o pipefail
set -o nounset


cmd="$@"

if [ -z "${POSTGRES_USER}" ]; then
    base_postgres_image_default_user='postgres'
    export POSTGRES_USER="${base_postgres_image_default_user}"
fi
export DATABASE_URL="postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres:5432/${POSTGRES_DB}"

postgres_ready() {
python << END
import sys
import psycopg2
try:
    psycopg2.connect(
        dbname="${POSTGRES_DB}",
        user="${POSTGRES_USER}",
        password="${POSTGRES_PASSWORD}",
        host="postgres"
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo 'PostgreSQL is not available yet (sleeping)...'
  sleep 2
done

>&2 echo 'PostgreSQL is up - continuing...'

# now make sure we are running as the user that owns the files within /app
export USER_NAME="developer"
/create_developer_user.sh

# make sure our volumes are writable by this user
#chgrp -R ${USER_NAME} /static_files
#chmod 775 /static_files
#chgrp -R ${USER_NAME} /uploaded_files
#chmod 755 /uploaded_files

#exec su -p -c "cd /app/app && $cmd" ${USER_NAME}
exec $cmd

# when executing commands use this:
# docker-compose -f docker-compose.dev.yml run --rm python python manage.py makemigrations

