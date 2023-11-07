from django.urls import path
from Aplicacion.views import *


urlpatterns = [
    path('', inicio),
    path('cursos/', cursos),
    path('chefs/', chefs),
    path('alumnos/', alumnos),
    path('curso/',curso),
#Url de los formularios    
    path('cursoForm/',cursoForm, name='cursoForm'),
    path('alumnoForm/',alumnoForm, name='alumnoForm'),
    path('chefForm/', chefForm, name='chefForm')
]
    

