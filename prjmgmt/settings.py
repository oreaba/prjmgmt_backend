"""
Django settings for prjmgmt project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent




# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(u8+r-ug^y@k^3c)0*axybi*g526$5wq5&*3yzrdyzx$#1vb*3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'adm-pm.me-south-1.elasticbeanstalk.com'
    ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # framework applications
    'rest_framework',
    'rest_framework.authtoken', # to issue tokens

    # internal applications
    'users',
    'projects',
    'tasks',
    'organizations',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'prjmgmt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
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

WSGI_APPLICATION = 'prjmgmt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

#------------------------- Environment section ---------------
from enum import Enum
from environs import Env
env = Env()
env.read_env()

class EnvType(Enum):
    UNDEFINED = None
    LOCAL = 'local'
    DEVELOPMENT = 'dev'
    STAGING = 'stag'
    PRODUCTION = 'prod'
    
    # @classmethod
    # def _missing_(cls, value: object) -> os.Any:
    #     return super()._missing_(cls.UNDEFINED)
    
ADM_PM_ENV = EnvType(os.getenv('ADM_PM_ENV', EnvType.PRODUCTION.value))
SQL_FILE = '/efs-adm-pm-db-prod/adm-pm.db.sqlite3' # same as .ebextensions/env_variables.config - /efs-adm-pm-db-prod
if ADM_PM_ENV == EnvType.LOCAL: 
    SQL_FILE = f'{BASE_DIR}/local_db/adm-pm.db.sqlite3'
print('loading environment: ', ADM_PM_ENV)

print('Loading database at: ', SQL_FILE)
# -----------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': SQL_FILE,#BASE_DIR / 'db.sqlite3',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.oracle',
#         'NAME': 'GISTEST',
#         'USER': 'sddprjmgmt',
#         'PASSWORD': 'PrjMgmt!23',
#         'HOST': '10.24.16.12', # Or the host where your Oracle database is located
#         'PORT': '1521', # Default Oracle port
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/' # defines the URL prefix for serving static files.
STATIC_ROOT = os.path.join(BASE_DIR, 'static_files') #specifies the directory where collected static files will be stored.
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_admin'),] # provides additional directories where static files will be collected from

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'users.PMUser'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        # Add other authentication classes if needed
    ],
}