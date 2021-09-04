from django.shortcuts import render
from conductores.models import Conductores

# Create your views here.

#Cargar los conductores
def conductores(request):
	conductores = Conductores.objects.all()
	context = {'conductores': conductores}
	return render(request, 'conductores/conductores.html', context)