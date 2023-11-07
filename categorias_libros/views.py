from django.shortcuts import render, redirect
from django.urls import reverse
from categorias_libros.models import *
from categorias_libros.forms import *
from django.db.models import Q

def listar_libros_ficcion(request):
    contexto = {
        "libros_ficcion": Ficcion.objects.all()
    }
    http_response = render(
        request=request,
        template_name='categorias_libros/lista_libros_ficcion.html',
        context=contexto
    )
    return http_response

def listar_libros_poesia(request):
    contexto = {
        "libros_poesia": Poesia.objects.all()
    }
    http_response = render(
        request=request,
        template_name='categorias_libros/lista_libros_poesia.html',
        context=contexto
    )
    return http_response

def listar_libros_bios(request):
    contexto = {
        "libros_bios": Biografia.objects.all()
    }
    http_response = render(
        request=request,
        template_name='categorias_libros/lista_libros_bios.html',
        context=contexto
    )
    return http_response

def listar_libros_filo(request):
    contexto = {
        "libros_filo": FilosofiaYReligion.objects.all()
    }
    http_response = render(
        request=request,
        template_name='categorias_libros/lista_libros_filo.html',
        context=contexto
    )
    return http_response

def listar_libros_infantil(request):
    contexto = {
        "libros_infantil": InfantilYJuvenil.objects.all()
    }
    http_response = render(
        request=request,
        template_name='categorias_libros/lista_libros_infantil.html',
        context=contexto
    )
    return http_response


def ingresar_libro_ficcion(request):
   if request.method == "POST":
       formulario = FormularioFiccion(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           genero = data['genero']
           nombre = data['nombre']
           autor = data['autor']
           año_publicacion = data['año_publicacion']
           sinopsis = data['sinopsis']
           reseña = data['reseña']
           libro_ficcion = Ficcion(genero=data['genero'], nombre=data['nombre'], autor=data['autor'], año_publicacion=data['año_publicacion'], sinopsis=data['sinopsis'], reseña=data['reseña'])
           libro_ficcion.save()
           url_exitosa = reverse('ficcion')
           return redirect(url_exitosa)
   else:  # GET
       formulario = FormularioFiccion()
   http_response = render(
       request=request,
       template_name='categorias_libros/ingreso_libro_ficcion.html',
       context={'formulario': formulario}
   )
   return http_response


def ingresar_libro_bios(request):
   if request.method == "POST":
       formulario = FormularioBiografia(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data['nombre']
           autor = data['autor']
           año_publicacion = data['año_publicacion']
           sinopsis = data['sinopsis']
           reseña = data['reseña']
           libro_bios = Biografia(nombre=data['nombre'], autor=data['autor'], año_publicacion=data['año_publicacion'], sinopsis=data['sinopsis'], reseña=data['reseña'])
           libro_bios.save()
           url_exitosa = reverse('biografias')
           return redirect(url_exitosa)
   else:  # GET
       formulario = FormularioBiografia()
   http_response = render(
       request=request,
       template_name='categorias_libros/ingreso_libro_bios.html',
       context={'formulario': formulario}
   )
   return http_response

def ingresar_libro_poesia(request):
   if request.method == "POST":
       formulario = FormularioPoesia(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data['nombre']
           autor = data['autor']
           año_publicacion = data['año_publicacion']
           sinopsis = data['sinopsis']
           reseña = data['reseña']
           libro_poesia = Poesia(nombre=data['nombre'], autor=data['autor'], año_publicacion=data['año_publicacion'], sinopsis=data['sinopsis'], reseña=data['reseña'])
           libro_poesia.save()
           url_exitosa = reverse('poesia')
           return redirect(url_exitosa)
   else:  # GET
       formulario = FormularioPoesia()
   http_response = render(
       request=request,
       template_name='categorias_libros/ingreso_libro_poesia.html',
       context={'formulario': formulario}
   )
   return http_response

def ingresar_libro_filo(request):
   if request.method == "POST":
       formulario = FormularioFilosofiaYReligion(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data['nombre']
           autor = data['autor']
           año_publicacion = data['año_publicacion']
           descripcion = data['descripcion']
           reseña = data['reseña']
           libro_filo = FilosofiaYReligion(nombre=data['nombre'], autor=data['autor'], año_publicacion=data['año_publicacion'], descripcion=data['descripcion'], reseña=data['reseña'])
           libro_filo.save()
           url_exitosa = reverse('filosofia-y-religion')
           return redirect(url_exitosa)
   else:  # GET
       formulario = FormularioFilosofiaYReligion()
   http_response = render(
       request=request,
       template_name='categorias_libros/ingreso_libro_filo.html',
       context={'formulario': formulario}
   )
   return http_response


def ingresar_libro_infantil(request):
   if request.method == "POST":
       formulario = FormularioInfantilYJuvenil(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           genero = data['genero']
           nombre = data['nombre']
           autor = data['autor']
           año_publicacion = data['año_publicacion']
           sinopsis = data['sinopsis']
           reseña = data['reseña']
           libro_infantil = InfantilYJuvenil(genero=data['genero'], nombre=data['nombre'], autor=data['autor'], año_publicacion=data['año_publicacion'], sinopsis=data['sinopsis'], reseña=data['reseña'])
           libro_infantil.save()
           url_exitosa = reverse('infantil-y-juvenil')
           return redirect(url_exitosa)
   else:  # GET
       formulario = FormularioInfantilYJuvenil()
   http_response = render(
       request=request,
       template_name='categorias_libros/ingreso_libro_infantil.html',
       context={'formulario': formulario}
   )
   return http_response


def buscar_libro_ficcion(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data['busqueda']
        libros_ficcion = Ficcion.objects.filter(Q(nombre__icontains=busqueda) | Q(autor__icontains=busqueda))
        contexto = {
            "libros_ficcion": libros_ficcion,
        }
        http_response = render(
            request=request,
            template_name='categorias_libros/lista_libros_ficcion.html',
            context=contexto,
        )
        return http_response
    
def buscar_libro_bios(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data['busqueda']
        libros_bios = Biografia.objects.filter(Q(nombre__icontains=busqueda) | Q(autor__icontains=busqueda))
        contexto = {
            "libros_bios": libros_bios,
        }
        http_response = render(
            request=request,
            template_name='categorias_libros/lista_libros_bios.html',
            context=contexto,
        )
        return http_response
    
def buscar_libro_filo(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data['busqueda']
        libros_filo = FilosofiaYReligion.objects.filter(Q(nombre__icontains=busqueda) | Q(autor__icontains=busqueda))
        contexto = {
            "libros_filo": libros_filo,
        }
        http_response = render(
            request=request,
            template_name='categorias_libros/lista_libros_filo.html',
            context=contexto,
        )
        return http_response
    
def buscar_libro_poesia(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data['busqueda']
        libros_poesia = Poesia.objects.filter(Q(nombre__icontains=busqueda) | Q(autor__icontains=busqueda))
        contexto = {
            "libros_poesia": libros_poesia,
        }
        http_response = render(
            request=request,
            template_name='categorias_libros/lista_libros_poesia.html',
            context=contexto,
        )
        return http_response
    
def buscar_libro_infantil(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data['busqueda']
        libros_infantil = InfantilYJuvenil.objects.filter(Q(nombre__icontains=busqueda) | Q(autor__icontains=busqueda))
        contexto = {
            "libros_infantil": libros_infantil,
        }
        http_response = render(
            request=request,
            template_name='categorias_libros/lista_libros_infantil.html',
            context=contexto,
        )
        return http_response