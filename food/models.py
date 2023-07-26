# Imports the models module from Django, which provides tools for defining and interacting with database models.
from django.db import models

# Donar_Model represents donors' information
class Donar_Model(models.Model):
    """
    Donar_Model to store donor information related to food donations for orphanages. 
    The model is used in a web application to manage and interact with donor data, allowing 
    the application to handle donor records efficiently.
    Attributes:
        fullname (str): Full name of the donor.
        email (str): Email address of the donor.
        fooditems (str): Food items donated by the donor.
        foodpicture (ImageField): Image of the donated food items (optional).
        address (str): Address of the donor.
        phone (str): Phone number of the donor.
        orphanage (str): Name of the orphanage where the donation is made.
        date (date): Date of the donation.
    """
    # Full name field with a maximum length of 40 characters
    fullname=models.CharField(max_length=40)
    # Email field with a maximum length of 40 characters
    email=models.CharField(max_length=40)
    # Food items field with a maximum length of 100 characters
    fooditems=models.CharField(max_length=100)
    # ImageField to store the image of the donated food items (optional)
    foodpicture = models.ImageField(default="")
    # Address field with a default value "enter the address" for new donors
    address=models.TextField(default="enter the address")
    # Phone field with a maximum length of 20 characters
    phone=models.CharField(max_length=20)
    # Orphanage field with a maximum length of 30 characters
    orphanage=models.CharField(max_length=30)
    # Date field to store the date of the donation
    date=models.DateField()
    
    def __str__(self):
    # This method is used to represent the object as a string.
    # It is intended to provide a human-readable string representation of the object.
        return self.fullname


# DonarRegister_Model represents registered donors
class DonarRegister_Model(models.Model):
    """
    DonarRegister_Model to store information about registered donors. 
    The model is used in a web application to manage and interact with 
    donor registration data, allowing the application to handle user accounts 
    and profiles efficiently.

    Attributes:
        name (str): User name of the registered donor.
        password (str): Password for the donor account.
        email (str): Email address of the registered donor.
        phone (str): Phone number of the registered donor.
        address (str): Address of the registered donor.
    """
    # User name field with a maximum length of 40 characters
    name=models.CharField(max_length=40)
    # Password field with a maximum length of 40 characters
    password=models.CharField(max_length=40)
    # Email field with a maximum length of 50 characters
    email=models.CharField(max_length=50)
    # Phone field with a maximum length of 20 characters
    phone=models.CharField(max_length=20)
    # Address field with a default value "Enter the address" for new donors
    address=models.TextField(default="Enter the address")

    def __str__(self):
        # This method returns the string representation of the object based on its 'name' attribute.
        return self.name


class Agent_Model(models.Model):
    """
    Code implements a Django model named Agent_Model to store information about agents. 
    The model is used in a web application to manage and interact with agent data, allowing 
    the application to handle agent accounts and profiles efficiently.
    Attributes:
        name (str): User name of the agent.
        password (str): Password for the agent account.
        email (str): Email address of the agent.
        phone (str): Phone number of the agent.
        address (str): Address of the agent.
    """
    # User name field with a maximum length of 40 characters
    name=models.CharField(max_length=40)
    # Password field with a maximum length of 40 characters
    password=models.CharField(max_length=40)
    # Email field with a maximum length of 50 characters
    email=models.CharField(max_length=50)
    # Phone field with a maximum length of 20 characters
    phone=models.CharField(max_length=20)
    # Address field with a default value "Enter the address" for new agents
    address=models.TextField(default="Enter the address")

    def __str__(self):
        # This method returns the string representation of the object based on its 'name' attribute.
        return self.name


# Assign_Model represents the assignment of agents to customers
class Assign_Model(models.Model):
    """
    Django model named Assign_Model to represent the assignment of agents to customers. 
    The model is used in a web application to manage and interact with agent-customer 
    assignment data, ensuring that the correct agents are associated with their respective customers.
     Attributes:
        cid (int): Customer ID.
        aid (int): Agent ID.
    """
    # Customer ID field with primary key constraint
    cid=models.IntegerField(primary_key=True)
    # Agent ID field
    aid=models.IntegerField()

    def __str__(self):
    # This method returns the string representation of the object, which is the 'cid' attribute converted to a string.
        return self.cid
    

# Complaint_Model represents customer complaints
class Complaint_Model(models.Model):
    """
    code implements a Django model named Complaint_Model to represent and store customer complaints. 
    The model is used in a web application to manage and interact with complaint data, enabling the application to handle and resolve customer concerns efficiently.
    Attributes:
        name (str): Name of the customer making the complaint.
        message (str): Complaint message from the customer.
    """
    # Name field with a maximum length of 30 characters and a default value ""
    name = models.CharField(max_length=30,default="")
    # Complaint message field with a default value "Enter the complaint Message"

    message = models.TextField(default = "Enter the complaint Message")

    def __str__(self):
        # This method returns the string representation of the object based on its 'name' attribute.
        return self.name

    

class Suggestion_Model(models.Model):
    """
    This code implements the Suggestion_Model Django model, which is used to describe and store user recommendations.
      A web application uses the model to maintain and interact with recommendation data so that it may hear from users 
      and make changes in response to their ideas.

    Attributes:
        name (str): Name of the customer making the suggestion.
        message (str): Suggestion message from the customer.
    """

    # Name field with a maximum length of 30 characters
    name = models.CharField(max_length = 30)
    # Suggestion message field with a default value "Enter the suggestion Message"
    message = models.TextField(default="Enter the suggestion Message")

    def __str__(self):
    # This method returns the string representation of the object based on its 'name' attribute.
        return self.name


# Rating_Model represents customer ratings
class Rating_Model(models.Model):
    """
    code implements a Django model named Rating_Model to represent and store customer ratings. 
    The model is used in a web application to manage and interact with rating data, providing insights 
    into customer satisfaction and feedback for various services or products.
    Attributes:
        name (str): Name of the customer giving the rating.
        rating (str): Customer's rating value (e.g., 1, 2, 3, 4, 5).
    """
    # Name field with a maximum length of 30 characters
    name = models.CharField(max_length = 30)
    # Rating field with a maximum length of 30 characters
    rating = models.CharField(max_length=30)

    def __str__(self):
    # This method returns the string representation of the object based on its 'name' attribute.
     return self.name
