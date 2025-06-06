from .base import *

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('HOST'),
        'PORT': config('PORT'),


    }
}

