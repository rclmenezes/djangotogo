# Django settings for djangotogo project.
import os
# import dj_database_url
CURRENT_DIR = os.path.join(os.path.dirname( __file__ ), '..')

PRODUCTION = os.environ.get('PRODUCTION', None)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

if PRODUCTION:
    DEBUG = TEMPLATE_DEBUG = False
    COMPRESS_ENABLED = True
    
    # Database
    import dj_database_url
    DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
    
    # CDN
    AWS_STORAGE_BUCKET_NAME = 'djangotogo'
    S3_URL = 'http://djangotogo.s3.amazonaws.com/'
    
    # Static
    STATIC_ROOT = ''
    STATIC_URL = S3_URL + 'static/'
    STATICFILES_DIRS = (
        CURRENT_DIR + "/static",
    )
    
    # Email
    # EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
    #     EMAIL_HOST= 'smtp.sendgrid.net'
    #     EMAIL_PORT = 587
    #     EMAIL_USE_TLS = True
    #     EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
    
else:
    DEBUG = TEMPLATE_DEBUG = True
    COMPRESS_ENABLED = False
    
    # Database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'djangotogo.db',                      # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',     # Not used with sqlite3.
            'HOST': '',                  # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }
    
    # CDN
    AWS_STORAGE_BUCKET_NAME = 'djangotogodev'
    S3_URL = 'http://djangotogodev.s3.amazonaws.com/'
    
    # Static
    STATIC_ROOT =  CURRENT_DIR + "/static"
    STATIC_URL = '/static/'
    #STATICFILES_DIRS = (
    #    CURRENT_DIR + "/static",
    #)
    
    # Email
    # EMAIL_USE_TLS = True
    #     EMAIL_HOST = 'smtp.gmail.com'
    #     EMAIL_HOST_USER = 'APP@gmail.com'
    #     EMAIL_HOST_PASSWORD = 'GMAIL_PASSWORD'
    #     EMAIL_PORT = 587

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = S3_URL + 'media/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder'
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'lolnope'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'djangotogo.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'djangotogo.wsgi.application'

TEMPLATE_DIRS = (
	CURRENT_DIR + '/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'gunicorn',
    'debug_toolbar',
    'compressor'
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# S3 stuff
DEFAULT_FILE_STORAGE = 'djangotogo.s3utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'djangotogo.s3utils.StaticRootS3BotoStorage'
AWS_ACCESS_KEY_ID = 'nope'
AWS_SECRET_ACCESS_KEY = 'nopenopenope'
AWS_PRELOAD_METADATA = True
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_URL = S3_URL
COMPRESS_STORAGE = STATICFILES_STORAGE

INTERNAL_IPS = ('127.0.0.1',)
