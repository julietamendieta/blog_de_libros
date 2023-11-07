from django import forms

class FormularioFiccion(forms.Form):
    genero = forms.CharField(required=True, max_length=256)
    nombre = forms.CharField(required=True, max_length=256)
    autor = forms.CharField(required=True, max_length=256)
    año_publicacion = forms.IntegerField(required=True, max_value=3000)
    sinopsis = forms.CharField(required=True, max_length=400)
    reseña = forms.CharField(required=True, max_length=400)

class FormularioPoesia(forms.Form):
    nombre = forms.CharField(required=True, max_length=256)
    autor = forms.CharField(required=True, max_length=256)
    año_publicacion = forms.IntegerField(required=True, max_value=3000)
    sinopsis = forms.CharField(required=True, max_length=400)
    reseña = forms.CharField(required=True, max_length=400)

class FormularioInfantilYJuvenil(forms.Form):
    genero = forms.CharField(required=True, max_length=256)
    nombre = forms.CharField(required=True, max_length=256)
    autor = forms.CharField(required=True, max_length=256)
    año_publicacion = forms.IntegerField(required=True, max_value=3000)
    sinopsis = forms.CharField(required=True, max_length=400)
    reseña = forms.CharField(required=True, max_length=400)

class FormularioBiografia(forms.Form):
    nombre = forms.CharField(required=True, max_length=256)
    autor = forms.CharField(required=True, max_length=256)
    año_publicacion = forms.IntegerField(required=True, max_value=3000)
    sinopsis = forms.CharField(required=True, max_length=400)
    reseña = forms.CharField(required=True, max_length=400)

class FormularioFilosofiaYReligion(forms.Form):
    nombre = forms.CharField(required=True, max_length=256)
    autor = forms.CharField(required=True, max_length=256)
    año_publicacion = forms.IntegerField(required=True, max_value=3000)
    descripcion = forms.CharField(required=True, max_length=400)
    reseña = forms.CharField(required=True, max_length=400)