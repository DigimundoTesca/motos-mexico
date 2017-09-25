from motosmexico.settings.develop import *

DEBUG = False

# ALLOWED_HOSTS = ['motosmexico.digimundo.com.mx', 'motosmexico-env-dev.us-west-2.elasticbenstalk.com']
ALLOWED_HOSTS = ['*']

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('MOTOS_MEXICO_DB_NAME'),
        'USER': os.getenv('MOTOS_MEXICO_DB_USER'),
        'PASSWORD': os.getenv('MOTOS_MEXICO_DB_PASSWORD'),
        'HOST': os.getenv('MOTOS_MEXICO_DB_HOST'),
        'PORT': os.getenv('MOTOS_MEXICO_DB_PORT'),
    }
}

# AWS STATICS
AWS_HEADERS = {
    'Expires': 'Thu, 15 Apr 2099 20:00:00 GMT',
    'Cache-Control': 'max-age=956080000',
}

STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'

AWS_STORAGE_BUCKET_NAME = os.getenv('MOTOS_MEXICO_S3_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = os.getenv('MOTOS_MEXICO_S3_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('MOTOS_MEXICO_S3_SECRET_ACCESS_KEY')

STATICFILES_STORAGE = 'custom_storages.StaticStorage'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
AWS_S3_CUSTOM_DOMAIN = '%s.s3-us-west-2.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_SECURE_URLS = False

AWS_S3_CALLING_FORMAT = ProtocolIndependentOrdinaryCallingFormat()
S3Connection.DefaultHost = 's3-us-west-2.amazonaws.com'

STATIC_URL = "http://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
MEDIA_URL = "http://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
