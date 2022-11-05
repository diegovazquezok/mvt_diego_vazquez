from django.http import HttpResponse
from django.shortcuts import render
from .models import Familia

# Create your views here.



def inicio(request):
    familias=Familia.objects.all()
    return render(request, "appfamily/index.html", {"familias": familias})

#def listado_familias(request):
 #   familias = Familia.objects.all()

#    cadena_respuesta = ""
#   for familia in familias:
#        cadena_respuesta += familia.nombre + " | "
    
#    return HttpResponse(cadena_respuesta)

