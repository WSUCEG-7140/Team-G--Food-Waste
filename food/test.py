# Importing necessary modules for testing
from django.test import TestCase

# Importing the models to be tested
from .models import DonarRegister_Model, Complaint_Model, Suggestion_Model, Rating_Model

# Importing reverse function to generate URLs for testing
from django.urls import reverse

# Defining the test case class that inherits from Django's TestCase
class Complaint_ModelTest(TestCase):

    # The setUp method runs before each test method is executed.
    # It sets up the initial conditions required for testing.
    def setUp(self):
        # Creating a Complaint_Model object with name='vinay' and message='There is a problem'
        Complaint_Model.objects.create(name='vinay', message='There is a problem')

    # The test_text_content method tests the content of the Complaint_Model object.
    def test_text_content(self):
        # Retrieving the Complaint_Model object created in the setUp method by its id (1 in this case)
        complaintregister = Complaint_Model.objects.get(id=1)

        # Extracting the name and message from the Complaint_Model object
        com_name = f'{complaintregister.name}'
        com_message = f'{complaintregister.message}'

        # Asserting that the extracted name is 'vinay'
        self.assertEqual(com_name, 'vinay')

        # Asserting that the extracted message is 'There is a problem'
        self.assertEqual(com_message, 'There is a problem')
