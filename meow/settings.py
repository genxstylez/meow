"""
Django settings for meow project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ROOT_PATH = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), os.pardir), os.pardir))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hhrqjpzccwv(lek!o3i#a*i^_o#_35oebn+hj=p8r1x!pwdtw+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

JS_DEBUG = DEBUG

ALLOWED_HOSTS = []


ADMINS = (
    ('Sam Liu', 'genxstylez@gmail.com'),
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django_extensions',
    'meow',
    'documents',
    'providers',
    'gunicorn',
    'pagination',
    'south'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'meow.urls'

WSGI_APPLICATION = 'meow.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Cache

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(ROOT_PATH, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# Celery Related
# redis://:password@hostname:port/db_number

BROKER_URL = 'redis://localhost:6379/0'

CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'crawl-every-hour': {
        'task': 'meow.tasks.crawl',
        'schedule': timedelta(hours=1),
        'args': None
    },
}
"""
'refresh-every-quarter': {
    'task': 'meow.tasks.refresh_embed',
    'schedule': timedelta(minutes=15),
    'args': None
},
"""
CELERY_TIMEZONE = 'UTC'

# CELERY_IddMPORTS=("meow.tasks",)

# Logging

LOGGING = {
    'version': 1,
}

# Templates

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, '../templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "meow.context_processors.js_debug",
)


# Site headins
SITE_TITLE = 'development'

SITE_KEYWORDS = 'development'

SITE_DESCRIPTION = 'development'

SITE_BRAND = 'development'

SITE_SLOGAN = 'development'

CACHE_MIDDLEWARE_SECONDS = 600

API_LIMIT_PER_PAGE = 50

try:
    from local_settings import *
except ImportError:
    pass
