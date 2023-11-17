from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from categorias_libros.models import *
from categorias_libros.forms import *
from django.db.models import Q
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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

@login_required
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
           libro_ficcion = Ficcion(genero=data['genero'], nombre=data['nombre'], autor=data['autor'], año_publicacion=data['año_publicacion'], sinopsis=data['sinopsis'])
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

@login_required
def ingresar_libro_bios(request):
   if request.method == "POST":
       formulario = FormularioBiografia(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data['nombre']
           autor = data['autor']
           año_publicacion = data['año_publicacion']
           sinopsis = data['sinopsis']
           libro_bios = Biografia(nombre=data['nombre'], autor=data['autor'], año_publicacion=data['año_publicacion'], sinopsis=data['sinopsis'])
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

@login_required
def ingresar_libro_poesia(request):
   if request.method == "POST":
       formulario = FormularioPoesia(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data['nombre']
           autor = data['autor']
           año_publicacion = data['año_publicacion']
           sinopsis = data['sinopsis']
           libro_poesia = Poesia(nombre=data['nombre'], autor=data['autor'], año_publicacion=data['año_publicacion'], sinopsis=data['sinopsis'])
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

@login_required
def ingresar_libro_filo(request):
   if request.method == "POST":
       formulario = FormularioFilosofiaYReligion(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data['nombre']
           autor = data['autor']
           año_publicacion = data['año_publicacion']
           descripcion = data['descripcion']
           libro_filo = FilosofiaYReligion(nombre=data['nombre'], autor=data['autor'], año_publicacion=data['año_publicacion'], descripcion=data['descripcion'])
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

@login_required
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
           libro_infantil = InfantilYJuvenil(genero=data['genero'], nombre=data['nombre'], autor=data['autor'], año_publicacion=data['año_publicacion'], sinopsis=data['sinopsis'])
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

@login_required
def eliminar_bios(request, id):
    bios = Biografia.objects.get(id=id)
    if request.method == "POST":
        bios.delete()
        url_exitosa = reverse('biografias')
        return redirect(url_exitosa)

@login_required
def eliminar_ficcion(request, id):
    ficcion = Ficcion.objects.get(id=id)
    if request.method == "POST":
        ficcion.delete()
        url_exitosa = reverse('ficcion')
        return redirect(url_exitosa)
    
@login_required
def eliminar_infantil(request, id):
    infantil = InfantilYJuvenil.objects.get(id=id)
    if request.method == "POST":
        infantil.delete()
        url_exitosa = reverse('infantil-y-juvenil')
        return redirect(url_exitosa)

@login_required  
def eliminar_poesia(request, id):
    poesia = Poesia.objects.get(id=id)
    if request.method == "POST":
        poesia.delete()
        url_exitosa = reverse('poesia')
        return redirect(url_exitosa)

@login_required   
def eliminar_filo(request, id):
    filo = FilosofiaYReligion.objects.get(id=id)
    if request.method == "POST":
        filo.delete()
        url_exitosa = reverse('filosofia-y-religion')
        return redirect(url_exitosa)

@login_required
def editar_infantil(request, id):
   infantil = InfantilYJuvenil.objects.get(id=id)
   if request.method == "POST":
       formulario = FormularioInfantilYJuvenilE(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           infantil.genero = data['genero']
           infantil.nombre = data['nombre']
           infantil.autor = data['autor']
           infantil.año_publicacion = data['año_publicacion']
           infantil.sinopsis = data['sinopsis']
           infantil.save()
           url_exitosa = reverse('infantil-y-juvenil')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'genero': infantil.genero,
           'nombre': infantil.nombre,
           'autor': infantil.autor,
           'año_publicacion': infantil.año_publicacion,
           'sinopsis': infantil.sinopsis,
       }
       formulario = FormularioInfantilYJuvenilE(initial=inicial)
   return render(
       request=request,
       template_name='categorias_libros/ingreso_libro_infantil.html',
       context={'formulario': formulario},
   )

@login_required
def editar_ficcion(request, id):
   ficcion = Ficcion.objects.get(id=id)
   if request.method == "POST":
       formulario = FormularioFiccionE(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           ficcion.genero = data['genero']
           ficcion.nombre = data['nombre']
           ficcion.autor = data['autor']
           ficcion.año_publicacion = data['año_publicacion']
           ficcion.sinopsis = data['sinopsis']
           ficcion.save()
           url_exitosa = reverse('ficcion')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'genero': ficcion.genero,
           'nombre': ficcion.nombre,
           'autor': ficcion.autor,
           'año_publicacion': ficcion.año_publicacion,
           'sinopsis': ficcion.sinopsis,
       }
       formulario = FormularioFiccionE(initial=inicial)
   return render(
       request=request,
       template_name='categorias_libros/ingreso_libro_ficcion.html',
       context={'formulario': formulario},
   )

@login_required
def editar_poesia(request, id):
   poesia = Poesia.objects.get(id=id)
   if request.method == "POST":
       formulario = FormularioPoesiaE(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           poesia.nombre = data['nombre']
           poesia.autor = data['autor']
           poesia.año_publicacion = data['año_publicacion']
           poesia.sinopsis = data['sinopsis']
           poesia.save()
           url_exitosa = reverse('poesia')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': poesia.nombre,
           'autor': poesia.autor,
           'año_publicacion': poesia.año_publicacion,
           'sinopsis': poesia.sinopsis,
       }
       formulario = FormularioPoesiaE(initial=inicial)
   return render(
       request=request,
       template_name='categorias_libros/ingreso_libro_poesia.html',
       context={'formulario': formulario},
   )

@login_required
def editar_filo(request, id):
   filo = FilosofiaYReligion.objects.get(id=id)
   if request.method == "POST":
       formulario = FormularioFilosofiaYReligionE(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           filo.nombre = data['nombre']
           filo.autor = data['autor']
           filo.año_publicacion = data['año_publicacion']
           filo.descripcion = data['descripcion']
           filo.save()
           url_exitosa = reverse('filosofia-y-religion')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': filo.nombre,
           'autor': filo.autor,
           'año_publicacion': filo.año_publicacion,
           'descripcion': filo.descripcion,
       }
       formulario = FormularioFilosofiaYReligionE(initial=inicial)
   return render(
       request=request,
       template_name='categorias_libros/ingreso_libro_filo.html',
       context={'formulario': formulario},
   )

@login_required
def editar_bios(request, id):
   bios = Biografia.objects.get(id=id)
   if request.method == "POST":
       formulario = FormularioBiografiaE(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           bios.nombre = data['nombre']
           bios.autor = data['autor']
           bios.año_publicacion = data['año_publicacion']
           bios.sinopsis = data['sinopsis']
           bios.save()
           url_exitosa = reverse('biografias')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': bios.nombre,
           'autor': bios.autor,
           'año_publicacion': bios.año_publicacion,
           'sinopsis': bios.sinopsis,
       }
       formulario = FormularioBiografiaE(initial=inicial)
   return render(
       request=request,
       template_name='categorias_libros/ingreso_libro_bios.html',
       context={'formulario': formulario},
   )
class BiografiaDetailView(DetailView):
    model = Biografia
    success_url = reverse_lazy('biografias')

class FiccionDetailView(DetailView):
    model = Ficcion
    success_url = reverse_lazy('ficcion')

class InfantilYJuvenilDetailView(DetailView):
    model = InfantilYJuvenil
    success_url = reverse_lazy('infantil-y-juvenil')

class PoesiaDetailView(DetailView):
    model = Poesia
    success_url = reverse_lazy('poesia')

class FilosofiaYReligionDetailView(DetailView):
    model = FilosofiaYReligion
    success_url = reverse_lazy('filosofia-y-religion')