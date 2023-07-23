from django.shortcuts import render,redirect

from .models import Donar_Model,Agent_Model,Assign_Model

from .forms import Donar_ModelCreate,Agent_ModelCreate,Assign_ModelCreate

import sys
# Create your views here.

def index(request):

    return render(request,'index.html')


def about(request):

    return render(request,'about.html')

def donate(request):

    upload=Donar_ModelCreate()

    if request.method=='POST':
        
        upload=Donar_ModelCreate(request.POST,request.FILES)

        if upload.is_valid():

            upload.save()

            return redirect('donatesuccess')
        
    else:
        
        return render(request,'donate.html',{'upload_form':upload})


#function for handling the submission of a donor registration 
def donarregister(request):
    """
    Registers a donor with the provided information.

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

    if request.method == "POST":
        
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
            
            print("Hello world",username,password)
            #print("retive from database",Adminlogin.objects.get(username))
            if(username=="admin" and password=="admin"):
                
                request.session["name"]=username

                return redirect('AdminHome')
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])
            pass


    return render(request,'admin.html')

def contact(request):

    return render(request,'contact.html')

def agent(request):

    if request.method == "POST":
        
        name=request.POST.get('username')
        password=request.POST.get('password')

        try:
            print("Hello world",name,password)
            #print("retive from database",Adminlogin.objects.get(username))
            enter=Agent_Model.objects.get(name=name,password=password)

            print(enter.id)
            request.session["id"]=enter.id 
            request.session["name"]=enter.name
           


            return redirect('AgentHome')
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])
            pass

    return render(request,'agent.html')
#submission of a donor login form
def donar(request):

    """
    Register a donor with the provided information.

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
            
            if(username=="admin" and password=="admin"):
             # Check if the entered 'username' and 'password' are both "admin".
            request.session["name"]=username

                return redirect('AdminHome')
        # If any unexpected error occurs, handle it here.

        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])

          # Since the error is caught and handled, use 'pass' to continue with the code execution.
            pass

    # Render the 'donor.html' template to display the donor page.
      return render(request,'donor.html')

def donatesuccess(request):

    return render(request,'donatesuccess.html')

def AdminHome(request):
    return render(request,'AdminHome.html')


def AgentHome(request):

    name=request.session['name']

    return render(request,'AgentHome.html',{'name':name})


def AddAgent(request):
    """
    Adds a new agent to the system.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: If the request method is 'POST' and the form data is valid,
        redirects to 'AddAgent' page after saving the data. Otherwise, renders the
        'AddAgent.html' template with the 'upload_form' context variable.

    Contract:
        Precondition:
        - The Agent_ModelCreate class must have proper validation rules for the form data.

        Postcondition:
        - If the request method is 'POST' and the form data is valid, a new agent will be added to the system.
        - If the request method is not 'POST', the 'AddAgent.html' template will be rendered with the form.

    """
    upload = Agent_ModelCreate()

    if request.method == 'POST':
        upload = Agent_ModelCreate(request.POST, request.FILES)

        if upload.is_valid():
            upload.save()
            return redirect('AddAgent')
    else:
        return render(request, 'AddAgent.html', {'upload_form': upload})



    
def ViewAgent(request):

    obj=Agent_Model.objects.all()

    return render(request,'ViewAgents.html',{'obj':obj})

def update_agent(request, a_id):
    """
    Update the Agent_Model instance based on the provided a_id.

    Parameters:
        request (HttpRequest): The request object.
        a_id (int): The ID of the Agent_Model instance to update.

    Returns:
        HttpResponse: If the form is valid and the update is successful, redirect to the 'ViewAgent' page. Otherwise, render the 'AddAgent.html' template with the form to correct errors.

    Program By Contract (Precondition):
        - The Agent_Model class exists and is imported properly.
    
    Program By Contract (Postcondition):
        - If a valid Agent_Model instance with the given a_id is found, it will be updated with the submitted form data and saved.
        - If no Agent_Model instance is found with the given a_id, the user will be redirected to the 'index' page.
    """
    # Convert the provided a_id to an integer.
    a_id = int(a_id)

    # Print the provided a_id for debugging purposes.
    print("The aid is ", a_id)

    try:
        # Try to get the Agent_Model instance with the given a_id.
        a_sel = Agent_Model.objects.get(id=a_id)
    except Agent_Model.DoesNotExist:
        # If no instance is found, redirect the user to the 'index' page.
        return redirect('index')

    # Create a form to update the Agent_Model instance with the request data or use the existing instance data.
    f_form = Agent_ModelCreate(request.POST or None, instance=a_sel)

    if f_form.is_valid():
        # If the form is valid, save the updated instance and redirect the user to the 'ViewAgent' page.
        f_form.save()
        return redirect('ViewAgent')

    # If the form is not valid, render the 'AddAgent.html' template with the form to correct errors.
    return render(request, 'AddAgent.html', {'upload_form': f_form})


def EditProfile(request, d_id):
    """
    Edit a donor's profile.

    Parameters:
        request (HttpRequest): The HTTP request object containing form data.
        d_id (int): The donor's ID obtained from URL parameters.

    Returns:
        HttpResponse: A rendered HTML page displaying the editable profile form.

    Precondition:
        - The 'd_id' parameter must be a valid integer representing a DonarRegister_Model object.

    Postcondition:
        - If the 'd_id' parameter corresponds to an existing DonarRegister_Model object,
          the editable profile form will be rendered in the 'EditProfile.html' template.
        - If the 'd_id' parameter does not correspond to any object, the user will be redirected to 'index'.

    """
    # Convert 'd_id' to an integer.
    d_id = int(d_id)

    # Print the value of 'd_id' for debugging purposes.
    print("The did is ", d_id)

    try:
        # Attempt to retrieve the DonarRegister_Model object with the given 'd_id'.
        a_sel = DonarRegister_Model.objects.get(id=d_id)

    except DonarRegister_Model.DoesNotExist:
        # If the DonarRegister_Model object does not exist, redirect to the 'index' page.
        return redirect('index')

    # Create a form instance with the data from the POST request, if available,
    # using the retrieved DonarRegister_Model object as the instance for editing.
    f_form = DonarRegister_ModelCreate(request.POST or None, instance=a_sel)

    if f_form.is_valid():
        # If the form data is valid, save the changes to the DonarRegister_Model object.
        f_form.save()

        # Redirect to the 'ViewProfile' page after successful form submission.
        return redirect('ViewProfile')
        
    # Render the 'EditProfile.html' template with the form instance.
    return render(request, 'EditProfile.html', {'upload_form': f_form})


def delete_agent(request,a_id):

    a_id=int(a_id)
    try:

        a_sel=Agent_Model.objects.get(id=a_id)

    except Agent_Model.DoesNotExist:
        pass

    a_sel.delete()
    return redirect('ViewAgent')

def ViewSDonars(request,c_id):

    c_id=int(c_id)

    obj=Donar_Model.objects.all().filter(id=c_id)

    
    return render(request,'ViewSDonars.html',{'obj':obj})



def ViewDonars(request):

    obj=Donar_Model.objects.all()

    return render(request,'ViewDonars.html',{'obj':obj})

def ViewADonars(request):

    id=request.session['id']

    obj=Assign_Model.objects.all().filter(aid=id)

    
    return render(request,'ViewADonars.html',{'obj':obj})


def ViewProfile(request):
    """
    View a donor's profile.

    Parameters:
        request (HttpRequest): The HTTP request object containing session data.

    Returns:
        HttpResponse: A rendered HTML page displaying the donor's profile details.

    Precondition:
        - The 'did' key must exist in the request session.

    Postcondition:
        - If the 'did' key exists and corresponds to a valid DonarRegister_Model object,
          the profile details will be rendered in the 'ViewProfile.html' template.
        - If the 'did' key does not exist or the object is not found, an error page may be displayed.

    Raises:
        KeyError: If the 'did' key is not found in the request session.

    """
    try:
        # Precondition: Check if the 'did' key exists in the request session
        did = request.session['did']
    except KeyError:
        # If the 'did' key is not found, raise an error or redirect to an error page.
        raise KeyError("The 'did' key is not found in the request session.")

    # Retrieve the DonarRegister_Model object with the given 'did' value.
    # Postcondition: If the object is found, it will be available in the 'obj' variable.
    obj = DonarRegister_Model.objects.filter(id=did).first()

    # Render the 'ViewProfile.html' template with the 'obj' variable.
    return render(request, 'ViewProfile.html', {'obj': obj})


def AssignDonars(request):

    upload=Assign_ModelCreate()

    try:

            if request.method=='POST':
        
                 upload=Assign_ModelCreate(request.POST,request.FILES)

                 if upload.is_valid():

                    upload.save()

                    return redirect('AssignDonars')
                 else:
                    return redirect('AssignDonars')
        
            else:
        
                 return render(request,'AssignDonars.html',{'upload_form':upload})
    except:

            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])
            pass


def ViewAssignAgents(request):

    obj=Assign_Model.objects.all()

    return render(request,'ViewAssignAgents.html',{'obj':obj})







