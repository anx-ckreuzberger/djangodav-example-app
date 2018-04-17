from settings.base import *

# static file directory
STATIC_ROOT = "/static_files"

# define the media root, where all the uploaded files will be put
MEDIA_ROOT = "/uploaded_files"

ALLOWED_HOSTS.append('0.0.0.0')
ALLOWED_HOSTS.append('10.0.28.2')

DJANGODAV_X_REDIRECT = True
DJANGODAV_X_REDIRECT_PREFIX = "/uploads"
