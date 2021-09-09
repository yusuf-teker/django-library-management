
from pathlib import Path
import os
import environ
env = environ.Env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
environ.Env.read_env(os.path.join(BASE_DIR,'.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')





# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'library',
    'crispy_forms',
    'storages'
   
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases






# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR/"static"]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media/')

#AUTH_USER_MODEL = 'account.CustomUserModel'
#AUTH_USER_MODEL = 'users.CustomUser'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

#gmail_send/settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'y.teker.1907.1907@gmail.com'
EMAIL_HOST_PASSWORD = env('EMAIL_PASSWORD') #past the key or password app here
EMAIL_PORT = 587
EMAIL_USE_TLS  = True
DEFAULT_FROM_EMAIL = 'y.teker.1907.1907@gmail.com'

LOGIN_REDIRECT_URL = '/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers':False,
    'formatters': { 
        'basicCustom': {
            'format':'{asctime} {levelname} {message} {name}',
            'style': '{'
        }
    },
    'handlers':{
        'console':{
            'class':'logging.StreamHandler'
        },
        'file':{ 
            'class': 'logging.FileHandler',
            'filename': 'logs/borrow_demand.log',
            'formatter': 'basicCustom'
        },
        'file2':{ 
            'class': 'logging.FileHandler',
            'filename': 'logs/return_demand.log',
            'formatter': 'basicCustom'
        },
        'file3':{ 
            'class': 'logging.FileHandler',
            'filename': 'logs/extend_demand.log',
            'formatter': 'basicCustom'
        }
    },    
    'loggers': {
        'borrow_demand': {
            'handlers': ['console','file'],
            'level': 'INFO'
        },
        'return_demand': {
            'handlers': ['console', 'file2'],
            'level': 'INFO'
        },
        'extend_demand': {
            'handlers': ['console', 'file3'],
            'level': 'INFO'
        }
    }
}

