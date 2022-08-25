"""
Django settings for Tourism project.

Generated by 'django-admin startproject' using Django 3.2.14.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# for img file show 
MEDIA_ROOT = os.path.join(BASE_DIR, '/board/UploadImage/')
MEDIA_URL = '/board/UploadImage/'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.environ.get("DJANGO_SECRET_KEY"))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = str(os.environ.get("DEBUG")) == '1'

ALLOWED_HOSTS = ['127.0.0.1','localhost','kubernetes.docker.internal']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    #accounts app
    'accounts',
    #django-rest-auth
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    'rest_framework_simplejwt.token_blacklist',
    'rest_framework',
    # 'dj_rest_auth',
    # 'dj_rest_auth.registration',
    # cors 
    "corsheaders",
    #django-allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'board',
]
SITE_ID = 1
REST_USE_JWT = True # Whether to use JWT
# JWT_AUTH_COOKIE = 'my-app-auth'  # Cookie Key Value to Call
# JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token' Refresh Token Cookie Key Value (if used)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    "corsheaders.middleware.CorsMiddleware",

    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'Tourism.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Tourism.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DB_USERNAME = os.environ.get("POSTGRES_USERNAME")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_DATABASE = os.environ.get("POSTGRES_DB")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_IS_AVAILABLE = all([
    DB_USERNAME,
    DB_PASSWORD,
    DB_DATABASE,
    DB_HOST,
    DB_PORT
])

if DB_IS_AVAILABLE:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': DB_DATABASE,
            "USER": DB_USERNAME,
            "PASSWORD": DB_PASSWORD,
            "HOST": DB_HOST,
            "PORT": DB_PORT,
        }
    }

REST_FRAMEWORK = {
  # 'DEFAULT_PERMISSION_CLASSES': (
  #     'rest_framework.permissions.IsAuthenticated',
  # ),
	'DEFAULT_AUTHENTICATION_CLASSES' : (
      'rest_framework_simplejwt.authentication.JWTAuthentication',
      'rest_framework.authentication.SessionAuthentication',
      # 'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
  )
}
# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
#     # 'ROTATE_REFRESH_TOKENS': False,
#     # 'BLACKLIST_AFTER_ROTATION' : True,
#     # 'UPDATE_LAST_LOGIN': False,
#     'SIGNING_KEY': 'SECRET',
#     'ALGORITHM': 'HS256',
#     'AUTH_HEADER_TYPES': ('JWT',),
# }

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True, #If set to True, sending a refresh token returns a new access token and a refresh token
    'BLACKLIST_AFTER_ROTATION': True, #If set to True, the existing refresh token will be blacklisted
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer', 'JWT'),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),

    'AUTH_COOKIE': 'access_token',  # Cookie name. Enables cookies if value is set.
    'AUTH_COOKIE_DOMAIN': None,     # A string like "example.com", or None for standard domain cookie.
    'AUTH_COOKIE_SECURE': False,    # Whether the auth cookies should be secure (https:// only).
    'AUTH_COOKIE_HTTP_ONLY' : True, # Http only cookie flag.It's not fetch by javascript.
    'AUTH_COOKIE_PATH': '/',        # The path of the auth cookie.
    'AUTH_COOKIE_SAMESITE': 'Lax',  # Whether to set the flag restricting cookie leaks on cross-site requests. This can be 'Lax', 'Strict', or None to disable the flag.
}

print(DATABASES)
REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")
REDIS_DEFAULT_EXPIRATION = os.environ.get("REDIS_DEFAULT_EXPIRATION")

REDIS_IS_AVAILABLE = all([
    REDIS_HOST,
    REDIS_PORT,
    REDIS_DEFAULT_EXPIRATION,
])

if REDIS_IS_AVAILABLE:
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': f'redis://{REDIS_HOST}:{REDIS_PORT}/',
            'TIMEOUT': REDIS_DEFAULT_EXPIRATION,
            'OPTIONS': {
                'db': '0',
                'parser_class': 'redis.connection.PythonParser',
                'pool_class': 'redis.BlockingConnectionPool',
            }
        }
    }

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = [
'accept',
'accept-encoding',
'authorization',
'content-type',
'dnt',
'origin',
'user-agent',
'x-csrftoken',
'x-requested-with',
]


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{
			"NAME" : "accounts.validators.CustomPasswordValidator",
	},
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = "ko"

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


STATICFILES_DIRS = [
    BASE_DIR/"static",
]

STATIC_ROOT = BASE_DIR/"staticfiles"


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Auth Settings
AUTH_USER_MODEL = 'accounts.User'
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_SIGNUP_REDIRECT_URL ="list"
LOGIN_REDIRECT_URL ="list"
ACCOUNT_LOGOUT_ON_GET =True
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED =True
# ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_FORM_CLASS ="accounts.forms.SignupForm"
ACCOUNT_SESSION_REMEMBER =True
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE =True
# ACCOUNT_EMAIL_VARIFICATION ="optional"  // This part is the default even if you erase it
SESSION_COOKIE_AGE = 60 * 60 * 24
ACCOUNT_CONFIRM_EMAIL_ON_GET=True
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "account_email_confirmation_done"
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "account_email_confirmation_done"
PASSWORD_RESET_TIMEOUT = 60 * 60 * 24 * 3

# Email settings
EMAIL_BACKEND ="django.core.mail.backends.console.EmailBackend"


# if DEBUG:
#     CORS_ALLOW_ALL_ORIGINS = True