#base.py
# [1] IMPORTS
#-----------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals
from django.core.urlresolvers import reverse_lazy
import environ

#[2] PATH CONFIGURATION
#-------------------------------------------------------------------------------
ROOT_DIR = environ.Path(__file__) - 3  # (/a/b/myfile.py - 3 = /)
APPS_DIR = ROOT_DIR.path('osopr')

env = environ.Env()

#[3]TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            str(APPS_DIR.path('templates')),
            # insert more TEMPLATE_DIRS here

        ],
        #'APP_DIRS': True,
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            #'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # Your stuff: custom template context processors go here
            ],
        },
    },
]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# [4] SECURITY WARNING: keep the secret key used in production secret!
#-----------------------------------------------------------------------
SECRET_KEY = ["SECRET_KEY"]


#[5] HOST CONFIGURATION
#-----------------------------------------------------
ALLOWED_HOSTS = []

#------------------------------------------------------
# [6] APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin
    'django.contrib.admin',
)
THIRD_PARTY_APPS = (
    'crispy_forms',  # Form layouts
    'authtools',
    'easy_thumbnails',
    'youtube_thumbnail',
    #'allauth',  # registration
    #'allauth.account',  # registration
    #'allauth.socialaccount',  # registration
     # ... include the providers you want to enable:
    # 'allauth.socialaccount.providers.amazon',
    # 'allauth.socialaccount.providers.angellist',
    # 'allauth.socialaccount.providers.bitbucket',
    # 'allauth.socialaccount.providers.bitbucket_oauth2',
    # 'allauth.socialaccount.providers.bitly',
    # 'allauth.socialaccount.providers.coinbase',
    # 'allauth.socialaccount.providers.dropbox',
    # 'allauth.socialaccount.providers.dropbox_oauth2',
    # 'allauth.socialaccount.providers.edmodo',
    # 'allauth.socialaccount.providers.evernote',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.flickr',
    # 'allauth.socialaccount.providers.feedly',
    # 'allauth.socialaccount.providers.fxa',
    # 'allauth.socialaccount.providers.github',
    # 'allauth.socialaccount.providers.gitlab',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.hubic',
    # 'allauth.socialaccount.providers.instagram',
    # 'allauth.socialaccount.providers.linkedin',
    # 'allauth.socialaccount.providers.linkedin_oauth2',
    # 'allauth.socialaccount.providers.odnoklassniki',
    # 'allauth.socialaccount.providers.openid',
    # 'allauth.socialaccount.providers.persona',
    # 'allauth.socialaccount.providers.pinterest',
    # 'allauth.socialaccount.providers.reddit',
    # 'allauth.socialaccount.providers.soundcloud',
    # 'allauth.socialaccount.providers.spotify',
    # 'allauth.socialaccount.providers.stackexchange',
    # 'allauth.socialaccount.providers.stripe',
    # 'allauth.socialaccount.providers.tumblr',
    # 'allauth.socialaccount.providers.twitch',
    # 'allauth.socialaccount.providers.twitter',
    # 'allauth.socialaccount.providers.untappd',
    # 'allauth.socialaccount.providers.vimeo',
    # 'allauth.socialaccount.providers.vk',
    # 'allauth.socialaccount.providers.weibo',
    # 'allauth.socialaccount.providers.xing',
    )

# Apps specific for this project go here
#---------------------------------------
LOCAL_APPS = (
    #'osopr.users',  # custom users app
    #'users',  # custom users app
    # Your stuff: custom apps go here
    
    'blog2',
    
    #'profiles',
    #'accounts',

)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# [7] MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE_CLASSES = [
    # Make sure djangosecure.middleware.SecurityMiddleware is listed first
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# [8] MIGRATIONS CONFIGURATION
# ------------------------------------------------------------------------------
#MIGRATION_MODULES = {
#'sites': 'osopr.contrib.sites.migrations'
#}

#[9] DEBUG CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)

#[10] FIXTURE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    str(APPS_DIR.path('fixtures')),
)

#[11]EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

#[12] MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
# ------------------------------------------------------------------------------
ADMINS = (
    ("""janam""", 'songola@hotmail.com'),
)

#----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers

MANAGERS = ADMINS


#[13] URL Configuration
#----------------------
ROOT_URLCONF = 'osopr.urls'

#[14] WSGI CONFIGURATION
#-----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'osopr.wsgi.application'


##[15] DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    'default': env.db("DATABASE_URL", default="postgres:///osopr"),

#test db
#---------------------------------------------
    'extra': env.db('SQLITE_URL', default="sqlite:///db.sqlite3")
}


DATABASES['default']['ATOMIC_REQUESTS'] = True


# [16] Password validation
#-----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


#[18]INTERNATIONALIZATION -CONFIGURATION
#------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.9/topics/i18n/
# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.

# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'Africa/Nairobi'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True



#[19]MIGRATIONS CONFIGURATION
# ------------------------------------------------------------------------------
#MIGRATION_MODULES = {
    #'sites': 'oyomni5.contrib.sites.migrations'
#}


#[20] STATIC FILES CONFIGURATION
# ------------------------------------------------------------------------------
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

 #STATIC ROOT CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR('collected_staticfiles'))

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    str(APPS_DIR.path('static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR('media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

#[21] AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    #'allauth.account.auth_backends.AuthenticationBackend',
)

# Some really nice defaults
#--------------------------
#ACCOUNT_AUTHENTICATION_METHOD = 'username'
#ACCOUNT_EMAIL_REQUIRED = True
#ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
#ACCOUNT_ADAPTER = 'users.adapter.AccountAdapter'
#OCIALACCOUNT_ADAPTER = 'users.adapter.SocialAccountAdapter'
#ACCOUNT_ALLOW_REGISTRATION = True
#ACCOUNT_USER_MODEL_USERNAME_FIELD ='username'

# Custom user app defaults
# Select the correct user model
#------------------------------
#AUTH_USER_MODEL = 'users.User'
#LOGIN_REDIRECT_URL = 'users:redirect'
#LOGIN_URL = 'account_login'


#[22] BOOTSTRAP CONFIGURATION
# See: http://django-crispy-forms.readthedocs.org/en/latest/install.html#template-packs
#----------------------------------------------
# Crispy Form Theme - Bootstrap 3
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# For Bootstrap 3, change error alert to 'danger'
from django.contrib import messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

#[23] AUTHENTICATION CONFIGURATION
#Arun inspired
# Authentication Settings
#---------------------------------------------------------
AUTH_USER_MODEL = 'authtools.User'
LOGIN_REDIRECT_URL = reverse_lazy("profiles:show_self")
LOGIN_URL = reverse_lazy("accounts:login")

THUMBNAIL_EXTENSION = 'jpg'     # Or any extn for your thumbnails

#--------------------------------------------------

#[24] SLUGLIFIER
#-------------------------------------------------

AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'

#[25] CELERY CONFIGURATION
#-------------------------
INSTALLED_APPS += ('osopr.taskapp.celery.CeleryConfig',)
# if you are not using the django database broker (e.g. rabbitmq, redis, memcached), you can remove the next line.
#--------------------------------------------------------
INSTALLED_APPS += ('kombu.transport.django',)
BROKER_URL = env("CELERY_BROKER_URL", default='django://')

#[26] DJANGO-ADMIN CONFIGURATION
#-----------------------------------------
# Location of root django.contrib.admin URL, use {% url 'admin:index' %}
ADMIN_URL = r'^admin/'


#[26] CUSTOM-PROJECT SPECIFIC CONFIGURATION
#-------------------------------------------------
# Your common stuff: Below this line define 3rd party library settings






