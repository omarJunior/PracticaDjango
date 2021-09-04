from django.contrib import admin
from conductores.models import Conductores

# Register your models here.
class ConductorAdmin(admin.ModelAdmin):
    list_display=('codigo','nombre','apellidos','edad','telefono')
    list_filter=('apellidos',)
    search_fields=('nombre',)
    
admin.site.register(Conductores,ConductorAdmin)  
