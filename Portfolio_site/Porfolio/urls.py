"""
URL configuration for Ecommerce_Site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static



urlpatterns = [
                  path('', views.home, name='home'),
                  path('profolio_details', views.portfoliodet, name='portfolio_details'),
                  path('contact', views.contactMe, name='contact'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)