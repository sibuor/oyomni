#ARU-two_SCOOPS-INSPIRED:
#settings/development.py
'''
development settings

- Run in Debug mode
- Use console backend for emails
- Add Django Debug Toolbar
- Add django-extensions as app
'''
from .base import *
import sys
import logging.config

# SECURITY WARNING: don't run with debug turned on in production!

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

#Arun
#----
#DEBUG = True
#TEMPLATES[0]['OPTIONS'].update({'debug': True})

# Turn off debug while imported by Celery with a workaround
# See http://stackoverflow.com/a/4806384
if "celery" in sys.argv[0]:
    DEBUG = False

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env("DJANGO_SECRET_KEY", default='hdctm1d4ftczk6d9o8uik!5z6ylx*=s4f5uke1+)&*#9#i($nw')


#Mail settings
# ------------------------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025



#DATABASE CONFIGURATION
#--------------------------------------------------------------------------------
#Proper db config
#--------------
# DATABASES = {
#       "default": {  
#       "ENGINE": "django.db.backends.postgresql_psycopg2",
#       "NAME": "<project_name>",
#       "USER": "",
#       "PASSWORD": "osopr",
#       "HOST": "localhost",
#       "PORT": "",
#     }
# }

#testing db config
#-----------------
DATABASES = {
      "default": {
      "ENGINE": 'django.db.backends.sqlite3',
      "NAME": str(APPS_DIR.path('database.sqlite'))
    }
}

# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar', )

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}
#Django Debug Toolbar
#------------------------------------------------------------------------------
#INSTALLED_APPS += (
    #'debug_toolbar.apps.DebugToolbarConfig',)

# Show thumbnail generation errors
#-------------------------------------------------------------------------------
THUMBNAIL_DEBUG = True

# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('django_extensions', )

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'


# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}


#--------------------------------------
#to test this run python/python3 manage.py runserver --settings=<projectname>.settings.production
#python manage.py runserver --settings=osopr.settings.development
#python manage.py migrate --settings=osopr.settings.development
