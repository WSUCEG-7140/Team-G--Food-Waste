# Importing necessary modules for testing
from django.test import TestCase

# Importing the models to be tested
from .models import DonarRegister_Model, Complaint_Model, Suggestion_Model, Rating_Model

# Importing reverse function to generate URLs for testing
from django.urls import reverse


from django.test import TestCase
from myapp.models import Rating_Model

class Rating_ModelTest(TestCase):

    def setUp(self):
        # Preparing test data: Creating a Rating_Model object
        Rating_Model.objects.create(name='vinay', rating='5')

    def test_text_content(self):
        # Retrieving the Rating_Model object created in setUp
        ratingregister = Rating_Model.objects.get(id=1)

        # Contract: Testing the name and rating attributes of the Rating_Model object
        # Expected name and rating values are defined based on the setUp data
        rate_name = f'{ratingregister.name}'
        rate_rating = f'{ratingregister.rating}'

        # Assertion: Ensuring the name and rating values match the expected values
        self.assertEqual(rate_name, 'vinay')
        self.assertEqual(rate_rating, '5')

