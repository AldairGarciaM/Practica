from django.contrib import admin
from .models import Alumnos

# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields= ('created', 'update')
    list_display= ('image', 'matricula', 'nombre', 'carrera', 'turno')
    search_fields= ('image', 'matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy= 'created'
    list_filter= ('carrera', 'turno')

admin.site.register(Alumnos, AdministrarModelo)