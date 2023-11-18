from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from articulos_blog.models import *

class FormularioArticulo(forms.Form):
    titulo = forms.CharField(required=True, max_length=256)
    subtitulo = forms.CharField(required=True, max_length=256)
    cuerpo = forms.CharField(required=True, max_length=10000)
    autor = forms.CharField(required=True, max_length=256)
    fecha = forms.DateField(required=True)
    imagen = forms.ImageField(required=False)