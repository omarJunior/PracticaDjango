from django.contrib import admin
from helados.models import Helados

# Register your models here.
class HeladoAdmin(admin.ModelAdmin):
    list_display=('nombre','precio','stock','created_at','updated_at')
    list_filter=('nombre',)
    search_fields=('precio',)
    
admin.site.register(Helados,HeladoAdmin)  

