from django.urls import path
from Aplicacion.views import *

urlpatterns = [
    path('', inicio),
    path('cursos/', cursos),
    path('chefs/', chefs),
    path('alumnos/', alumnos),
    path('curso/',curso)
    
]

    

