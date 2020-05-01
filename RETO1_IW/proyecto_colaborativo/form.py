from django import forms
from django.forms import ModelForm

from .models import ticket, Equipo, Empleado


class EquipoForm(ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'


class TicketForm(ModelForm):
    class Meta:
        model = ticket
        fields = '__all__'


class EmpleadoForm(forms.ModelForm):  # En este caso hemos querido utilizar ambas manera
    class Meta:
        model = Empleado
        fields = '__all__'
