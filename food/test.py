# Importing necessary modules for testing
from django.test import TestCase

# Importing the models to be tested
from .models import DonarRegister_Model, Complaint_Model, Suggestion_Model, Rating_Model

# Importing reverse function to generate URLs for testing
from django.urls import reverse

class DonorPageViewTest(TestCase):

    def setUp(self):
        # Preparing test data: Creating a DonarRegister_Model object
        DonarRegister_Model.objects.create(name='vinay', password='vinay123', email='vinay@gmail.com', phone='9999988888', address='vijayawada')

    def test_view_url_exists_at_proper_location(self):
        # Contract: Testing if the view for the specified URL exists and returns a 200 status code
        url = reverse('home')  # Assuming the URL name for the homepage is 'home'
        resp = self.client.get(url)

        # Assertion: Ensuring the view for the specified URL exists and returns a 200 status code
        self.assertEqual(resp.status_code, 200)
