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

# Emails (Use Mandrill to send actual emails)

INSTALLED_APPS += ('djrill',)

EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'
MANDRILL_API_KEY = ''

# Google Analytics

GOOGLE_ANALYTICS_ID = ''
