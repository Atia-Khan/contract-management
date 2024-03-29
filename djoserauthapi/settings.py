"""
Django settings for djoserauthapi project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta
# settings.py
from dotenv import load_dotenv
load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-jds14b8=nk4u3zxavy*302s@+u$mj^0vlu3je^0#=h-28jv)b1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'widget_tweaks',
    'djoser',
    'corsheaders',  # Remove the duplicate entry here
    'account',
    'social_django',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'taggit',
    'taggit_autosuggest',
    'folder',
    'file',
]


TAGGIT_TAGS_FROM = 'file.models.File.tags'

X_FRAME_OPTIONS = 'SAMEORIGIN'
CSP_FRAME_ANCESTORS=["http://localhost:8000"]
CSP_DEFAULT_SRC = "'self'"

# Remove the duplicate entry from MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Keep this line
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djoserauthapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],  # Remove the 'build' directory from here
        'DIRS': [ os.path.join(BASE_DIR, 'frontend/build') ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'account.context_processors.frontend_base_url',  

            ],
        },
    },
]

WSGI_APPLICATION = 'djoserauthapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'database',
#         'USER': 'postgres',
#         'PASSWORD': 'password',
#         'HOST': 'localhost'
#     }
# }
SUPABASE_DB_URL = os.environ.get("SUPABASE_DB_URL")
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "postgres",
        'USER': "postgres",
        'PASSWORD': "Atia@54321@12",
        'HOST': "db.tsitkyogfxczaucebjnd.supabase.co",
        'PORT': 5432,
    }
}

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ifrasaleemcsengineer12@gmail.com'
EMAIL_HOST_PASSWORD = 'kjhdgnsgqferexuj'
EMAIL_USE_TLS = True

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = []

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom User Model
AUTH_USER_MODEL = 'account.User'

# JWT Configuration
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend'
)

# JWT Settings
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "UPDATE_LAST_LOGIN": True,
    'AUTH_TOKEN_CLASSES': (
        'rest_framework_simplejwt.tokens.AccessToken',
    )
}

# Djoser Settings
DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE':True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'ACTIVATION_URL':'/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL':True,
    'SEND_CONFIRMATION_EMAIL':True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION':True,
    'PASSWORD_RESET_CONFIRM_URL': 'password-reset/{uid}/{token}',
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,
    'SOCIAL_AUTH_TOKEN_STRATEGY': 'djoser.social.token.jwt.TokenStrategy',
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': ['http://127.0.0.1:8000/google'],
    'TOKEN_MODEL': None,      
    'SERIALIZERS':{
        'user_create': 'account.serializers.UserCreateSerializer',
        'user': 'account.serializers.UserCreateSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    },
    'EMAIL': {
        'activation': 'account.email.ActivationEmail',
        'confirmation': 'account.email.ConfirmationEmail',
        'password_reset': 'account.email.PasswordResetEmail',
        'password_changed_confirmation': 'account.email.PasswordChangedConfirmationEmail',
    },


}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '930640781365-mu80bpifeir239cl06go1653q5q5ieh5.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile', 'openid']
SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ['first_name', 'last_name']

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:3000",

]

# ALLOWED_HOSTS = ['localhost', '127.0.0.1']
ALLOWED_HOSTS = ['.vercel.app', '.now.sh']
# Or * to allow all
ALLOWED_HOSTS = ['*']


CSRF_TRUSTED_ORIGINS = ['http://localhost:3000', 'http://127.0.0.1:3000']

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

# settings.py

FRONTEND_BASE_URL = 'http://localhost:3000'  # Replace with your actual frontend base URL


CORS_ALLOW_CREDENTIALS = True
CSRF_COOKIE_SECURE = False