from motosmexico.settings.develop import *

DEBUG = False

ALLOWED_HOSTS = ['motosmexico.digimundo.com.mx']

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DIARY_DB_NAME'),
        'USER': os.getenv('DIARY_DB_USER'),
        'PASSWORD': os.getenv('DIARY_DB_PASSWORD'),
        'HOST': os.getenv('DIARY_DB_HOST'),
        'PORT': os.getenv('DIARY_DB_PORT'),
    }
}
