from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from articulos_blog.models import *
from articulos_blog.forms import *
from django.db.models import Q
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required

def listar_articulos(request):
    contexto = {
        "articulos": Articulo.objects.all()
    }
    http_response = render(
        request=request,
        template_name='articulos_blog/lista_articulos.html',
        context=contexto
    )
    return http_response

@login_required
def escribir_articulo(request):
   if request.method == "POST":
       formulario = FormularioArticulo(request.POST, request.FILES)

       if formulario.is_valid():
           data = formulario.cleaned_data
           titulo = data['titulo']
           subtitulo = data['subtitulo']
           cuerpo = data['cuerpo']
           autor = data['autor']
           fecha = data['fecha']
           imagen = data['imagen']
           articulo = Articulo(titulo=data['titulo'], subtitulo=data['subtitulo'], cuerpo=data['cuerpo'], autor=data['autor'], fecha=data['fecha'], imagen=data['imagen'], creador=request.user)
           articulo.save()
           url_exitosa = reverse('articulos')
           return redirect(url_exitosa)
   else:  # GET
       formulario = FormularioArticulo()
   http_response = render(
       request=request,
       template_name='articulos_blog/nuevo_articulo.html',
       context={'formulario': formulario}
   )
   return http_response

def buscar_articulo(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data['busqueda']
        articulo = Articulo.objects.filter(Q(nombre__icontains=busqueda) | Q(autor__icontains=busqueda))
        contexto = {
            "articulos": articulo,
        }
        http_response = render(
            request=request,
            template_name='articulos_blog/lista_articulos.html',
            context=contexto,
        )
        return http_response
    
@login_required
def eliminar_articulo(request, id):
    articulo = Articulo.objects.get(id=id)
    if request.method == "POST":
        articulo.delete()
        url_exitosa = reverse('articulos')
        return redirect(url_exitosa)
    
@login_required
def editar_articulo(request, id):
   articulo = Articulo.objects.get(id=id)
   if request.method == "POST":
       formulario = FormularioArticulo(request.POST, request.FILES)

       if formulario.is_valid():
           data = formulario.cleaned_data
           articulo.titulo = data['titulo']
           articulo.subtitulo = data['subtitulo']
           articulo.cuerpo = data['cuerpo']
           articulo.autor = data['autor']
           articulo.fecha = data['fecha']
           articulo.imagen = data['imagen']
           articulo.save()
           url_exitosa = reverse('articulos')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'titulo': articulo.titulo,
           'subtitulo': articulo.subtitulo,
           'cuerpo': articulo.cuerpo,
           'autor': articulo.autor,
           'fecha': articulo.fecha,
           'imagen': articulo.imagen,
       }
       formulario = FormularioArticulo(initial=inicial)
   return render(
       request=request,
       template_name='articulos_blog/nuevo_articulo.html',
       context={'formulario': formulario},
   )

class ArticuloDetailView(DetailView):
    model = Articulo
    success_url = reverse_lazy('articulos')
