import os
from pathlib import Path

# 1. Base Directory Definition
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Security Settings
SECRET_KEY = "django-insecure-v99(ro7r#qj@gm^w_ymmpodlyh2^(vtm512e#4fpc76r_61i*e"
DEBUG = True  # Set to False when you're ready to go live
ALLOWED_HOSTS = ['*'] # Allows Render to access the app

# 3. Application Definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'finance.apps.FinanceConfig',
    'widget_tweaks',   
    'import_export',
]

# 4. Middleware (Fixed WhiteNoise position)
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Correctly placed here
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "FinanceTracker.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "FinanceTracker.wsgi.application"

# 5. Database (Using SQLite for now)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# 6. Static Files Configuration (Fixed Typo)
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"  # Fixed: No more BASE_Path error

STATICFILES_DIRS = [
    BASE_DIR / "static", # Ensure you have a folder named 'static' in your root
]

# This handles the compression and caching of your CSS/JS
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# 7. Other Settings
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
