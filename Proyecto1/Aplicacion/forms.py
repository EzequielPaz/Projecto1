#Cree un archivo 'forms.py' para crear los formularios correspondientes a los modelos
from django import forms 

class CursoForm(forms.ModelForm):
    nombre = forms.CharField()
    camada = forms.IntegerField()
class AlumnoForm(forms.ModelForm):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class ChefForm(forms.ModelForm):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    edad = forms.IntegerField()