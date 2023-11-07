from django.urls import path
from categorias_libros.views import *

urlpatterns = [
    path('ficcion/', listar_libros_ficcion, name="ficcion"),
    path('poesia/', listar_libros_poesia, name="poesia"),
    path('biografias/', listar_libros_bios, name="biografias"),
    path('infantil-y-juvenil/', listar_libros_infantil, name="infantil-y-juvenil"),
    path('filosofia-y-religion/', listar_libros_filo, name="filosofia-y-religion"),
    path('ingresar-libro-ficcion/', ingresar_libro_ficcion, name="ingresar_libro_ficcion"),
    path('ingresar-libro-filo/', ingresar_libro_filo, name="ingresar_libro_filo"),
    path('ingresar-libro-poesia/', ingresar_libro_poesia, name="ingresar_libro_poesia"),
    path('ingresar-libro-bios/', ingresar_libro_bios, name="ingresar_libro_bios"),
    path('ingresar-libro-infantil/', ingresar_libro_infantil, name="ingresar_libro_infantil"),
    path('buscar-libro-ficcion/', buscar_libro_ficcion, name="buscar_libro_ficcion"),
    path('buscar-libro-bios/', buscar_libro_bios, name="buscar_libro_bios"),
    path('buscar-libro-filo/', buscar_libro_filo, name="buscar_libro_filo"),
    path('buscar-libro-infantil/', buscar_libro_infantil, name="buscar_libro_infantil"),
    path('buscar-libro-poesia/', buscar_libro_poesia, name="buscar_libro_poesia"),
]