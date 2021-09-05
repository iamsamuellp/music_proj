# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hec$of4b39wv8mjje+uq=_)ou6jahd_hp5y4^6z*o%tb+jpgu*'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
  'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library',
        'USER': 'root',
        'PASSWORD': 'Thispassword1',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
