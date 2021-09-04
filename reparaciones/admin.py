from django.contrib import admin
from reparaciones.models import Reparaciones

# Register your models here.
class ReparacionAdmin(admin.ModelAdmin):
    list_display=('fecha','observacion','costo','vehiculo')
    list_filter=('costo',)
    search_fields=('vehiculo',)
    
admin.site.register(Reparaciones, ReparacionAdmin)  

