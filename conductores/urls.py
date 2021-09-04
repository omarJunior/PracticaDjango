from django.urls import path
from . import views

urlpatterns = [
	path('', views.conductores, name="conductores")
]