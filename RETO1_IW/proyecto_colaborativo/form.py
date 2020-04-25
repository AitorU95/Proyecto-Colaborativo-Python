from django import forms
from .models import ticket


class EquipoForm(forms.Form):
    modelo = forms.CharField(label="modelo", max_length=100)
    numeroserie = forms.CharField(label="numeroserie", max_length=100)
    marca = forms.CharField(label="marca", max_length=100)
    tipo = forms.CharField(label="tipo", max_length=100)
    fecha_adquisicion = forms.DateField(label="fecha adquisicion", required=False)
    fecha_puesta_marcha = forms.DateField(label="fecha puesta marcha", required=False)
    proveedor = forms.CharField(label="proveedor", max_length=100)
    planta = forms.CharField(label="planta", max_length=100)


class EmpleadoForm(forms.Form):
    nombre = forms.CharField(label="nombre", max_length=100)
    apellido = forms.CharField(label="apellido", max_length=100)
    dni = forms.CharField(label="Dni", max_length=100)
    telefono = forms.CharField(label="telefono", max_length=100)
    email = forms.CharField(label="email", max_length=100)


class ticketForm(forms.Form):
    numeroref = forms.CharField(label="numeroref", max_length=100)
    titulo = forms.CharField(label="titulo", max_length=100)
    descripcion = forms.CharField(label="descripcion", max_length=100)
    fecha_apertura = forms.DateField(label="fecha apertura", required=False)
    fecha_resolucion = forms.DateField(label="fecha resolucion", required=False)
    urgencia = forms.CharField(label="urgencia", max_length=100)
    tipo = forms.CharField(label="tipo", max_length=100)
    estado = forms.CharField(label="estado", max_length=100)
    empleado = forms.CharField(label="empleado", max_length=100)
    comentarios = forms.CharField(label="comentarios", max_length=100)


class Equipo2Form(forms.ModelForm):#metodos opcionales de usar, de momento no los usamos
    class Meta:
        fields = '__all__'


class Empleado2Form(forms.ModelForm):#metodos opcionales de usar, de momento no los usamos
    class Meta:
        fields = '__all__'


class ticket2Form(forms.ModelForm):
    class Meta:
        model=ticket
        exclude= ['empleado']
