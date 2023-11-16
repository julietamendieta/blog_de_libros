from django.db import models

class Ficcion(models.Model):
    genero = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    autor = models.CharField(max_length=256)
    año_publicacion = models.IntegerField(blank=True, null=True)
    sinopsis = models.TextField(null=True)

    def __str__(self):
        return f"{self.nombre} ({self.autor})"
    
class Poesia(models.Model):
    nombre = models.CharField(max_length=256)
    autor = models.CharField(max_length=256)
    año_publicacion = models.IntegerField(blank=True, null=True)
    sinopsis = models.TextField(null=True)

    def __str__(self):
        return f"{self.nombre} ({self.autor})"

class Biografia(models.Model):
    nombre = models.CharField(max_length=256)
    autor = models.CharField(max_length=256)
    año_publicacion = models.IntegerField(blank=True, null=True)
    sinopsis = models.TextField(null=True)

    def __str__(self):
        return f"{self.nombre} ({self.autor})"

class InfantilYJuvenil(models.Model):
    genero = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    autor = models.CharField(max_length=256)
    año_publicacion = models.IntegerField(blank=True, null=True)
    sinopsis = models.TextField(null=True)

    def __str__(self):
        return f"{self.nombre} ({self.autor})"

class FilosofiaYReligion(models.Model):
    nombre = models.CharField(max_length=256)
    autor = models.CharField(max_length=256)
    año_publicacion = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField(null=True)

    def __str__(self):
        return f"{self.nombre} ({self.autor})"


