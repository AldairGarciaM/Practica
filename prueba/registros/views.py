from django.shortcuts import render
from .models import Alumnos, ComentarioContacto, Archivos
from .forms import ComentarioContactoForm, formArchivo
from django.shortcuts import get_object_or_404
import datetime
from django.contrib import messages


# Create your views here.

def registros(request):
    alumnos= Alumnos.objects.all()
    
    return render(request, "registros/principal.html", {'alumnos': alumnos})

def comentarios(request):
    comentarios= ComentarioContacto.objects.all()

    return render(request, "registros/comantarios.html", {'comentarios': comentarios})


def contacto(request):

    return render(request,"registros/contacto.html")


def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            comentarios= ComentarioContacto.objects.all()
            return render(request, 'registros/comantarios.html', {'comentarios': comentarios})
    form= ComentarioContactoForm()

    return render(request, 'registros/contacto.html', {'form': form})


def elimnarComentarios(request, id, confirmacion= 'registros/confirmarEliminacion.html'):
    comentario= get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios= ComentarioContacto.objects.all()
        return render(request, "registros/comantario.html", {'comentarios': comentarios})
    return render(request, confirmacion, {'object': comentario})


    
def consultarComentario(request,id):
    comentario= ComentarioContacto.objects.get(id=id)
    return render(request, "registros/editarComentario.html", {'comentario': comentario})

def editarComentario(request, id):
    comentario= get_object_or_404(ComentarioContacto, id=id)
    form= ComentarioContactoForm(request.POST, instance=comentario)

    if form.is_valid():
        form.save()
        comentarios= ComentarioContacto.objects.all()

        return render(request, "registros/comantarios.html", {'comentarios': comentarios})

    return render(request, "registros/editarComentario.html", {'comentario': comentario})


def consulta1(request):
    alumnos= Alumnos.objects.filter(carrera="TI")
    
    return render(request, "registros/principal.html", {'alumnos': alumnos})

def consulta2(request):
    alumnos= Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    
    return render(request, "registros/principal.html", {'alumnos': alumnos})

def consulta3(request):
    alumnos= Alumnos.objects.all().only("matricula", "nombre", "carrera", "turno", "image")
    
    return render(request, "registros/principal.html", {'alumnos': alumnos})

def consulta4(request):
    alumnos= Alumnos.objects.filter(turno__contains="Vesp")
    
    return render(request, "registros/principal.html", {'alumnos': alumnos})

def consulta5(request):
    alumnos= Alumnos.objects.filter(nombre__in=["Juan", "Ana"])
    
    return render(request, "registros/principal.html", {'alumnos': alumnos})

def consulta6(request):
    fechainicio= datetime.date(2022, 7, 1)
    fechafin= datetime.date(2022, 7, 13)
    alumnos= Alumnos.objects.filter(created__range=(fechainicio, fechafin))
    
    return render(request, "registros/principal.html", {'alumnos': alumnos})

def consulta7(request):
    alumnos= Alumnos.objects.filter(comentarios__coment__contains="Este sitio esta chido")
    
    return render(request, "registros/principal.html", {'alumnos': alumnos})


def archivos(request):
    if request.method=='POST':
        form= formArchivo(request.POST, request.FILES)
        if form.is_valid():
            titulo=request.POST['titulo']
            descripcion= request.POST['descripcion']
            archivo= request.FILES['archivo']
            insert= Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
            insert.save()
            return render(request, "registros/archivos.html")
        else:
            messages.error(request, "Error al procesar el archivo.")
    else:
        return render(request, "registros/archivos.html", {'archivo': Archivos})


def consultasSQL(request):
    alumnos= Alumnos.objects.raw('SELECT id, matricula, nombre, carrera, turno, image FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')

    return render(request, 'registros/consultas.html', {'alumnos': alumnos})


def seguridad(request, nombre=None):
    nombre= request.GET.get('nombre')

    return render(request, 'registros/seguridad.html', {'nombre': nombre})