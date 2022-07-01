from distutils.command.upload import upload
from turtle import update
from django.db import models

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