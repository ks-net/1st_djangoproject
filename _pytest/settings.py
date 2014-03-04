"""
Django settings for pytest project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j*8)a&ah=y6xjmt1gua713u#!k3xbkb7((3g_ld#olb@yu1jk^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    #'django_admin_bootstrapped.bootstrap3',
    #'django_admin_bootstrapped', 
    # you can ommit docs in production sites   
    'django.contrib.admindocs',             
    'django.contrib.admin',   
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_evolution',
    'blog',
    'accommodation',
    'pages',
    'resorts',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #Using the admindocs bookmarklets requires 
    'django.contrib.admindocs.middleware.XViewMiddleware'
)

ROOT_URLCONF = '_pytest.urls'

WSGI_APPLICATION = '_pytest.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'root',
        'PASSWORD': '608505',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#If you define a custom LANGUAGES setting, you can mark the language names as 
#translation strings using the ugettext_lazy() function.
from django.utils.translation import ugettext_lazy as _

LANGUAGES = (
    ('el', _('Greek')),
    ('en', _('English')),
)


#MY CONTEX PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",                           
    "_pytest.context_processors.sitedictionary",  
)

# SITE-WIDE SETTINGS
# TODO: switch to sites
SITE_URL = 'http://localhost:8000'
SITE_NAME = 'My First DjangoProject'
SITE_URL2 = 'http://localhost:8000222'
SITE_NAME2 = '222My First DjangoProject'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/home/ks-net/Documents/Aptana Studio 3 Workspace/_pytest/static',
)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

