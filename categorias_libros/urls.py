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
    path('eliminar-bios/<int:id>/', eliminar_bios, name="eliminar_bios"),
    path('eliminar-ficcion/<int:id>/', eliminar_ficcion, name="eliminar_ficcion"),
    path('eliminar-infantil/<int:id>/', eliminar_infantil, name="eliminar_infantil"),
    path('eliminar-poesia/<int:id>/', eliminar_poesia, name="eliminar_poesia"),
    path('eliminar-filo/<int:id>/', eliminar_filo, name="eliminar_filo"),
    path('editar-bios/<int:id>/', editar_bios, name="editar_bios"),
    path('editar-ficcion/<int:id>/', editar_ficcion, name="editar_ficcion"),
    path('editar-infantil/<int:id>/', editar_infantil, name="editar_infantil"),
    path('editar-poesia/<int:id>/', editar_poesia, name="editar_poesia"),
    path('editar-filo/<int:id>/', editar_filo, name="editar_filo"),
    path('detalles-bios/<int:pk>', BiografiaDetailView.as_view(), name="detalles_bios"),
    path('detalles-ficcion/<int:pk>', FiccionDetailView.as_view(), name="detalles_ficcion"),
    path('detalles-poesia/<int:pk>', PoesiaDetailView.as_view(), name="detalles_poesia"),
    path('detalles-infantil/<int:pk>', InfantilYJuvenilDetailView.as_view(), name="detalles_infantil"),
    path('detalles-filo/<int:pk>', FilosofiaYReligionDetailView.as_view(), name="detalles_filo"),
]