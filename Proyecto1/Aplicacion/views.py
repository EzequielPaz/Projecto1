from django.shortcuts import redirect, render
from Aplicacion.models import Curso, Alumno, Chef
from django.http import HttpResponse
from Aplicacion.forms import *

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

def cursoForm(request):
    if request.method == 'POST':
        curso = Curso(nombre=request.POST['curso'], camada=request.POST['camada'])
        curso.save()
        return render(request, "Aplicacion/index.html")
    return render(request, "Aplicacion/cursoForm.html")

def alumnoForm(request):
    if request.method == 'POST':
        miFormulario = AlumnoForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            info = Alumno(nombre = info['nombre'], apellido = info['apellido'], email = info['email'])
            info.save()
            return render(request, 'Aplicacion/index.html')
    else:
        miFormulario = AlumnoForm()
    return render(request, "Aplicacion/alumnoForm.html",{'miFormulario':miFormulario})

def chefForm(request):
    if request.method == 'POST':
        miFormulario = ChefForm(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            data = Chef(nombre = data['nombre'], apellido = data['apellido'], email = data['email'], edad = data['edad'])
            data.save()
            return render(request, 'Aplicacion/index.html')
    else:
        miFormulario = ProfesorForm()
    return render(request, 'Aplicacion/chefForm.html', {"miFormulario":miFormulario})

        
        
