# Importing necessary functions from the Django module 'shortcuts'
from django.shortcuts import render, redirect
# Importing models from the current package or module (denoted by the dot)
from .models import Donar_Model, Agent_Model, Assign_Model, DonarRegister_Model, Complaint_Model, Suggestion_Model, Rating_Model
# Importing forms from the current package or module (denoted by the dot)
from .forms import Donar_ModelCreate, Agent_ModelCreate, Assign_ModelCreate, DonarRegister_ModelCreate, Complaint_ModelCreate, Suggestion_ModelCreate, Rating_ModelCreate

# Importing the 'sys' module, which provides access to some variables used or maintained by the interpreter
import sys

# View function for the 'index' page
def index(request):
    """
    The 'render' function is used to render an HTML template ('index.html')
    and return it as an HTTP response to the client (usually a web browser).
    The 'request' parameter is the HttpRequest object sent by the client.
    It contains information about the client's request, such as GET or POST data.
    return render(request, 'index.html')
    """
    return render(request, 'index.html')

# View function for the 'about' page
def about(request):
    """
    Similar to the 'index' function, this function renders the 'about.html' template
    and returns it as an HTTP response to the client (usually a web browser).
    The 'request' parameter contains information about the client's request.
    """
    return render(request, 'about.html')


def donate(request):
    """
    The donate view function handles form submissions for donations, saving valid data to the database, and redirecting to a success page if the data is successfully saved.
    This code was implemented to manage donation form submissions efficiently and store valid donation data into the database.
    This code is used to handle the donation functionality of a Django web application, processing and saving donation data submitted via a form.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: If the request method is 'POST' and the form data is valid,
        redirects to 'donatesuccess' page after saving the data. Otherwise, renders
        the 'donate.html' template with the 'upload_form' context variable.
    """
    # Create an instance of the Donar_ModelCreate form
    upload=Donar_ModelCreate()
    # Check if the request method is 'POST'
    if request.method=='POST':
            # Create a new instance of the Donar_ModelCreate form with the POST data and FILES data
            upload=Donar_ModelCreate(request.POST,request.FILES)
            # Check if the form data is valid
            if upload.is_valid():
                # Save the valid form data (donation) to the database
                upload.save()
            # Redirect to the 'donatesuccess' page after successful data saving
            return redirect('donatesuccess')
    else:
        # If the request method is not 'POST', render the 'donate.html' template
        # and pass the 'upload' form as context variable 'upload_form'
        return render(request,'donate.html',{'upload_form':upload})


def Addcomplaint(request):
    """
    The Addcomplaint view function handles form submissions for adding complaints,
    saving valid data to the database, and redirecting to a success page if the data
    is successfully saved.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: If the request method is 'POST' and the form data is valid,
        redirects to 'complaintsuccess' page after saving the data. Otherwise, renders
        the 'Addcomplaint.html' template with the 'upload_form' context variable.
    """
    # Create an instance of the Complaint_ModelCreate form
    upload = Complaint_ModelCreate()

    # Check if the request method is 'POST'
    if request.method == 'POST':
        # Create a new instance of the Complaint_ModelCreate form with the POST data and FILES data
        upload = Complaint_ModelCreate(request.POST, request.FILES)

        # Check if the form data is valid
        if upload.is_valid():
            # Save the valid form data (complaint) to the database
            upload.save()
            # Redirect to the 'complaintsuccess' page after successful data saving
            return redirect('complaintsuccess')
    else:
        # If the request method is not 'POST', render the 'Addcomplaint.html' template
        # and pass the 'upload' form as context variable 'upload_form'
        return render(request, 'Addcomplaint.html', {'upload_form': upload})


def Addsuggestion(request):
    """
    The Addsuggestion view function handles form submissions for adding suggestions,
    saving valid data to the database, and redirecting to a success page if the data
    is successfully saved.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: If the request method is 'POST' and the form data is valid,
        redirects to 'suggestionsuccess' page after saving the data. Otherwise, renders
        the 'Addsuggestion.html' template with the 'upload_form' context variable.
    """
    # Create an instance of the Suggestion_ModelCreate form
    upload = Suggestion_ModelCreate()

    # Check if the request method is 'POST'
    if request.method == 'POST':
        # Create a new instance of the Suggestion_ModelCreate form with the POST data and FILES data
        upload = Suggestion_ModelCreate(request.POST, request.FILES)

        # Check if the form data is valid
        if upload.is_valid():
            # Save the valid form data (suggestion) to the database
            upload.save()
            # Redirect to the 'suggestionsuccess' page after successful data saving
            return redirect('suggestionsuccess')
    else:
        # If the request method is not 'POST', render the 'Addsuggestion.html' template
        # and pass the 'upload' form as context variable 'upload_form'
        return render(request, 'Addsuggestion.html', {'upload_form': upload})


def Addrating(request):
    """
    The Addrating view function handles form submissions for adding ratings,
    saving valid data to the database, and redirecting to a success page if the data
    is successfully saved.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: If the request method is 'POST' and the form data is valid,
        redirects to 'ratingsuccess' page after saving the data. Otherwise, renders
        the 'Addrating.html' template with the 'upload_form' context variable.
    """
    # Create an instance of the Rating_ModelCreate form
    upload = Rating_ModelCreate()

    # Check if the request method is 'POST'
    if request.method == 'POST':
        # Create a new instance of the Rating_ModelCreate form with the POST data and FILES data
        upload = Rating_ModelCreate(request.POST, request.FILES)

        # Check if the form data is valid
        if upload.is_valid():
            # Save the valid form data (rating) to the database
            upload.save()
            # Redirect to the 'ratingsuccess' page after successful data saving
            return redirect('ratingsuccess')
    else:
        # If the request method is not 'POST', render the 'Addrating.html' template
        # and pass the 'upload' form as context variable 'upload_form'
        return render(request, 'Addrating.html', {'upload_form': upload})


#function for handling the submission of a donor registration 
def donarregister(request):
    """
    This is a Django view function named donarregister, which handles donor registration form submissions. 
    It checks if the HTTP request method is 'POST', validates the form data, saves the valid data to the database, 
    and redirects to a 'donatersuccess' page upon successful registration. If the request method is 'GET' or the form is invalid, 
    it renders the 'donateregister.html' template with the form. The function ensures the donor's information is saved in the database 
    if the form data is valid.
    Parameters:
    - request: The HTTP request object containing form data.
    Returns:
    - If the registration is successful, redirects to 'donatersuccess' page.
    - If the request method is GET or the form is invalid, renders the 'donateregister.html' template with the form.
    Contracts:
    - Precondition: 'donateregister.html' template with 'upload_form' context variable exists.
    - Postcondition: The donor's information is saved in the database if the form is valid.
    """
    # Create an instance of the DonarRegister_ModelCreate form.
    upload=DonarRegister_ModelCreate()
    # Check if the HTTP request method is POST, indicating a form submission.

    if request.method=='POST':
        # Create another instance of the DonarRegister_ModelCreate form with the data from the POST request.
        upload=DonarRegister_ModelCreate(request.POST,request.FILES)
            # Check if the submitted form data is valid.
        if upload.is_valid():
                upload.save()
        return redirect('donatersuccess')
    else:
        # If the request method is not POST, render the 'donateregister.html' template with the form.
        return render(request,'donateregister.html',{'upload_form':upload})


def admin1(request):
    """
    View function named admin1, responsible for handling administrator login attempts. 
    If the HTTP request method is 'POST', the function retrieves the 'username' and 'password' 
    from the POST data, and if they match the admin credentials ("admin" for both username and password), 
    the function stores the 'username' in the session and redirects to the 'AdminHome' page for a successful login.
    If any error occurs during the login process, it will be printed to the console. If the request method is not 
    'POST', it renders the 'admin.html' template to display the login form.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: If the request method is 'POST' and the login credentials are valid,
        redirects to 'AdminHome' page. Otherwise, renders the 'admin.html' template.
    """
    # Check if the request method is 'POST'
    if request.method == "POST":
        # Retrieve the 'username' and 'password' from the POST data
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
            # Print the 'username' and 'password' received from the request
            print("Hello world",username,password)
            #print("retive from database",Adminlogin.objects.get(username))
            if(username=="admin" and password=="admin"):
               # Store 'username' in the request session
                request.session["name"]=username
                # Redirect to the 'AdminHome' page after successful login
                return redirect('AdminHome')
        # If an exception occurs during the login process, handle it
        except:
            # Print the unexpected error information
            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])
            pass

    # If the request method is not 'POST', render the 'admin.html' template for login
    return render(request,'admin.html')


#submission of a donor login form
def donar(request):
    """
    The 'donar' view function in Django facilitates donor registration and login. 
    It checks if the form data contains valid 'username' and 'password' fields and verifies them against records in the 'DonarRegister_Model'. 
    Upon successful login, the donor's information is stored in the session, and the user is redirected to 'DonorHome'. 
    In case of errors or if the method is not 'POST', the function renders the 'donor.html' template for registration or login. 
    Valid form data is then saved in the database, completing the registration process.
    Parameters:
    - request: The HTTP request object containing form data.
    Returns:
    - If the registration is successful, redirects to the 'donatersuccess' page.
    - If the request method is GET or the form is invalid, renders the 'donateregister.html' template with the form.
    Contracts:
    - Precondition: The 'donateregister.html' template with the 'upload_form' context variable exists.
    - Postcondition: If the form is valid, the donor's information is saved in the database.
    """
    # Check if the request method is a POST request.
    if request.method == "POST":
        # Retrieve the 'username' and 'password' fields from the POST data.
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            #print("retive from database",Adminlogin.objects.get(username))
            print("Hello world",username,password)
            enter=DonarRegister_Model.objects.get(name=username,password=password)
            #print("retive from database",Adminlogin.objects.get(username))
            print(enter.id)
            request.session["did"]=enter.id 
            request.session["dname"]=enter.name
            request.session["name"]=username

            # Check if the entered 'username' and 'password' are both "admin".
            return redirect('DonorHome')
            # If any unexpected error occurs, handle it here.
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])
            # Since the error is caught and handled, use 'pass' to continue with the code execution.
            pass
    # Render the 'donor.html' template to display the donor page.
    return render(request,'donor.html')


def contact(request):
    """
    The contact view function renders the 'contact.html' template.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered 'contact.html' template.
    """
    return render(request, 'contact.html')


def agent(request):
    """
    The agent view function handles agent login attempts, storing relevant information in the session if successful,
    and redirecting to the 'AgentHome' page.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: If the request method is 'POST' and the login credentials are valid,
        redirects to the 'AgentHome' page. Otherwise, renders the 'agent.html' template.
    """
    # Check if the request method is 'POST'
    if request.method == "POST":
        # Retrieve the 'username' and 'password' fields from the POST data
        name = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Print the 'username' and 'password' received from the request
            print("Hello world", name, password)
            enter = Agent_Model.objects.get(name=name, password=password)
            # Print the 'id' of the agent retrieved from the database
            print(enter.id)
            # Store 'id' and 'name' of the agent in the request session
            request.session["id"] = enter.id 
            request.session["name"] = enter.name
            # Redirect to the 'AgentHome' page after successful login
            return redirect('AgentHome')

        except:
            # Print the unexpected error information
            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])
            pass

    # Render the 'agent.html' template for agent login
    return render(request, 'agent.html')


def donatesuccess(request):
    """
    The donatesuccess view function renders the 'donatesuccess.html' template.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered 'donatesuccess.html' template.
    """
    return render(request, 'donatesuccess.html')


def complaintsuccess(request):
    """
    The complaintsuccess view function renders the 'complaintsuccess.html' template.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered 'complaintsuccess.html' template.
    """
    return render(request, 'complaintsuccess.html')


def suggestionsuccess(request):
    """
    The suggestionsuccess view function renders the 'suggestionsuccess.html' template.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered 'suggestionsuccess.html' template.
    """
    return render(request, 'suggestionsuccess.html')


def ratingsuccess(request):
    """
    The ratingsuccess view function renders the 'ratingsuccess.html' template.
     Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered 'ratingsuccess.html' template.
    """
    return render(request, 'ratingsuccess.html')


def donatersuccess(request):
    """
    The donatersuccess view function renders the 'donatersuccess.html' template.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered 'donatersuccess.html' template.
    """
    return render(request, 'donatersuccess.html')


def AdminHome(request):
    """
    The AdminHome view function renders the 'AdminHome.html' template.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered 'AdminHome.html' template.
    """
    return render(request, 'AdminHome.html')


def AgentHome(request):
    """
    The AgentHome view function renders the 'AgentHome.html' template.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered 'AgentHome.html' template with the 'name' context variable.
    """
    name = request.session.get('name', None)  
    # Use get method to handle missing key
    return render(request, 'AgentHome.html', {'name': name})


def DonorHome(request):
    """
    The DonorHome view function renders the 'DonorHome.html' template.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered 'DonorHome.html' template with the 'name' context variable.
    """
    name = request.session.get('name', None)  
    # Use get method to handle missing key
    return render(request, 'DonorHome.html', {'name': name})


def AddAgent(request):
    """
    The AddAgent view function handles form submissions for adding agents,
    saving valid data to the database, and redirecting back to the 'AddAgent' page after data saving.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: If the request method is 'POST' and the form data is valid,
        redirects to 'AddAgent' page after saving the data. Otherwise, renders
        the 'AddAgent.html' template with the 'upload_form' context variable.
    """
    # Create an instance of the Agent_ModelCreate form
    upload = Agent_ModelCreate()

    # Check if the request method is 'POST'
    if request.method == 'POST':
        # Create a new instance of the Agent_ModelCreate form with the POST data and FILES data
        upload = Agent_ModelCreate(request.POST, request.FILES)

        # Check if the form data is valid
        if upload.is_valid():
            # Save the valid form data (agent) to the database
            upload.save()
            # Redirect back to the 'AddAgent' page after successful data saving
            return redirect('AddAgent')

    # If the request method is not 'POST', render the 'AddAgent.html' template
    # and pass the 'upload' form as context variable 'upload_form'
    return render(request, 'AddAgent.html', {'upload_form': upload})


def ViewAgent(request):
    """
    The ViewAgent view function retrieves all objects of the Agent_Model from the database
    and renders them in the 'ViewAgents.html' template.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered 'ViewAgents.html' template with the 'obj' context variable,
        containing all the Agent_Model objects retrieved from the database.
    """
    # Retrieve all objects of the Agent_Model from the database
    obj = Agent_Model.objects.all()

    # Render the 'ViewAgents.html' template with the 'obj' context variable
    # 'obj' will contain all the Agent_Model objects retrieved from the database
    return render(request, 'ViewAgents.html', {'obj': obj})


def update_agent(request, a_id):
    """
    The update_agent view function handles updating agent information,
    saving valid data to the database, and redirecting to the 'ViewAgent' page after data saving.
    Parameters:
        request (HttpRequest): The HTTP request object.
        a_id (int): The ID of the agent to be updated.
    Returns:
        HttpResponse: If the request method is 'POST' and the form data is valid,
        updates the agent information in the database and redirects to 'ViewAgent' page.
        Otherwise, renders the 'AddAgent.html' template with the form pre-filled with existing data.
    """
    a_id = int(a_id)

    print("The aid is ", a_id)

    try:
        a_sel = Agent_Model.objects.get(id=a_id)

    except Agent_Model.DoesNotExist:
        return redirect('index')

    # Create an instance of the Agent_ModelCreate form, pre-filled with existing agent data
    f_form = Agent_ModelCreate(request.POST or None, instance=a_sel)

    if f_form.is_valid():
        # Save the valid form data (updated agent information) to the database
        f_form.save()
        # Redirect to the 'ViewAgent' page after successful data saving
        return redirect('ViewAgent')

    # Render the 'AddAgent.html' template with the 'upload_form' context variable
    # 'upload_form' will contain the pre-filled form with existing agent data
    return render(request, 'AddAgent.html', {'upload_form': f_form})


def EditProfile(request, d_id):
    """
    The EditProfile view function handles updating donor profile information,
    saving valid data to the database, and redirecting to the 'ViewProfile' page after data saving.
    Parameters:
        request (HttpRequest): The HTTP request object.
        d_id (int): The ID of the donor to be updated.
    Returns:
        HttpResponse: If the request method is 'POST' and the form data is valid,
        updates the donor profile information in the database and redirects to 'ViewProfile' page.
        Otherwise, renders the 'EditProfile.html' template with the form pre-filled with existing data.
    """
    d_id = int(d_id)

    print("The did is ", d_id)

    try:
        a_sel = DonarRegister_Model.objects.get(id=d_id)

    except DonarRegister_Model.DoesNotExist:
        return redirect('index')

    # Create an instance of the DonarRegister_ModelCreate form, pre-filled with existing donor data
    f_form = DonarRegister_ModelCreate(request.POST or None, instance=a_sel)

    if f_form.is_valid():
        # Save the valid form data (updated donor profile information) to the database
        f_form.save()
        # Redirect to the 'ViewProfile' page after successful data saving
        return redirect('ViewProfile')

    # Render the 'EditProfile.html' template with the 'upload_form' context variable
    # 'upload_form' will contain the pre-filled form with existing donor data
    return render(request, 'EditProfile.html', {'upload_form': f_form})

def delete_agent(request, a_id):
    """
    The delete_agent view function handles deleting an agent from the database and redirects to 'ViewAgent' page.
    Parameters:
        request (HttpRequest): The HTTP request object.
        a_id (int): The ID of the agent to be deleted.
    Returns:
        HttpResponse: Redirects to 'ViewAgent' page after deleting the agent.
    """
    a_id = int(a_id)

    try:
        a_sel = Agent_Model.objects.get(id=a_id)
        a_sel.delete()
    except Agent_Model.DoesNotExist:
        pass

    return redirect('ViewAgent')


def ViewSDonars(request, c_id):
    """
    The ViewSDonars view function retrieves all donors associated with a specific ID (c_id)
    and renders them in the 'ViewSDonars.html' template.
    Parameters:
        request (HttpRequest): The HTTP request object.
        c_id (int): The ID of the donor to be viewed.
    Returns:
        HttpResponse: The rendered 'ViewSDonars.html' template with the 'obj' context variable,
        containing all the Donar_Model objects filtered by the provided c_id.
    """
    c_id = int(c_id)

    # Retrieve all donors associated with the provided ID (c_id) from the database
    obj = Donar_Model.objects.all().filter(id=c_id)

    # Render the 'ViewSDonars.html' template with the 'obj' context variable
    # 'obj' will contain all the Donar_Model objects filtered by the provided c_id
    return render(request, 'ViewSDonars.html', {'obj': obj})


def ViewDonars(request):
    """
    The ViewDonars view function retrieves all donors from the database and renders them in the 'ViewDonars.html' template.
    If a POST request with a search query is made, it filters donors by fullname.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered 'ViewDonars.html' template with the 'obj' context variable,
        containing all the Donar_Model objects filtered by the search query (if provided).
    """
    # Retrieve all donors from the database
    obj = Donar_Model.objects.all()

    # Check if the request method is 'POST'
    if request.method == 'POST':
        # Retrieve the search query from the POST data
        name = request.POST.get("search")

        # Filter donors by fullname based on the search query
        obj = Donar_Model.objects.all().filter(fullname=name)

    # Render the 'ViewDonars.html' template with the 'obj' context variable
    # 'obj' will contain all the Donar_Model objects filtered by the search query (if provided)
    return render(request, 'ViewDonars.html', {'obj': obj})


def ViewADonars(request):
    """
    The ViewADonars view function retrieves all donors associated with the logged-in agent (based on the agent's ID)
    and renders them in the 'ViewADonars.html' template.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered 'ViewADonars.html' template with the 'obj' context variable,
        containing all the Donar_Model objects filtered by the agent's ID.
    """
    # Retrieve the agent's ID from the session
    id = request.session.get('id')

    # Retrieve all donors associated with the agent's ID from the database
    obj = Assign_Model.objects.all().filter(aid=id)

    # Render the 'ViewADonars.html' template with the 'obj' context variable
    # 'obj' will contain all the Donar_Model objects filtered by the agent's ID
    return render(request, 'ViewADonars.html', {'obj': obj})


def ViewProfile(request):
    """
    The ViewProfile view function retrieves the donor's profile information based on the donor's ID (did) stored in the session
    and renders them in the 'ViewProfile.html' template.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered 'ViewProfile.html' template with the 'obj' context variable,
        containing the DonarRegister_Model object filtered by the donor's ID (did) stored in the session.
    """
    # Retrieve the donor's ID (did) from the session
    did = request.session.get('did')

    # Retrieve the donor's profile information based on the donor's ID (did) from the database
    obj = DonarRegister_Model.objects.all().filter(id=did)

    # Render the 'ViewProfile.html' template with the 'obj' context variable
    # 'obj' will contain the DonarRegister_Model object filtered by the donor's ID (did)
    return render(request, 'ViewProfile.html', {'obj': obj})

def AssignDonars(request):
    """
    The 'AssignDonars' view function handles the assignment of donors to agents. 
    It validates the form data received from the 'Assign_ModelCreate' form and saves the data to create donor assignments in the database 
    if it's valid. If the form data is invalid or the method is not 'POST', it redirects back to the 'AssignDonars' page to display the form again.
    If any unexpected error occurs during execution, it will be caught, and the error details will be printed for debugging.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: If the request method is 'POST' and the form data is valid,
        redirects to 'AssignDonars' page after saving the data. Otherwise, redirects
        back to 'AssignDonars' page to display the form.
    Contract:
        Precondition:
        - The Assign_ModelCreate class must have proper validation rules for the form data.
        Postcondition:
        - If the request method is 'POST' and the form data is valid, donor assignments will be saved to the database.
        - If the request method is 'POST' and the form data is invalid, the user will be redirected back to the 'AssignDonars' page to display the form again.
        - If the request method is not 'POST', the 'AssignDonars.html' template will be rendered with the form.
        Exception Handling:
        - If any unexpected error occurs during execution, it will be caught, and the error details will be printed.
    """
    # Create an instance of the Assign_ModelCreate form
    upload=Assign_ModelCreate()
    try:
        # Check if the request method is 'POST'
        if request.method=='POST':
            # Create a new instance of the Assign_ModelCreate form with the POST data and FILES data
            upload=Assign_ModelCreate(request.POST,request.FILES)
            # Check if the form data is valid
            if upload.is_valid():
                    # Save the form data to create donor assignments in the database
                    upload.save()
                    # Redirect to the 'AssignDonars' page after successful data saving
                    return redirect('AssignDonars')
            else:
                # If the form data is invalid, redirect back to 'AssignDonars' page to display the form again
                return redirect('AssignDonars')
        else:
            # If the request method is not 'POST', render the 'AssignDonars.html' template
            # and pass the 'upload' form as context variable 'upload_form'
            return render(request,'AssignDonars.html',{'upload_form':upload})
    except:
            # Print the unexpected error information
            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])
            pass


def ViewAssignAgents(request):
    """
    The code retrieves all objects of the 'Assign_Model' from the database and renders them in the 'ViewAssignAgents.html' template using the 'obj' context variable.
    This code was implemented to display assigned agent information in a Django web application.
    This code is used to show information about assigned agents to users in a Django web application.
    Parameters:
    - request: An HTTP request object.
    Returns:
    - HttpResponse: The rendered 'ViewAssignAgents.html' template with the 'obj' context variable,
      containing all the Assign_Model objects retrieved from the database.
    """
    # Retrieve all objects of the Assign_Model from the database
    obj=Assign_Model.objects.all()
    # Render the 'ViewAssignAgents.html' template with the 'obj' context variable
    # 'obj' will contain all the Assign_Model objects retrieved from the database
    return render(request,'ViewAssignAgents.html',{'obj':obj})

