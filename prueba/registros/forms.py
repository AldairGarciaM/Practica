from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from turtle import clear
from django import forms
from .models import ComentarioContacto, Archivos
from django.forms import ModelForm, ClearableFileInput

class ComentarioContactoForm(forms.ModelForm):
    class Meta:
        model= ComentarioContacto
        fields= ['usuario', 'mensaje']

class CustomCleareFlied(ClearableFileInput):
    template_with_clear='<br><label for= "%(clear_checkbox_id)s">%(clear_checkbox_label)s </label>%(clear)s'

class formArchivo(ModelForm):
    class Meta:
        model= Archivos
        fields=('titulo', 'descripcion', 'archivo')
        widgets={ 'archivo': CustomCleareFlied}