from django import forms
from .models import Equipo


class EquipoForm(forms.Form):
    modelo = forms.CharField(label="modelo", max_length=100)
    numeroserie = forms.CharField(label="numeroserie", max_length=100)
    marca = forms.CharField(label="marca", max_length=100)
    tipo = forms.CharField(label="tipo", max_length=100)
    fecha_adquisicion = forms.DateField(label="fecha adquisicion", required=False)
    fecha_puesta_marcha = forms.DateField(label="fecha puesta marcha", required=False)
    proveedor = forms.CharField(label="proveedor", max_length=100)
    planta = forms.CharField(label="planta", max_length=100)




