from django.test import TestCase

from articulos_blog.models import *


class ArticuloTests(TestCase):

   def test_creacion_articulo(self):
       articulo = Articulo(titulo='titulo', subtitulo='subtitulo', cuerpo='cuerpo', autor='autorx', fecha='2023-11-11', imagen='imagen')
       articulo.save()


       self.assertEqual(Articulo.objects.count(), 1)
       self.assertEqual(articulo.titulo, 'titulo')
       self.assertEqual(articulo.subtitulo, 'subtitulo')
       self.assertEqual(articulo.cuerpo, 'cuerpo')
       self.assertEqual(articulo.autor, 'autorx')
       self.assertEqual(articulo.fecha, '2023-11-11')
       self.assertEqual(articulo.imagen, 'imagen')

   def test_curso_str(self):
       articulo = Articulo(titulo='Libros Antiguos', subtitulo='Los libros antiguos volvieron para quedarse', cuerpo='Este es el cuerpo del artículo de libros antiguos', autor='Julio Pérez', fecha='2023-11-19', imagen='una_imagen')
       articulo.save()

       self.assertEqual(articulo.__str__(), "Libros Antiguos (Julio Pérez)")