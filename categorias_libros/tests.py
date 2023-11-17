from django.test import TestCase

from categorias_libros.models import *


class FiccionTests(TestCase):

   def test_creacion_ficcion(self):
       # caso uso esperado
       ficcion = Ficcion(genero='genero', nombre='nombrelibro', autor='autorx', año_publicacion=1980, sinopsis='sinopsisxx')
       ficcion.save()


       self.assertEqual(Ficcion.objects.count(), 1)
       self.assertEqual(ficcion.genero, "genero")
       self.assertEqual(ficcion.nombre, "nombrelibro")
       self.assertEqual(ficcion.autor, "autorx")
       self.assertEqual(ficcion.año_publicacion, 1980)
       self.assertEqual(ficcion.sinopsis, "sinopsisxx")

   def test_curso_str(self):
       ficcion = Ficcion(genero='fantasia', nombre='Harry Potter', autor='JK Rowling', año_publicacion=2001, sinopsis='niño mago')
       ficcion.save()

       # Compruebo el str funciona como se desea
       self.assertEqual(ficcion.__str__(), "Harry Potter (JK Rowling)")
