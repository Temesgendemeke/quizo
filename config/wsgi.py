"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Initialize Django WSGI application
application = get_wsgi_application()

# Configure WhiteNoise to serve static files
application = WhiteNoise(application, root=settings.STATIC_ROOT)

# Serve media files with a unique prefix (e.g., '/media/')
application.add_files(settings.MEDIA_ROOT, prefix=settings.MEDIA_URL.strip("/"))

# For compatibility if other code references `app`
app = application
