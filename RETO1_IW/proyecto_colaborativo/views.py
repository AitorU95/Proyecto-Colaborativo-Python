from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.http import HttpResponse
from .models import Equipo, Empleado, ticket
from .form import EquipoForm


def index(request):

    context = {'titulo_pagina': 'Inicio'}
    return render(request, 'Inicio.html', context)  # request, nombre de la template, contenido que se le pasa

def equipos(request):
    equipos = Equipo.objects.order_by("marca")  # metodo que ordena por marca
    context = {'titulo_pagina': 'Gestión de equipos',
               'lista_equipos': equipos}        # pasamos lista_equipos a la template como dato

    return render(request, 'equipos.html', context)


class TicketListView(ListView): #clase para sacar los tickets como listado ordenados por numero de referencia
    model = ticket
    template_name = 'listado_tickets.html'
    queryset = ticket.objects.order_by('numeroref')

    def get_context_data(self, **kwargs):
        context = super(TicketListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de tickets'
        return context

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'listado_empleados.html'
    queryset = Empleado.objects.order_by('nombre')

    def get_context_data(self, **kwargs):
        context = super(EmpleadoListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de empleados'
        return context

def detail(request, equipo_id):  # nos busca por id
    equipos = Equipo.objects.get(pk=equipo_id)
    return HttpResponse(equipos)


'''
def empleado(request, empleado_id):
    empleados = Empleado.objects.get(pk=empleado_id)
    # output = ",".join([empleados.nombre,empleados.dni]) #cargar directamente ne http respons sin plantilla
    context={'titulo_pagina':'listado de empleados','empleados':empleados}
    return render(request,'empleado.html',context)'''

class TicketDetaiView(DetailView):
    model = ticket
    template_name = 'ticket.html'

    def get_context_data(self, **kwargs):
        context = super(TicketDetaiView,self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del ticket'
        return context


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

def show_form(request):
    return render(request, 'registro.html')


def post_form(request):
    modelo = request.POST["modelo"]
    numeroserie = request.POST["numeroserie"]
    marca = request.POST["marca"]
    tipo = request.POST["tipo"]
    fecha_adquisicion = request.POST["fecha_adquisicion"]
    fecha_puesta_marcha = request.POST["fecha_puesta_marcha"]
    proveedor = request.POST["proveedor"]
    return HttpResponse(
        F"el model: {modelo} ,Nserie:{numeroserie},marca:{marca},tipo:{tipo},fecha_adquisicion:{fecha_adquisicion},fechapm={fecha_puesta_marcha},proveedor:{proveedor}")


def show_equipo_form(request):
    form = EquipoForm()
    context={'form':form}
    return render(request, 'empleado.form.html', context)


def post_equipo_form(request):
    form = EquipoForm(request.POST)
    if form.is_valid():
        equipo=Equipo()
        equipo.modelo = form.cleaned_data['modelo'],
        equipo.numeroserie = form.cleaned_data['numeroserie']
        equipo.marca = form.cleaned_data['marca']
        equipo.tipo =form.cleaned_data['tipo']
        equipo.fecha_adquisicion =form.cleaned_data['fecha_adquisicion']
        equipo.fecha_puesta_marcha=form.cleaned_data['fecha_puesta_marcha']
        equipo.planta=form.cleaned_data['planta']
        equipo.save()


    return HttpResponse(F"EL equipo  MODELO ES:{equipo.modelo}, el numero de serie es:{equipo.numeroserie}")

