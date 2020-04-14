
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6q-x(pg&mj5-*z51$-dv06%xj9%7cbwhat))8b#)w(zwmkd&d1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'masukat6455',
        'USER': 'masukat6455',
        'PASSWORD': 'yamsmos55',
        'HOST': 'localhost',
        'PORT': '',
    }
}
