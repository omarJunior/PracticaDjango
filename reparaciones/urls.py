from django.urls import path
from . import views

urlpatterns = [
	path('', views.reparaciones, name="reparaciones")
]