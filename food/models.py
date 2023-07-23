from django.db import models

# Create your models here.


class Donar_Model(models.Model):

    fullname=models.CharField(max_length=40)

    email=models.CharField(max_length=40)

    fooditems=models.CharField(max_length=100)

    address=models.TextField(default="enter the address")

    phone=models.CharField(max_length=20)

    orphanage=models.CharField(max_length=30)

    date=models.DateField()

    def __str__(self):

        return self.fullname


class DonarRegister_Model(models.Model):
    """
    Represents a donor registration.

    Fields:
    - name: CharField with a maximum length of 40 characters, representing the user's name.
    - password: CharField with a maximum length of 40 characters, representing the user's password.
    - email: CharField with a maximum length of 50 characters, representing the user's email.
    - phone: CharField with a maximum length of 20 characters, representing the user's phone number.
    - address: TextField with a default value of "Enter the address", representing the user's address.

    Contracts:
    - Precondition: The length of the name field is less than or equal to 40 characters.
    - Precondition: The length of the password field is less than or equal to 40 characters.
    - Precondition: The length of the email field is less than or equal to 50 characters.
    - Precondition: The length of the phone field is less than or equal to 20 characters.
    - Postcondition: The __str__() method returns the user's name as a string representation of the DonarRegister_Model object.
    """

    name = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.TextField(default="Enter the address")

    def __str__(self):
        """
        Returns a string representation of the DonarRegister_Model object.
        """
        return self.name


class Agent_Model(models.Model):

    name=models.CharField(max_length=40)

    password=models.CharField(max_length=40)

    email=models.CharField(max_length=50)

    phone=models.CharField(max_length=20)

    address=models.TextField(default="Enter the address")

    
    def __str__(self):

        return self.name


class Assign_Model(models.Model):

    cid=models.IntegerField(primary_key=True)
    
    aid=models.IntegerField()

    def __str__(self):

       return self.cid

# Defining the Complaint_Model class which represents a model for complaints
class Complaint_Model(models.Model):

    # Defining a field "name" to store the name of the complainant
    name = models.CharField(max_length=30, default="")

    # Defining a field "message" to store the complaint message
    message = models.TextField(default="Enter the complaint Message")

    # Defining the __str__ method to represent the model instance as a string (name in this case)
    def __str__(self):
        return self.name

# Defining the Suggestion_Model class which represents a model for suggestions
class Suggestion_Model(models.Model):

    # Defining a field "name" to store the name of the person providing the suggestion
    name = models.CharField(max_length=30)

    # Defining a field "message" to store the suggestion message
    message = models.TextField(default="Enter the suggestion Message")

    # Defining the __str__ method to represent the model instance as a string (name in this case)
    def __str__(self):
        return self.name

    

