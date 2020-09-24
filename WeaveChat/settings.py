"""
Django settings for WeaveChat project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

import os, sys
import inspect
import pathlib

FILENAME = inspect.getframeinfo(inspect.currentframe()).filename
PROJECTPATH = pathlib.Path(os.path.dirname(os.path.abspath(FILENAME)))
ROOTPATH = PROJECTPATH.parent

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = str(ROOTPATH)  # os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print('BASE_DIR', BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lkeq)cq&p!o^ww=2-j^wmg80hnyyv9c#tf&cmlqkincr%9km@c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', True)

ERROR_TRACE_LEVEL = 10

account_sid = ""
api_key = ""
api_key_secret = ""
app_sid = ""
push_credential_sid = ""
auth_token = ""

CALLER_NUMBER = '+13345680002'

google_api_key = ''
google_maps_api_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
google_place_photo_url = 'https://maps.googleapis.com/maps/api/place/photo?'

ALLOWED_HOSTS = ['3.18.187.218', '192.168.129.128', '127.0.0.1', '165.227.38.5', 'iweave.ca', 'iweave.com']

# ALLOWED_HOSTS = ['*']
AUTH_USER_MODEL = 'api.CustomUser'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.gis',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_gis',
    'push_notifications',
    'api.apps.ApiConfig',
    'chat.apps.ChatConfig',
    'friendship.apps.FriendshipConfig',
    'pages.apps.PagesConfig',
    'channels',
    'captcha',
    'recurrence',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}

AUTHENTICATION_BACKENDS = [
    'api.backends.phone_backend.PhoneBackend',
    'django.contrib.auth.backends.ModelBackend'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'api.middleware.ActiveUserMiddleware'
]

ROOT_URLCONF = 'WeaveChat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'WeaveChat.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'weave',
        'USER': 'postgres',
        'PASSWORD': '12qw!@QW',
        'PORT': '5432',
        'HOST': 'localhost'
    }
}

if os.environ.get('DB_HOST'):
    DATABASES['default']['HOST'] = os.environ.get('DB_HOST')

# -----------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
    }
}

# Number of seconds of inactivity before a user is marked offline
USER_ONLINE_TIMEOUT = 300

# Number of seconds that we will keep track of inactive users for before
# their last seen is removed from the cache
USER_LASTSEEN_TIMEOUT = 60 * 60 * 24 * 7

# ---------------------------------------------


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

PUSH_NOTIFICATIONS_SETTINGS = {
    "UPDATE_ON_DUPLICATE_REG_ID": True,
    "UNIQUE_REG_ID": False,
    "CONFIG": "push_notifications.conf.AppConfig",
    "APPLICATIONS": {
        "com.weave.up": {
            "PLATFORM": "APNS",
            "CERTIFICATE": os.path.join(BASE_DIR, 'WeaveChat/aps_dis.pem'),
            "TOPIC": "com.weave.up",
            "USE_SANDBOX": False
        },
        "com.weave.adhoc": {
            "PLATFORM": "APNS",
            "CERTIFICATE": os.path.join(BASE_DIR, 'WeaveChat/com.weave.adhoc.pem'),
            "TOPIC": "com.weave.adhoc",
            "USE_SANDBOX": False
        },
    }
}

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIR = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SENDSMS_FROM_NUMBER = '+13345680002'

FRIENDSHIP = {
    "USER_SERIALIZER": 'api.serializers.UserSerializer',
}

ASGI_APPLICATION = "chat.routing.application"
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": ['redis://127.0.0.1:6379']
        }
    },
}
EMAIL_HOST = 'smtp.outlook.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'davidweaves@outlook.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'message': {
            'format': "{asctime} {message}",
            'style': "{",
        },
        'detailed': {
            'format': "{levelname} {asctime} {module} {funcName} {lineno} {process}/{thread} {message} ",
            'style': "{",
        },
    },
    'handlers': {
        'console': {
            'class': "logging.StreamHandler",
            'level': "INFO",
            'formatter': "message",
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'applogfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(ROOTPATH / 'logs' / 'app.log'),
            'maxBytes': 1024 * 1024 * 15,  # 15MB
            'backupCount': 10,
            'formatter': "detailed",
        },

    },
    'loggers': {
        'django.request': {
            'handlers': ['applogfile', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        },
        'log': {
            'handlers': ['applogfile'],
            'level': 'DEBUG',
        },

    }
}

# print('LOGGING  -- ', LOGGING['handlers']['applogfile']['filename'])
