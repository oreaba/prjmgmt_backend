from .base import BASE_DIR

SQL_FILE = f'{BASE_DIR}/local_db/adm-pm.db.sqlite3'
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
]



DEBUG = True
