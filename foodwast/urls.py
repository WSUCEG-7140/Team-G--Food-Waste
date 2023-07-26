"""
foodwast URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
The code sets up URL patterns for a Django project named "foodwast" by defining mappings between specific URLs and corresponding view functions from the "food" app. 
It also includes configurations for serving static and media files during development.
The code was implemented to provide a routing mechanism for the Django project. 
It establishes how different URLs are accessed and handled in the web application. 
By defining URL patterns and linking them to view functions, the code separates the logic of different views, 
ensuring clean and organized code.
The code is typically located in the main URL configuration file (usually named urls.py) of a Django project. 
It acts as the central point for handling URL routing in the application. 
"""
# Import the admin module for Django's built-in administration site.
from django.contrib import admin

# Import the 'url' function for defining URL patterns.
from django.conf.urls import url

# Import views module from the 'food' app as 'food_views'.
from food import views as food_views

# Import various settings from 'foodwast.settings'.
from foodwast.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT

# Import 'static' function for serving static and media files during development.
from django.conf.urls.static import static

# URL patterns for the Django project.
urlpatterns = [
    # Admin URL
    url(r'^admin/', admin.site.urls),

    # Home URL
    url(r'^$', food_views.index, name='index' ),

    # About URL
    url(r'^about/$', food_views.about, name='about' ),
    
    # Donation URL
    url(r'^donate/$',food_views.donate,name='donate'),

    # Complaint URL
    url(r'^Addcomplaint/$',food_views.Addcomplaint,name='Addcomplaint'),

    # Suggestion URL
    url(r'^Addsuggestion/$',food_views.Addsuggestion,name='Addsuggestion'),

    # Rating URL
    url(r'^Addrating/$',food_views.Addrating,name='Addrating'),

    # Donor Login URL
    url(r'^donar/$',food_views.donar,name='donar'),

    # Donor Registration URL
    url(r'^donarregister/$',food_views.donarregister,name='donarregister'),
    
    # Admin Login URL
    url(r'^admin1/$',food_views.admin1,name='admin1'),

    # Agent Login URL
    url(r'^agent/$',food_views.agent,name='agent'),

    # Contact URL
    url(r'^contact/$',food_views.contact,name='contact'),

    # Donor Home URL
    url(r'^DonorHome/$',food_views.DonorHome,name='DonorHome'),

    # Admin Home URL
    url(r'^AdminHome/$',food_views.AdminHome,name='AdminHome'),

    # Agent Home URL
    url(r'^AgentHome/$',food_views.AgentHome,name='AgentHome'),

    # Add Agent URL
    url(r'^AddAgent/$',food_views.AddAgent,name='AddAgent'),

    # View Assigned Donors URL
    url(r'^ViewADonars/$',food_views.ViewADonars,name='ViewADonars'),

    # Donor Donation Success URL
    url(r'^donatesuccess/$',food_views.donatesuccess,name='donatesuccess'),

    # Complaint Success URL
    url(r'^complaintsuccess/$',food_views.complaintsuccess,name='complaintsuccess'),

    # Suggestion Success URL
    url(r'^suggestionsuccess/$',food_views.suggestionsuccess,name='suggestionsuccess'),

    # Rating Success URL
    url(r'^ratingsuccess/$',food_views.ratingsuccess,name='ratingsuccess'),

    # Donor Registration Success URL
    url(r'^donatersuccess/$',food_views.donatersuccess,name='donatersuccess'),

    # View Agents URL
    url(r'^ViewAgent/$',food_views.ViewAgent,name='ViewAgent'),

    # Update Agent URL
    url(r'^updateagent/(?P<a_id>\w+)',food_views.update_agent),

    # Delete Agent URL
    url(r'^deleteagent/(?P<a_id>\w+)',food_views.delete_agent),
    
    # View Specific Donors URL
    url(r'^ViewSDonars/(?P<c_id>\w+)',food_views.ViewSDonars),

    # View All Donors URL
    url(r'^ViewDonars/$',food_views.ViewDonars,name='ViewDonars'),

    # View Donor Profile URL
    url(r'^ViewProfile/$',food_views.ViewProfile,name='ViewProfile'),

    # Edit Donor Profile URL
    url(r'^EditProfile/(?P<d_id>\w+)',food_views.EditProfile,name='EditProfile'),
    
    # Assign Donors URL
    url(r'^AssignDonars/$',food_views.AssignDonars,name='AssignDonars'),
   
    # View Assigned Agents URL
    url(r'^ViewAssignAgents/$',food_views.ViewAssignAgents,name='ViewAssignAgents'),
]

# Check if the app is running in debug mode.
if DEBUG:
    # Add URL patterns for serving static and media files during development.
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
