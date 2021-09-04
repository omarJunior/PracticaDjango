from django.contrib import admin
from vehiculos.models import Vehiculos

# Register your models here.
class VehiculoAdmin(admin.ModelAdmin):
    list_display=('placa','modelo','marca','precio', 'cliente', 'conductor')
    list_filter=('modelo',)
    search_fields=('marca',)
    
admin.site.register(Vehiculos, VehiculoAdmin)  

