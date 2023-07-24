# Importing necessary modules for testing
from django.test import TestCase

# Importing the models to be tested
from .models import DonarRegister_Model, Complaint_Model, Suggestion_Model, Rating_Model

# Importing reverse function to generate URLs for testing
from django.urls import reverse

# Defining the test case class that inherits from Django's TestCase
class Suggestion_ModelTest(TestCase):

    # The setUp method runs before each test method is executed.
    # It sets up the initial conditions required for testing.
    def setUp(self):
        # Creating a Suggestion_Model object with name='vinay' and message='Increase More Services'
        Suggestion_Model.objects.create(name='vinay', message='Increase More Services')

    # The test_text_content method tests the content of the Suggestion_Model object.
    def test_text_content(self):
        # Retrieving the Suggestion_Model object created in the setUp method by its id (1 in this case)
        suggestionregister = Suggestion_Model.objects.get(id=1)

        # Extracting the name and message from the Suggestion_Model object
        sug_name = f'{suggestionregister.name}'
        sug_message = f'{suggestionregister.message}'

        # Asserting that the extracted name is 'vinay'
        self.assertEqual(sug_name, 'vinay')

        # Asserting that the extracted message is 'Increase More Services'
        self.assertEqual(sug_message, 'Increase More Services')
