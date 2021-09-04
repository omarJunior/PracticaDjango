from django.db import models
from vehiculos.models import Vehiculos

# Create your models here.
class Reparaciones(models.Model):
	fecha = models.DateField()
	observacion = models.TextField()
	costo = models.DecimalField(max_digits = 5, decimal_places = 2)
	vehiculo = models.ForeignKey(Vehiculos, null = True, blank = True, on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.fecha + " " + self.observacion + " "+ self.costo + " " + self.vehiculo
		
	class Meta:
		db_table = 'reparaciones'

	