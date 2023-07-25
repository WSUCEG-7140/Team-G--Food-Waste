
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


from django.test import TestCase 

from .models import DonarRegister_Model,Complaint_Model, Suggestion_Model, Rating_Model

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

