import os
from .settings import *

STATIC_ROOT = os.path.join(BASE_DIR, "resources")

STATIC_URL = '/resources/'

DEBUG = False
ALLOWED_HOSTS = ['.bayareapython.com']

SECRET_KEY = os.getenv('BAYAREAPYTHON_SECRET')

DEFAULT_FROM_EMAIL = 'sf@simeonfranklin.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'sf@simeonfranklin.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = os.getenv('EMAILPW')
