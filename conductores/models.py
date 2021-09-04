from django.db import models

# Create your models here.
class Conductores(models.Model):
	codigo = models.CharField(max_length = 60 ) 
	nombre = models.CharField(max_length = 100)
	apellidos = models.CharField(max_length= 100)
	edad = models.IntegerField()
	ciudad = models.CharField(max_length = 100)
	direccion = models.CharField(max_length = 80)
	telefono = models.CharField(max_length = 80)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.nombre + " " + self.apellidos

	class Meta:
		db_table = 'conductores'
	