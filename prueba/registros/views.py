from django.shortcuts import render
from .models import Alumnos, ComentarioContacto
from .forms import ComentarioContactoForm
from django.shortcuts import get_object_or_404


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
