# Importing the AppConfig class from the django.apps module.
from django import forms
from .models import Donar_Model,Agent_Model,Assign_Model,DonarRegister_Model,Complaint_Model, Suggestion_Model, Rating_Model

# Donar_ModelCreate form for creating Donar_Model objects
class Donar_ModelCreate(forms.ModelForm):
    """
        Code generates the Donar_ModelCreate Django form, which makes it simple to handle and save data in the
        Donar_Model database. In order to efficiently receive and manage donor data, the form is made to be 
        utilised in a web application.

        Attributes:
        orphanes (list): Choices for orphanages.
        fooditems (list): Choices for food items.
    """
    # List of choices for orphanages. Each choice is represented by a tuple (value, display_name).
    orphanes = [
        ('vij', 'Vijayawada'),
        ('Gun', 'Gunturu'),
      ]
    # List of choices for food items. Each choice is represented by a tuple (value, display_name).
    fooditems = [

      ('Rice and Curries', 'Rice and Curries'),
      ('Chapathi','Chapathi')
    ]
    # Full Name field with a TextInput widget and form-control class for styling
    fullname=forms.CharField(label='Full Name',widget=forms.TextInput(attrs={'class':"form-control"}))
    # Email field with a TextInput widget and form-control class for styling
    email=forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': "form-control"}))
    # Food Items field with a TextInput widget and form-control class for styling
    fooditems=forms.CharField(label='Food Items', widget=forms.TextInput(attrs={'class': "form-control"}))
    # Address field with a Textarea widget and form-control class for styling
    address = forms.CharField(label='Address',widget=forms.Textarea(attrs={'class': "form-control"}))
    # Phone field with a TextInput widget and form-control class for styling
    phone=forms.CharField(label='Phone', widget=forms.TextInput(attrs={'class': "form-control"}))
    # Orphanages field with a Select widget and form-control class for styling, using the orphanes choices
    orphanage = forms.ChoiceField(label='Orphanages', widget=forms.Select(attrs={'class': "form-control"}), choices=orphanes)
    # Date Of Donation field with a DateInput widget and form-control class for styling
    date=forms.CharField(label='Date Of Donation', widget=forms.widgets.DateInput(attrs={'class': "form-control",'type':"date"}))
  

    class Meta:
        """
        Module defines a user-friendly form to collect donor data, leveraging Django's powerful ModelForm feature to directly
        interact with the Donar_Model database model.This integration ensures data consistency and validation, making it 
        efficient for users to input their details and for developers to handle and store donor information in the application.
        """
        # Specify the model to use for this form
        model=Donar_Model
        # Include all fields from the model
        fields='__all__'


# Complaint_ModelCreate form for creating Complaint_Model objects
class Complaint_ModelCreate(forms.ModelForm):
  """
  Class creates a Django ModelForm named Complaint_ModelCreate for capturing complaint information.
  It is used to simplify the process of handling and storing complaint data as instances of the Complaint_Model in the database,
  providing a convenient way for users to submit their complaints through a web form.
  """
  # Name field with a TextInput widget and form-control class for styling
  name=forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':"form-control"}))
  # Message field with a Textarea widget and form-control class for styling
  message = forms.CharField(label='Message',widget=forms.Textarea(attrs={'class': "form-control"}))
    
     
  class Meta:
    """
    Implements a Django ModelForm named Complaint_ModelCreate to handle complaint submissions. 
    The form is automatically generated based on the fields of the Complaint_Model and is utilized 
    in web applications to simplify the process of collecting and managing complaint data.
    """
    # Specify the model to use for this form
    model = Complaint_Model
    # Include all fields from the model
    fields = '__all__'
    

# Suggestion_ModelCreate form for creating Suggestion_Model objects
class Suggestion_ModelCreate(forms.ModelForm):
  """
  Module creates a Django ModelForm named Suggestion_ModelCreate to facilitate the submission of user suggestions.
  The form allows users to input their name and suggestion message and automatically maps these inputs to the corresponding 
  fields in the Suggestion_Model. It simplifies the process of capturing and managing suggestion data in the web application.
  """
  # Name field with a TextInput widget and form-control class for styling
  name=forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':"form-control"}))
  # Message field with a Textarea widget and form-control class for styling
  message = forms.CharField(label='Message',widget=forms.Textarea(attrs={'class': "form-control"}))
    

  class Meta: 
    """
    Django ModelForm named Suggestion_ModelCreate to handle suggestion submissions.
    The form is automatically generated based on the fields of the Suggestion_Model 
    and is used in web applications to simplify the process of collecting and managing suggestion data.
    """
    # Specify the model to use for this form
    model = Suggestion_Model
    # Specify the model to use for this form
    fields = '__all__'

# Rating_ModelCreate form for creating Rating_Model objects
class Rating_ModelCreate(forms.ModelForm):
  """
  To record user ratings, a Django ModelForm called Rating_ModelCreate was used.
  Users can fill out the form by entering their name and choosing a rating from a 
  list of options. It streamlines the procedure for collecting and maintaining rating 
  data in the web application by automatically mapping these inputs to the relevant fields in the Rating_Model.
  
  Attributes:
  r_choice (list): Choices for ratings.

  """
  r_choice = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
      ]

  # Name field with a TextInput widget and form-control class for styling
  name=forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':"form-control"}))
  # Name field with a TextInput widget and form-control class for styling
  rating = forms.ChoiceField(label='Rating', widget=forms.Select(attrs={'class': "form-control"}), choices=r_choice)
   

    
class Meta:
    """
    This code implements a Django ModelForm named Rating_ModelCreate for capturing user ratings. 
    The form allows users to provide their name and select a rating from a predefined set of choices. 
    It is used in web applications to simplify the process of collecting and managing rating data in the system, 
    mapping the data to instances of the Rating_Model in the database.
    """
    # Specify the model to use for this form
    model = Rating_Model
    # Include all fields from the model
    fields = '__all__'



# DonarRegister_ModelCreate form for creating DonarRegister_Model objects
class DonarRegister_ModelCreate(forms.ModelForm):
  """
  Django ModelForm named DonarRegister_ModelCreate for capturing donor registration details. 
  The form allows users to input their name, password, email, phone number, and address, and 
  automatically maps these inputs to the corresponding fields in the DonarRegister_Model. 
  It simplifies the process of capturing and managing donor registration data in the web application.
  """
  # User Name field with a TextInput widget and form-control class for styling
  name=forms.CharField(label='User Name',widget=forms.TextInput(attrs={'class':"form-control"}))
  # Password field with a PasswordInput widget and form-control class for styling
  password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':"form-control"}))
  # Email field with a TextInput widget and form-control class for styling
  email=forms.CharField(label='Email',widget=forms.TextInput(attrs={'class':"form-control"}))
  # Phone field with a TextInput widget and form-control class for styling
  phone=forms.CharField(label='Phone',widget=forms.TextInput(attrs={'class':"form-control"}))
  # Address field with a Textarea widget and form-control class for styling
  address = forms.CharField(label='Address',widget=forms.Textarea(attrs={'class': "form-control"}))
   

  class Meta:
        """
        DonarRegister_ModelCreate for capturing donor registration details. 
        The form allows users to provide their name, password, email, phone number, 
        and address, automatically mapping these inputs to the corresponding fields in the DonarRegister_Model. 
        It is used in web applications to simplify the process of collecting and managing donor registration data, 
        storing it as instances of the DonarRegister_Model in the database.
        """
        # Specify the model to use for this form
        model=DonarRegister_Model
        # Include all fields from the model
        fields='__all__'

# Agent_ModelCreate form for creating Agent_Model objects
class Agent_ModelCreate(forms.ModelForm):
  """
  Agent_ModelCreate for capturing agent registration details. 
  The form allows users to input their name, password, email, phone number, and address, and automatically maps these 
  inputs to the corresponding fields in the Agent_Model. It simplifies the process of capturing and managing agent registration 
  data in the web application.
  """
  # User Name field with a TextInput widget and form-control class for styling
  name=forms.CharField(label='User Name',widget=forms.TextInput(attrs={'class':"form-control"}))
  # Password field with a TextInput widget and form-control class for styling
  password=forms.CharField(label='Password',widget=forms.TextInput(attrs={'class':"form-control"}))
  # Email field with a TextInput widget and form-control class for styling
  email=forms.CharField(label='Email',widget=forms.TextInput(attrs={'class':"form-control"}))
  # Phone field with a TextInput widget and form-control class for styling
  phone=forms.CharField(label='Phone',widget=forms.TextInput(attrs={'class':"form-control"}))
  # Address field with a Textarea widget and form-control class for styling
  address = forms.CharField(label='Address',widget=forms.Textarea(attrs={'class': "form-control"}))
   

  class Meta:
        """
        This code implements a Django ModelForm named Agent_ModelCreate for capturing agent registration details. 
        The form allows users to provide their name, password, email, phone number, and address, automatically mapping 
        these inputs to the corresponding fields in the Agent_Model. It is used in web applications to simplify the process
          of collecting and managing agent registration data, storing it as instances of the Agent_Model in the database.
        """
        # Specify the model to use for this form
        model=Agent_Model
        # Include all fields from the model
        fields='__all__'


# Assign_ModelCreate form for creating Assign_Model objects
class Assign_ModelCreate(forms.ModelForm):
  """
  Assign_ModelCreate for capturing agent assignment details. The form allows users to input customer ID and agent ID, and 
  automatically maps these inputs to the corresponding fields in the Assign_Model. It simplifies the process of capturing 
  and managing agent assignment data in the web application.
  """
  # Customer Id field with a TextInput widget and form-control class for styling
  cid=forms.IntegerField(label='Customer Id',widget=forms.TextInput(attrs={'class':"form-control"}))
  # Customer Id field with a TextInput widget and form-control class for styling
  aid=forms.IntegerField(label='Agent Id',widget=forms.TextInput(attrs={'class':"form-control"}))
  
  class Meta:
    """
    Assign_ModelCreate for capturing agent assignment details. The form allows users to provide customer ID 
    and agent ID, automatically mapping these inputs to the corresponding fields in the Assign_Model. It is 
    used in web applications to simplify the process of collecting and managing agent assignment data, storing 
    it as instances of the Assign_Model in the database.
    """
    # Specify the model to use for this form
    model=Assign_Model
    # Include all fields from the model
    fields='__all__'


