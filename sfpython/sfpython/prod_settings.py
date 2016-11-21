import os
from .settings import *

STATIC_ROOT = os.path.join(BASE_DIR, "resources")

STATIC_URL = '/resources/'

DEBUG = False
ALLOWED_HOSTS = ['.bayareapython.com']
