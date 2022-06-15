from django.shortcuts import render, HttpResponse

# Create your views here.

menu="""
    <a href="/"> Home </a>
    <a href= "/contacto"> Contacto </a>
"""

def principal(request):
    contenido="<h1> Hola Django <h1>"
    return HttpResponse(menu + contenido)

def contacto(request):
    contenido="""<h2> Contacto </h2>
    <p>Nombre: <input type="text" name="nombre"> </p>
    <p>Mensaje: </p> <p> <textarea cols="50" rows="10"></textarea> </p>
    <p> <input type="Button" name="enviar" value="Enviar" /> </p>
    """
    return HttpResponse(contenido)
