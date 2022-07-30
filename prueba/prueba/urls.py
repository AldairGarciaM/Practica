"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from registros import views as views_registros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_registros.registros, name="Principal"),
    path('contacto/', views_registros.contacto, name="Contacto"),
    path('formulario/', views.formulario, name="Formulario"),
    path('ejemplo/', views.ejemplo, name="Ejemplo"),
    path('registrar/', views_registros.registrar, name="Registrar"),
    path('comentarios/', views_registros.comentarios, name="Comentarios"),
    path('eliminarComentario/<int:id>/', views_registros.elimnarComentarios, name="Eliminar"),
    path('consultarComentario/<int:id>/', views_registros.consultarComentario, name="consultaComentario" ),
    path('editarComentario/<int:id>/', views_registros.editarComentario, name="Editar" ),
    path('consulta1/', views_registros.consulta1, name="Consulta1"),
    path('consulta2/', views_registros.consulta2, name="Consulta2"),
    path('consulta3/', views_registros.consulta3, name="Consulta3"),
    path('consulta4/', views_registros.consulta4, name="Consulta4"),
    path('consulta5/', views_registros.consulta5, name="Consulta5"),
    path('consulta6/', views_registros.consulta6, name="Consulta6"),
    path('consulta7/', views_registros.consulta7, name="Consulta7"),
    path('subir/', views_registros.archivos, name="Subir"),
    path('SQL/', views_registros.consultasSQL, name="sql"),
    
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)