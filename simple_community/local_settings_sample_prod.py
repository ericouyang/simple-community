"""
Sample Production local_settings.py
Usage: copy to local_settings.py and configure for your own usage
"""
from settings import INSTALLED_APPS

SECRET_KEY = 'GENERATE ME AS A LONG RANDOM KEY'

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    '.example.com',
]

# Database (Use MySQL instead of SQLite)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DATABASE NAME',
        'USER': 'USERNAME',
        'PASSWORD': 'PASSWORD',
        'HOST': 'localhost',
    }
}

# compress and minify LESS CSS files

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile} --clean-css'),
)

# Emails (Use SparkPost to send actual emails)

INSTALLED_APPS += ('anymail',)

EMAIL_BACKEND = 'anymail.backends.sparkpost.SparkPostBackend'
ANYMAIL = {
    'SPARKPOST_API_KEY': '',
    'SEND_DEFAULTS': {
        'esp_extra': {
            'transactional': True,
        },
        'track_clicks': True,
        'track_opens': True,
    },
}

DEFAULT_FROM_EMAIL = ''

# Google Analytics

GOOGLE_ANALYTICS_ID = ''
