from distutils.command.upload import upload
from tabnanny import verbose
from turtle import update
from venv import create
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Alumnos(models.Model): #Definir la estructura de la tabla
    matricula= models.CharField(max_length=12) #Texto corto
    nombre= models.TextField() #Texto largo
    carrera= models.TextField()
    turno= models.CharField(max_length=10)
    image= models.ImageField(null= True, upload_to="fotos", verbose_name="Imagen")
    created= models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    update= models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name= "Alumno"
        verbose_name_plural= "Alumnos"
        ordering= ["-created"] 

    def __str__(self):
        return self.nombre


class Comentarios(models.Model):
    id= models.AutoField(primary_key=True, verbose_name="Llave")
    alumno= models.ForeignKey(Alumnos, on_delete=models.CASCADE,verbose_name="Alumno")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Registros")
    coment= RichTextField(verbose_name="Comentario")

    class Meta:
        verbose_name= "Comentario"
        verbose_name_plural= "Comentarios"
        ordering= ["-created"]

    def __str__(self):
        return self.coment


class ComentarioContacto(models.Model):
    id= models.AutoField(primary_key=True, verbose_name="Clave")
    usuario= models.TextField(verbose_name="Usaurio")
    mensaje= models.TextField(verbose_name="Comentario")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Registros")

    class Meta: 
        verbose_name= "Comentario Contacto"
        verbose_name_plural= "Comentarios Contactos"
        ordering= ["-created"]

    def __str__(self):
        return self.mensaje

class Archivos(models.Model):
    id= models.AutoField(primary_key=True, verbose_name="ID")
    titulo= models.CharField(max_length=50, verbose_name="Titulo")
    descripcion= models.CharField(max_length=50, verbose_name="Descripcion")
    archivo= models.FileField(upload_to="archivos", null=True, blank=True)
    create=models.DateTimeField(auto_now_add=True, verbose_name="Creacion")
    update=models.DateTimeField(auto_now_add=True, verbose_name="Actualizacion")

    class Meta:
        verbose_name="Archivo"
        verbose_name_plural="Archivos"
        ordering=["-create"]

    def __str__(self):
        return self.titulo