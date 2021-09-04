from django.shortcuts import render
from clientes.models import Clientes

# Create your views here.
#Cargar los clientes
def clientes(request):
	clientes = Clientes.objects.all()
	context = {'clientes': clientes}
	return render(request, 'clientes/clientes.html', context)