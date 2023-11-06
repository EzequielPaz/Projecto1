from django.shortcuts import render
from Aplicacion.models import Curso, Alumno, Chef
from django.http import HttpResponse

# Create your views here.
def curso(self):
    curso = Curso(nombre="Pasteleria", camada=1000)
    curso.save()
    documentoDeTexto = f"----->Curso {curso.nombre} Camada {curso.camada}" 
    return HttpResponse(documentoDeTexto)

def inicio(request):
    return render(request, "Aplicacion/index.html")

def cursos(request):
    return HttpResponse('vista cursos')

def chefs(request):
    return HttpResponse('vista chefs')

def alumnos(request):
    return render(request, "Aplicacion/alumnos.html")

