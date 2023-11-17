from django.urls import path
from articulos_blog.views import *

urlpatterns = [
    path('articulos/', listar_articulos, name="articulos"),
    path('nuevo-articulo/', escribir_articulo, name="nuevo_articulo"),
    path('buscar-articulo/', buscar_articulo, name="buscar_articulo"),
    path('eliminar-articulo/<int:id>/', eliminar_articulo, name="eliminar_articulo"),
    path('editar-articulo/<int:id>/', editar_articulo, name="editar_articulo"),
    path('detalle-articulo/<int:pk>', ArticuloDetailView.as_view(), name="detalle_articulo"),
]