
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
