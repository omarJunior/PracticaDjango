from django.shortcuts import render
from reparaciones.models import Reparaciones #Estoy en esta carpeta actual

# Create your views here.
def index(request):
	return render(request, 'home.html')

def reparaciones(request):
	reparaciones = Reparaciones.objects.all()
	context = { 'reparaciones': reparaciones }
	return render(request, "reparaciones/reparaciones.html", context)
