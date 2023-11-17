from django import forms

class FormularioFiccion(forms.Form):
    genero = forms.CharField(required=True, max_length=256)
    nombre = forms.CharField(required=True, max_length=256)
    autor = forms.CharField(required=True, max_length=256)
    año_publicacion = forms.IntegerField(required=True, max_value=3000)
    sinopsis = forms.CharField(required=True, max_length=3000)

class FormularioPoesia(forms.Form):
    nombre = forms.CharField(required=True, max_length=256)
    autor = forms.CharField(required=True, max_length=256)
    año_publicacion = forms.IntegerField(required=True, max_value=3000)
    sinopsis = forms.CharField(required=True, max_length=3000)

class FormularioInfantilYJuvenil(forms.Form):
    genero = forms.CharField(required=True, max_length=256)
    nombre = forms.CharField(required=True, max_length=256)
    autor = forms.CharField(required=True, max_length=256)
    año_publicacion = forms.IntegerField(required=True, max_value=3000)
    sinopsis = forms.CharField(required=True, max_length=3000)

class FormularioBiografia(forms.Form):
    nombre = forms.CharField(required=True, max_length=256)
    autor = forms.CharField(required=True, max_length=256)
    año_publicacion = forms.IntegerField(required=True, max_value=3000)
    sinopsis = forms.CharField(required=True, max_length=3000)

class FormularioFilosofiaYReligion(forms.Form):
    nombre = forms.CharField(required=True, max_length=256)
    autor = forms.CharField(required=True, max_length=256)
    año_publicacion = forms.IntegerField(required=True, max_value=3000)
    descripcion = forms.CharField(required=True, max_length=3000)

class FormularioFiccionE(forms.Form):
    genero = forms.CharField(required=True, max_length=256)
    nombre = forms.CharField(required=True, max_length=256)
    autor = forms.CharField(required=True, max_length=256)
    año_publicacion = forms.IntegerField(required=True, max_value=3000)
    sinopsis = forms.CharField(required=True, max_length=3000)

class FormularioPoesiaE(forms.Form):
    nombre = forms.CharField(required=True, max_length=256)
    autor = forms.CharField(required=True, max_length=256)
    año_publicacion = forms.IntegerField(required=True, max_value=3000)
    sinopsis = forms.CharField(required=True, max_length=3000)

class FormularioInfantilYJuvenilE(forms.Form):
    genero = forms.CharField(required=True, max_length=256)
    nombre = forms.CharField(required=True, max_length=256)
    autor = forms.CharField(required=True, max_length=256)
    año_publicacion = forms.IntegerField(required=True, max_value=3000)
    sinopsis = forms.CharField(required=True, max_length=3000)

class FormularioBiografiaE(forms.Form):
    nombre = forms.CharField(required=True, max_length=256)
    autor = forms.CharField(required=True, max_length=256)
    año_publicacion = forms.IntegerField(required=True, max_value=3000)
    sinopsis = forms.CharField(required=True, max_length=3000)

class FormularioFilosofiaYReligionE(forms.Form):
    nombre = forms.CharField(required=True, max_length=256)
    autor = forms.CharField(required=True, max_length=256)
    año_publicacion = forms.IntegerField(required=True, max_value=3000)
    descripcion = forms.CharField(required=True, max_length=3000)
