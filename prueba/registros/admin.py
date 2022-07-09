from django.contrib import admin
from .models import Alumnos
from .models import Comentarios
from .models import ComentarioContacto

# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields= ('created', 'update')
    list_display= ('image', 'matricula', 'nombre', 'carrera', 'turno')
    search_fields= ('image', 'matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy= 'created'
    list_filter= ('carrera', 'turno')

class administraComentarios(admin.ModelAdmin):
    list_display= ('id', 'coment')
    search_fields= ('id', 'created')
    date_hierarchy= 'created'
    readonly_fields= ('created', 'id')


class comentarioContacto(admin.ModelAdmin):
    list_display= ('id', 'mensaje')
    search_fields= ('id', 'created')
    date_hierarchy= 'created'
    readonly_fields= ('created', 'id')

admin.site.register(Alumnos, AdministrarModelo)

admin.site.register(Comentarios, administraComentarios)

admin.site.register(ComentarioContacto, comentarioContacto)