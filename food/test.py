# Imports the TestCase class from Django's testing framework.
from django.test import TestCase 
# Imports the DonarRegister_Model, Complaint_Model, Suggestion_Model, and Rating_Model classes from the current app's models.py file.
from .models import DonarRegister_Model,Complaint_Model, Suggestion_Model, Rating_Model
# Imports the reverse function from Django's urls module, used for resolving and generating URLs based on view names.
from django.urls import reverse


# DonarRegister_ModelTest test case for DonarRegister_Model
class DonarRegister_ModelTest(TestCase):
     """
     Code is a test case written in Django for the DonorRegister_Model class. 
     It is designed to test the functionality of the DonorRegister_Model by checking 
     if the name and password attributes are set correctly.
      """
     
def setUp(self):
        # Create a DonarRegister_Model object for testing
        DonarRegister_Model.objects.create(name='vinay',password='vinay123',email='vinay@gmail.com',phone='9999988888',address='vijayawada')

def test_text_content(self):
        # Retrieve the DonarRegister_Model object created in setUp
        donarregister = DonarRegister_Model.objects.get(id=1)
        # Check if the name and password fields are set correctly
        exp_name = f'{donarregister.name}'
        exp_password = f'{donarregister.password}'
        self.assertEqual(exp_name,'vinay')
        self.assertEqual(exp_password,'vinay123')


# DonorPageViewTest test case for testing the view URL
class DonorPageViewTest(TestCase):
    """
    The provided code defines a Django test case named DonorPageViewTest that checks if the view URL '/' (root URL) exists and returns a status code of 200, indicating a successful response.
    The code was implemented to verify that the main page view (root URL '/') is functioning correctly without errors or issues.
    This code is part of the test suite in a Django project and is placed in a test module (usually named tests.py) within the app 
    that contains the views (in the views.py file). It is executed during the development and maintenance process to automatically test the proper configuration and accessibility of the root URL view.
    """

    def setUp(self):
        # Create a DonarRegister_Model object for testing
        DonarRegister_Model.objects.create(name='vinay',password='vinay123',email='vinay@gmail.com',phone='9999988888',address='vijayawada')

    def test_view_url_exits_at_proper_location(self):
        # Test if the view URL exists at the proper location
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)


# Complaint_ModelTest test case for Complaint_Model
class Complaint_ModelTest(TestCase):
    """
    The provided code is a Django test case named Complaint_ModelTest, which tests the functionality of the Complaint_Model class.
    The test case ensures that the name and message attributes of the Complaint_Model instance are correctly set.
    """
    def setUp(self):
        # Create a Complaint_Model object for testing
        Complaint_Model.objects.create(name='vinay',message='There is a problem')

    def test_text_content(self):
        # Retrieve the Complaint_Model object created in setUp
        complaintregister = Complaint_Model.objects.get(id=1)
        # Check if the name and message fields are set correctly
        com_name = f'{complaintregister.name}'
        com_message = f'{complaintregister.message}'
        self.assertEqual(com_name,'vinay')
        self.assertEqual(com_message,'There is a problem')


# Suggestion_ModelTest test case for Suggestion_Model
class Suggestion_ModelTest(TestCase):
    """
    code is a Django test case named Suggestion_ModelTest, designed to test the functionality of the Suggestion_Model class. 
    The test case ensures that the name and message attributes of the Suggestion_Model instance are correctly set.
     """
    def setUp(self):
        # Create a Suggestion_Model object for testing
        Suggestion_Model.objects.create(name='vinay',message='Increase More Services')

    def test_text_content(self):
        # Retrieve the Suggestion_Model object created in setUp
        suggestionregister = Suggestion_Model.objects.get(id=1)
        # Check if the name and message fields are set correctly
        sug_name = f'{suggestionregister.name}'
        sug_message = f'{suggestionregister.message}'
        self.assertEqual(sug_name,'vinay')
        self.assertEqual(sug_message,'Increase More Services')


# Rating_ModelTest test case for Rating_Model
class Rating_ModelTest(TestCase):
    """
    The provided code defines a Django test case named Rating_ModelTest, which tests the functionality of the Rating_Model class. 
    The test case ensures that the name and rating attributes of the Rating_Model instance are correctly set.
    """
    def setUp(self):
        # Create a Rating_Model object for testing
        Rating_Model.objects.create(name='vinay',rating='5')

    def test_text_content(self):
        # Retrieve the Rating_Model object created in setUp
        ratingregister = Rating_Model.objects.get(id=1)
        # Check if the name and rating fields are set correctly
        rate_name = f'{ratingregister.name}'
        rate_rating = f'{ratingregister.rating}'
        self.assertEqual(rate_name,'vinay')
        self.assertEqual(rate_rating,'5')
