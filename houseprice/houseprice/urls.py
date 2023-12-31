"""
URL configuration for houseprice project.

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
from django import views
from django.contrib import admin
from django.urls import path,include
from . import views 
from django.conf import settings 
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('house.urls')),
    path('', views.home),
    path('predict/', views.predict),
    path('predict/result/',views.result, name='result'),
    path('properties/', views.property_list, name='property_list'),    
    path('add_property/', views.add_property, name='add_property'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

