"""
ASGI config for foodwast project.
It exposes the ASGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""
# Import the 'os' module to access operating system functionalities
import os
# Import the 'get_asgi_application' function from 'django.core.asgi' module
from django.core.asgi import get_asgi_application
# Set the 'DJANGO_SETTINGS_MODULE' environment variable to 'foodwast.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodwast.settings')
# Get the ASGI application for the Django project
application = get_asgi_application()
