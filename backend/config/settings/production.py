import os

from .base import *  # noqa

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = [os.environ.get("PRODUCTION_HOST")]


# White Noise configuration - http://whitenoise.evans.io/en/stable/django.html
INSTALLED_APPS.extend(["whitenoise.runserver_nostatic"])  # noqa F405

# Must insert after SecurityMiddleware, which is first in settings/common.py
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")  # noqa F405

TEMPLATES[0]["DIRS"] = [os.path.join(BASE_DIR, "../", "frontend", "build")]  # noqa F405

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "../", "frontend", "build", "static")  # noqa F405
]  # noqa F405
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  # noqa F405

STATIC_URL = "/static/"
WHITENOISE_ROOT = os.path.join(
    BASE_DIR, "../", "frontend", "build", "root"  # noqa F405
)  # noqa F405
