# Importing necessary modules for testing
from django.test import TestCase

# Importing the models to be tested
from .models import DonarRegister_Model, Complaint_Model, Suggestion_Model, Rating_Model

# Importing reverse function to generate URLs for testing
from django.urls import reverse

from django.test import TestCase
from myapp.models import DonarRegister_Model

class DonarRegister_ModelTest(TestCase):

    def setUp(self):
        # Preparing test data: Creating a DonarRegister_Model object
        DonarRegister_Model.objects.create(name='vinay', password='vinay123', email='vinay@gmail.com', phone='9999988888', address='vijayawada')

    def test_text_content(self):
        # Retrieving the DonarRegister_Model object created in setUp
        donarregister = DonarRegister_Model.objects.get(id=1)

        # Contract: Testing the name and password attributes of the DonarRegister_Model object
        # Expected name and password values are defined based on the setUp data
        exp_name = f'{donarregister.name}'
        exp_password = f'{donarregister.password}'

        # Assertion: Ensuring the name and password values match the expected values
        self.assertEqual(exp_name, 'vinay')
        self.assertEqual(exp_password, 'vinay123')

