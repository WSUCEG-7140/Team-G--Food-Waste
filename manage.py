#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.
Sets up the entry point for running Django management commands from the command line.
To provide a standardized way to execute Django management commands, handle exceptions, and ensure the correct settings module is used.
The code is placed in the main Python script of a Django project named 'manage.py', used for running various management commands and managing the Django project components via the command line.

"""
# Import the 'os' module to access operating system functionalities
import os

# Import the 'sys' module to access system-specific parameters and functions
import sys

# Define the main function
def main():
    # Set the 'DJANGO_SETTINGS_MODULE' environment variable to 'foodwast.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodwast.settings')

    # Try importing 'execute_from_command_line' from 'django.core.management'
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Raise an ImportError with an informative message if Django is not installed or not available
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Execute the Django management command from the command-line arguments
    execute_from_command_line(sys.argv)

# Check if the script is being run as the main module
if __name__ == '__main__':
    # Call the main function
    main()

