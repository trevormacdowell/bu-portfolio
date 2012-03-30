from settings import *

# Put any settings overrides for the local Vagrant environment here
# (Database, Paths, etc.)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # or 'oracle'.
        'NAME': '/db/bu_portfolio_management_devl.db',                      # Or path to database file if using sqlite3.
#         'USER': '',                      # Not used with sqlite3.
#         'PASSWORD': '',                  # Not used with sqlite3.
#         'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

SOUTH_DATABASE_ADAPTERS = {
    'default': "south.db.sqlite3"
}

DEBUG = True
SERVE_STATIC = True

# since DEBUG and SERVE_STATIC are True, static content will be served by Django's
# staticfiles view anyway, so don't bother with STATIC_ROOT
STATIC_ROOT = ''
STATIC_URL = '/static/'
