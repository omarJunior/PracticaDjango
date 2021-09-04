from django.shortcuts import render
from vehiculos.models import Vehiculos

# Create your views here.
def vehiculos(request):
	vehiculos = Vehiculos.objects.all()
	context = { 'vehiculos': vehiculos }
	return render(request, 'vehiculos/vehiculos.html', context)