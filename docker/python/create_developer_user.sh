#!/bin/bash

DIR=${PWD}
USER_ID=$(stat -c "%u" ${PWD})

echo "Using uid=${USER_ID} from owner of dir ${DIR}"

# verify if user exists
id "${USER_NAME?}"

if [[ $? -ne 0 ]]; then
	echo "Creating user ${USER_NAME} with UID ${USER_ID}"
	# create a new user, without home directory and without a password
	adduser -u ${USER_ID} -D -s /bin/bash ${USER_NAME}
fi
