"""
Code facilitates the customization of settings and behavior for the 'food' app by 
defining a custom AppConfig class. It helps keep the app-specific configurations 
separate from the project-wide settings, promoting modularity and maintainability 
in Django projects.
"""

# Importing the AppConfig class from the django.apps module.
from django.apps import AppConfig

# Defining a new class named 'FoodConfig' that inherits from AppConfig.
class FoodConfig(AppConfig):

    # Setting the 'name' attribute of the class to 'food'.
    name = 'food'
