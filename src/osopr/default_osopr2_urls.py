"""osorp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from __future__ import unicode_literals
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views import defaults as default_views

urlpatterns = [

    # PROJECT URLS CONFIGURATION
    #------------------------------------------------------
    url(settings.ADMIN_URL, include(admin.site.urls)),
    url(r'^', include('links.urls')),

    
    # USER MANAGEMENT URLS CONFIGURATION 
    #--------------------------------------------------------

    # User management_Arun
    #----------------------------
    #url(r'^users/', include(profiles.urls, namespace='profiles')), 
    #url(r'^', include(accounts.urls, namespace='accounts')), 

    # User management_two scoops
    #----------------------------
    #url(r'^users/', include("users.urls", namespace="users")),
    #url(r'^accounts/', include('allauth.urls')),



    # django-allauth
    #---------------------------
    #url(r'^accounts/', include('allauth.urls')),


    #django-registration 
    #-------------------------------------
    url(r'^accounts/', include('registration.backends.simple.urls')),

]


#STATIC FILES CONFIGURATION
#-------------------------------------------------------------------------
# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
     # This allows the error pages to be debugged during development, just visit
     # these url in browser to see how these error pages look like.
     urlpatterns += [
         url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception("Bad Request!")}),
         url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception("Permissin Denied")}),
         url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception("Page not Found")}),
         url(r'^500/$', default_views.server_error),

    ]




