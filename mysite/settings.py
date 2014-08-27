"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1&-qltu6v8njlz0sep!b_we1(pc!*xirjy+-na6ls*m2ba$ba%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'books',
    'garment',
    'south',
    'rest_framework',
    'snippets'
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 10
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__),'../templates'),
)

if os.path.split(sys.executable)[1].find('pythonw') != -1:
    console_handler = 'logging.NullHandler'
else:
    console_handler = 'logging.StreamHandler'

MYSITE_DIR = os.environ.get('MYSITE_DIR', os.path.join(os.path.expanduser('~'), '.mysite'))
if not os.path.isdir(os.path.join(os.path.expanduser('~'), '.mysite')):
    os.mkdir(os.path.join(os.path.expanduser('~'), '.mysite'))
debug_log_filename = 'debug.log'
celery_log_file_name = 'celery.log'
celery_task_log_file_name = 'celery_task.log'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    'formatters': {
        'console': {
            'format': '[%(asctime)s][%(levelname)s] %(name)s %(filename)s:%(funcName)s:%(lineno)d | %(message)s',
            'datefmt': '%y-%m-%d, %H:%M:%S',
            },
        'verbose': {
            'format': '%(asctime)s %(levelname)-8s[%(filename)s:%(lineno)d(%(funcName)s)] %(message)s',
            'datefmt': '%y-%m-%d, %H:%M:%S',
            },
        'celery': {
            'format': '[%(asctime)s: %(levelname)s/%(processName)s] %(message)s',
            'datefmt': '%y-%m-%d, %H:%M:%S',
            },
        },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
            },
        },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': console_handler,
            'formatter': 'console'
            },
        'debug_log_handler': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(MYSITE_DIR, debug_log_filename),
                'mode': 'a',
                'maxBytes': 0,
                'backupCount': 5,
                'encoding': 'utf-8',
                'formatter': 'verbose',
            },
        'celery_log_handler': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(MYSITE_DIR, celery_log_file_name),
                'mode': 'a',
                'maxBytes': 0,
                'backupCount': 5,
                'encoding': 'utf-8',
                'formatter': 'celery',
            },
        'celery_task_log_handler': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(MYSITE_DIR, celery_task_log_file_name),
                'mode': 'a',
                'maxBytes': 0,
                'backupCount': 5,
                'encoding': 'utf-8',
                'formatter': 'celery',
            },
        },

    'loggers': {
        '': {
            'handlers': ['console', 'debug_log_handler'],
            'level': 'DEBUG',
            'propagate': False,
            },
        'mysite.books': {
            'handlers': ['console', 'debug_log_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'mysite.common': {
            'handlers': ['console', 'debug_log_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'mysite.robot': {
            'handlers': ['console', 'debug_log_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'mysite.mysite_client': {
            'handlers': ['console', 'debug_log_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'celery': {
            'handlers': ['console', 'celery_log_handler'],
            'level': 'INFO',
            'propagate': False,
        },
        'celery.task': {
            'handlers': ['console', 'celery_task_log_handler'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console', 'debug_log_handler'],
            'level': 'WARNING',
            'propagate': False,
        },
    }
}
