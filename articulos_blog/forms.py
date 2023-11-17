from django import forms

class FormularioArticulo(forms.Form):
    titulo = forms.CharField(required=True, max_length=256)
    subtitulo = forms.CharField(required=True, max_length=256)
    cuerpo = forms.CharField(required=True, max_length=10000)
    autor = forms.CharField(required=True, max_length=256)
    fecha = forms.DateField(required=True)
