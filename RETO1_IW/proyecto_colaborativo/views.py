from django.shortcuts import render
from django.views.generic import DetailView
from django.http import HttpResponse
from .models import Equipo, Empleado, ticket


def index(request):

    context = {'titulo_pagina': 'Inicio'}
    return render(request, 'Inicio.html', context)  # request, nombre de la template, contenido que se le pasa

def equipos(request):
    equipos = Equipo.objects.order_by("marca")  # metodo que ordena por marca
    context = {'titulo_pagina': 'Gestión de equipos',
               'lista_equipos': equipos}        # pasamos lista_equipos a la template como dato

    return render(request, 'equipos.html', context)

def detail(request, equipo_id):  # nos busca por id
    equipos = Equipo.objects.get(pk=equipo_id)
    return HttpResponse(equipos)


'''
def empleado(request, empleado_id):
    empleados = Empleado.objects.get(pk=empleado_id)
    # output = ",".join([empleados.nombre,empleados.dni]) #cargar directamente ne http respons sin plantilla
    context={'titulo_pagina':'listado de empleados','empleados':empleados}
    return render(request,'empleado.html',context)'''


class EmpleadoDetailView(DetailView): #clase predefinida de django para ids
    model = Empleado
    template_name = 'empleado.html'
    context_object_name = 'empleados'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'detalles del empleado'

        return context

class EquiposDetailView(DetailView):
    model = Equipo
    template_name = 'equipos.html'
    context_object_name = 'equipos'

    def get_context_data(self, **kwargs):
        context = super(EquiposDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'detalles de los equipos'
        return context
