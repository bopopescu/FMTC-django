"""
Django settings for FMTC project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url
from YamJam import yamjam





# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '3hb3&d00*4*=8ar^0j$f!d)vfk4eb-uja@dk1j=v)xra!lse-y'


if 'PROD' in os.environ:
    print('============= on HEROKU enviroment ==============')
    DEBUG = False
    print('')
    print(os.environ['SECRET_KEY'])
    print(os.environ['PROD'])
    print('---------')
else:
    print('============= on DEV enviroment ================')
    CFG = yamjam()['fmtc']
    DEBUG = True
    SECRET_KEY = CFG['secret_key']


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',
    'sidebar',
    'static_precompiler'
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'static_precompiler.finders.StaticPrecompilerFinder',
)

STATIC_PRECOMPILER_COMPILERS = (
    'static_precompiler.compilers.LESS',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'FMTC.urls'

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

WSGI_APPLICATION = 'FMTC.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets"), # static folder (not in any apps)
    os.path.join(BASE_DIR, "node_modules"),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/assets/'
MEDIA_URL = '/images/' # used in urls.py

STATIC_PRECOMPILER_ROOT = os.path.dirname(BASE_DIR + '/assets/')
STATIC_ROOT = os.path.dirname(BASE_DIR + '/static/')

MEDIA_ROOT = 'fmtc/'


# ----------------------------------------------------------------------------
# GOOGLE CLOUD
# ----------------------------------------------------------------------------

GOOGLE_APPLICATION_CREDENTIALS = CFG['google_cloud_storage']

PROJECT_ID = GOOGLE_APPLICATION_CREDENTIALS['project_id']

CLOUD_STORAGE_BUCKET = 'fmtc'


CLOUD_STORAGE_ROOT = "https://storage.googleapis.com/{bucket_name}/".format(
    bucket_name=CLOUD_STORAGE_BUCKET
)

MEDIA_PREFIX = "media/"
MEDIA_URL = "{gcs_root}{prefix}/".format(
    gcs_root=CLOUD_STORAGE_ROOT,
    prefix=MEDIA_PREFIX,
)

DEFAULT_FILE_STORAGE = 'google.storage.googleCloud.GoogleCloudStorage'





# ----------------------------------------------------------------------------
# PRODUCTION ENV SETTINGS
# ----------------------------------------------------------------------------

if DEBUG is False:
    # ----- HEROKU -----
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    ALLOWED_HOSTS = ['*']
