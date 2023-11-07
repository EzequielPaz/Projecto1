
#Importo de django modelos
from django.db import models
#Cree 3 modelos: Curso, alumno y chef
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    
class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    
class Chef(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    edad = models.IntegerField()