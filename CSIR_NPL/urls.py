"""
URL configuration for CSIR_NPL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# CSIR_NPL/urls.py

from django.contrib import admin # type: ignore
from django.urls import path, include, re_path # type: ignore
from django.views.generic import TemplateView # type: ignore
from ntpweb.views import favicon_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ntpweb.urls')),  # Include app-specific URLs
    # Add any other global URLs here
    path('favicon.ico', favicon_view),
    
    # Serve React frontend for all other unmatched paths
   re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]

