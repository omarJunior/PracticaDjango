from django.db import models
from clientes.models import Clientes
from conductores.models import Conductores


# Create your models here.
class Vehiculos(models.Model):
	placa = models.CharField(max_length = 60)
	modelo = models.CharField(max_length = 65)
	marca = models.CharField(max_length = 65)
	color = models.CharField(max_length = 60)
	precio = models.DecimalField(max_digits = 5, decimal_places = 2)
	descripcion = models.TextField()
	cliente = models.ForeignKey(Clientes, null = True, blank = True, on_delete= models.CASCADE)
	conductor = models.ForeignKey(Conductores,null = True, blank = True, on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.placa + " " + self.marca + " " + str(self.cliente) + " " + str(self.conductor)

	class Meta:
		db_table = 'vehiculos' 

	