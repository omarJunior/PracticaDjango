from django.contrib import admin
from clientes.models import Clientes

# Register your models here.

class ClienteAdmin (admin.ModelAdmin):
    list_display=('nombre','apellidos','correo','direccion','telefono')
    list_filter=('apellidos',)
    search_fields=('nombre',)
admin.site.register(Clientes,ClienteAdmin)  
