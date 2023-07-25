from django import forms

from .models import Donar_Model,Agent_Model,Assign_Model,DonarRegister_Model


class Donar_ModelCreate(forms.ModelForm):

    orphanes = [
        ('vij', 'Vijayawada'),
        ('Gun', 'Gunturu'),
      ]

    fullname=forms.CharField(label='Full Name',widget=forms.TextInput(attrs={'class':"form-control"}))
    
    email=forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': "form-control"}))
  
    fooditems=forms.CharField(label='Food Items', widget=forms.TextInput(attrs={'class': "form-control"}))
  
    address = forms.CharField(label='Address',widget=forms.Textarea(attrs={'class': "form-control"}))
    
    phone=forms.CharField(label='Phone', widget=forms.TextInput(attrs={'class': "form-control"}))
    
    orphanage = forms.ChoiceField(label='Orphanages', widget=forms.Select(attrs={'class': "form-control"}), choices=orphanes)
   
    date=forms.CharField(label='Date Of Donation', widget=forms.widgets.DateInput(attrs={'class': "form-control",'type':"date"}))
  
    class Meta:

        model=Donar_Model

        fields='__all__'


class DonarRegister_ModelCreate(forms.ModelForm):
    """
    A form for creating a donor registration.

    Fields:
    - name: CharField for the user's name.
    - password: CharField for the user's password.
    - email: CharField for the user's email.
    - phone: CharField for the user's phone number.
    - address: CharField for the user's address.

    Contracts:
    - Precondition: The 'class' attribute of the form input elements is set to "form-control".
    - Postcondition: A new instance of DonarRegister_Model is created if the form is valid and saved to the database.
    """

    name = forms.CharField(
        label='User Name',
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    phone = forms.CharField(
        label='Phone',
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    address = forms.CharField(
        label='Address',
        widget=forms.Textarea(attrs={'class': "form-control"})
    )

    class Meta:
        model = DonarRegister_Model
        fields = '__all__'


class Agent_ModelCreate(forms.ModelForm):

  name=forms.CharField(label='User Name',widget=forms.TextInput(attrs={'class':"form-control"}))
    
  password=forms.CharField(label='Password',widget=forms.TextInput(attrs={'class':"form-control"}))
  
  email=forms.CharField(label='Email',widget=forms.TextInput(attrs={'class':"form-control"}))
  
  phone=forms.CharField(label='Phone',widget=forms.TextInput(attrs={'class':"form-control"}))
  
  address = forms.CharField(label='Address',widget=forms.Textarea(attrs={'class': "form-control"}))
   

  class Meta:

        model=Agent_Model

        fields='__all__'

class Assign_ModelCreate(forms.ModelForm):

  cid=forms.IntegerField(label='Customer Id',widget=forms.TextInput(attrs={'class':"form-control"}))
  
  aid=forms.IntegerField(label='Agent Id',widget=forms.TextInput(attrs={'class':"form-control"}))
  
  class Meta:

    model=Assign_Model

    fields='__all__'

# Defining the Complaint_ModelCreate form for creating complaints
class Complaint_ModelCreate(forms.ModelForm):
    # Defining a field "name" to store the name of the complainant
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': "form-control"}))

    # Defining a field "message" to store the complaint message
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': "form-control"}))

    # Meta class to associate the form with the Complaint_Model model and specify the fields to be included
    class Meta:
        model = Complaint_Model
        fields = '__all__'

# Defining the Suggestion_ModelCreate form for creating suggestions
class Suggestion_ModelCreate(forms.ModelForm):
    # Defining a field "name" to store the name of the person providing the suggestion
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': "form-control"}))

    # Defining a field "message" to store the suggestion message
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': "form-control"}))

    # Meta class to associate the form with the Suggestion_Model model and specify the fields to be included
    class Meta:
        model = Suggestion_Model
        fields = '__all__'




