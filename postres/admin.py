from django.contrib import admin
from postres.models import Postres

# Register your models here.
class PostreAdmin(admin.ModelAdmin):
    list_display=('nombre','precio','stock','created_at','updated_at')
    list_filter=('nombre',)
    search_fields=('precio',)
    
admin.site.register(Postres,PostreAdmin)  

