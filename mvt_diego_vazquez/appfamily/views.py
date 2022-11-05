from django.http import HttpResponse
from django.shortcuts import render
from .models import Familia

# Create your views here.

def home(request):
    familias=Familia.objects.all()
    #return HttpResponse("<h1>HOLA MUNDO!</h1>")
    return render(request,"lista_famlias.html", {"familias": familias})

#def listado_familias(request):
 #   familias = Familia.objects.all()

#    cadena_respuesta = ""
#   for familia in familias:
#        cadena_respuesta += familia.nombre + " | "
    
#    return HttpResponse(cadena_respuesta)

