"""django01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from reparaciones.views import index #Este metodo me va a renderizar la pagina inicial

urlpatterns = [
    path('', index, name="home"),
    path('clientes/', include("clientes.urls")), #Incluyo mis rutas 
    path('conductores/', include("conductores.urls")),
    path('reparaciones/', include("reparaciones.urls")),
    path('vehiculos/', include("vehiculos.urls")),
    path('admin/', admin.site.urls),
]
