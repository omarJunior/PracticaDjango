from django.db import models
from postres.models import Postres
from helados.models import Helados

# Create your models here.
#Creacion de la tabla en la base de datos
class Clientes(models.Model):
	nombre = models.CharField(max_length = 100)
	apellidos = models.CharField(max_length= 100)
	correo = models.CharField(max_length = 100)
	edad = models.IntegerField()
	ciudad = models.CharField(max_length = 100)
	direccion = models.CharField(max_length = 80)
	telefono = models.CharField(max_length = 80)
	postre = models.ForeignKey(Postres, null = True, blank = True, on_delete= models.CASCADE) 
	helado = models.ForeignKey(Helados, null = True, blank = True, on_delete= models.CASCADE) 
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.nombre + " " + self.apellidos
	
	class Meta:
		db_table = 'clientes' #Nombre de la tabla en la base de datos
