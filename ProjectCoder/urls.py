"""
URL configuration for ProjectCoder project.

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
from django.contrib import admin
from django.urls import path
from AppCoder.views import index, form_proveedor, form_dispositivo, form_sitio, buscar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('agregar-proveedor/', form_proveedor, name='agregar_proveedor'),
    path('agregar-dispositivo/', form_dispositivo, name='agregar_dispositivo'),
    path('agregar-sitio/', form_sitio, name='agregar_sitio'),
    path('buscar/', buscar, name='buscar'),
]