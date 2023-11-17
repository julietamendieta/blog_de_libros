from django.db import models
from django.contrib.auth.models import User

class Articulo(models.Model):
    titulo = models.CharField(max_length=256)
    subtitulo = models.CharField(max_length=256)
    cuerpo = models.TextField(null=True)
    autor = models.CharField(max_length=256)
    fecha = models.DateField(null=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)