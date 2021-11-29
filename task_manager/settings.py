"""
Django settings for task_manager project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
import django_heroku
import dj_database_url
import rollbar

from pathlib import Path
from dotenv import load_dotenv

from django.utils.translation import gettext_lazy as _
# ! выбор локалей
# ! https://habr.com/ru/company/ruvds/blog/498452/
# ! django.core.exceptions.AppRegistryNotReady: The translation infrastructure
# ! cannot be initialized before the apps registry is ready. Check that you
# ! don't make non-lazy gettext calls at import time.

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# load_dotenv()
env_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=env_path)  # ! взять переменные среды из .env.


SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'  # dev
# DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'  # prod
# DEBUG = os.getenv('DJANGO_DEBUG') != 'False'  # prod
# DEBUG = False
DEBUG = os.getenv('DJANGO_DEBUG') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'todo-shka.herokuapp.com')
# ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'todo-shka.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4',
    'django_tables2',
    'django_filters',
    'task_manager',
    'statuses',
    'labels',
    'tasks',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # ! включение перевода
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
]

ROOT_URLCONF = 'task_manager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'task_manager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

db_from_env = dj_database_url.config(conn_max_age=500, ssl_require=False)
DATABASES['default'].update(db_from_env)
django_heroku.settings(locals(), databases=False)


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale'), ]

LANGUAGE_CODE = 'ru'
LANGUAGES = (
    ('en-us', _('English')),
    ('ru', _('Russian')),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
    # '/var/www/static/', # ! папка для сервера?
]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# ! сборная папка для файлов в режиме эксплуатации


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'


ROLLBAR = {
    'access_token': os.getenv('POST_SERVER_ITEM_ACCESS_TOKEN'),
    'environment': 'development' if DEBUG else 'production',
    'root': BASE_DIR,
}

rollbar.init(**ROLLBAR)
# https://docs.rollbar.com/docs/django

# django_heroku.settings(locals(), databases=False)
