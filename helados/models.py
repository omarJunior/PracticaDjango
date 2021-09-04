from django.db import models

# Create your models here.
class Helados(models.Model):
    nombre = models.CharField(max_length=100, default='DEFAULT VALUE')
    precio = models.DecimalField(max_digits = 5, decimal_places = 2)
    stock = models.CharField(max_length=100, default='DEFAULT VALUE')
    img = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre + " " + str(self.precio)

    class Meta:
    	db_table = 'helados'