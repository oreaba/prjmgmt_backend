SQL_FILE = '/efs-adm-pm-db-prod/adm-pm.db.sqlite3' # same as .ebextensions/env_variables.config - /efs-adm-pm-db-prod
print('Loading database at: ', SQL_FILE)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': SQL_FILE,
    }
}



CORSE_ALLOWED_ORIGINS = [
    'http://localhost:4200',
    # '*',
]

ALLOWED_HOSTS = [
    '127.0.0.1',
    'adm-pm.me-south-1.elasticbeanstalk.com',
    'www.adm-pm.me-south-1.elasticbeanstalk.com',
    'adm-pm.com',
    'www.adm-pm.com'
]
#-----securing the app session and cookie to be sent only in https connection----------------------
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
#--------------------------------------------------------------------------------------------------

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
