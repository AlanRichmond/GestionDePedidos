from django.contrib import admin
from .models import Servicio

# Register your models here.

class Servicio_Admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Servicio, Servicio_Admin) #PARA AGREGAR SERVICIOS A ADMIN

