"""
WSGI config for foodwast project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""
"""
Configures the WSGI application for the Django project named "foodwast" and sets the 'DJANGO_SETTINGS_MODULE' environment variable.
To enable communication between the web server and the Django application via the WSGI standard interface, while specifying the project's settings module.
"""
# Import the 'os' module to access operating system functionalities
import os
# Import the 'get_wsgi_application' function from 'django.core.wsgi' module
from django.core.wsgi import get_wsgi_application
# Set the 'DJANGO_SETTINGS_MODULE' environment variable to 'foodwast.settings'
# This specifies the settings module that Django should use to configure the project.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodwast.settings')
# Get the WSGI application for the Django project
# The WSGI application is a callable object used by the web server to interact with Django and handle HTTP requests.
application = get_wsgi_application()
