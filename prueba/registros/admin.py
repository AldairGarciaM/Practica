from django.contrib import admin
from .models import Alumnos
from .models import Comentarios
from .models import ComentarioContacto
from .models import Archivos

# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields= ('created', 'update')
    list_display= ('matricula','image', 'nombre', 'carrera', 'turno', 'created')
    search_fields= ('image', 'matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy= 'created'
    list_filter= ('carrera', 'turno')

    def get_readonly_field(self, request, obj=None):
        if request.user.groups.filter(name="Usuarios").exists():
            return ('created', 'update', 'matricula', 'carrera', 'turno')
        else:
            return ('created', 'update')

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

admin.site.register(Archivos)