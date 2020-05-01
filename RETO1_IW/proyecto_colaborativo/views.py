from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, View
from django.http import HttpResponse
from .models import Equipo, Empleado, ticket
from .form import EquipoForm, EmpleadoForm, Empleado2Form, TicketForm


def index(request):
    context = {'titulo_pagina': 'Inicio'}
    return render(request, 'Inicio.html', context)  # request, nombre de la template, contenido que se le pasa


def equipos(request):
    equipos = Equipo.objects.order_by("marca")  # metodo que ordena por marca
    context = {'titulo_pagina': 'Gestión de equipos',
               'lista_equipos': equipos}  # pasamos lista_equipos a la template como dato

    return render(request, 'equipos.html', context)


def proveedor(request):  # muestra los proveedores
    proveedores = Equipo.objects.order_by("proveedor")
    context = {'titulo_pagina': 'lista de proveedores',
               'lista_proveedores': proveedores}
    return render(request, 'proveedores.html', context)


def borradoPrueba(request, ekipo_id):  # esta de prueba
    objeto = Equipo.objects.get(pk=ekipo_id)
    objeto.delete()
    context = {'titulo_pagina': 'Detalles de equipos',
               'equipos': objeto}
    return render(request, 'equipoid.html', context)


class TicketListView(ListView):  # clase para sacar los tickets como listado ordenados por numero de referencia
    model = ticket
    template_name = 'listado_tickets.html'
    queryset = ticket.objects.order_by('numeroref')

    def get_context_data(self, **kwargs):
        context = super(TicketListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de tickets'
        return context


def ListaEmpleados(request):
    empleados = Empleado.objects.order_by("nombre")  # metodo que ordena por marca
    context = {'titulo_pagina': 'Gestión de empleados',
               'Empleados_list': empleados}  # pasamos lista_equipos a la template como dato

    return render(request, 'listado_empleados.html', context)


def detail(request, equipo_id):  # nos saca los atributos de los equipos
    equipos = Equipo.objects.get(pk=equipo_id)
    context = {'titulo_pagina': 'Detalles de equipos',
               'equipos': equipos}  # pasamos lista_equipos a la template como dato

    return render(request, 'equipoid.html', context)


class TicketDetaiView(DetailView):
    model = ticket
    template_name = 'ticket.html'

    def get_context_data(self, **kwargs):
        context = super(TicketDetaiView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del ticket'
        return context


class EmpleadoDetailView(DetailView):  # clase predefinida de django para ids
    model = Empleado
    template_name = 'empleado.html'
    context_object_name = 'empleados'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'detalles del empleado'

        return context


class EquiposDetailView(DetailView):  # detalles de los equipos
    model = Equipo
    template_name = 'equipos.html'
    context_object_name = 'equipos'

    def get_context_data(self, **kwargs):
        context = super(EquiposDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'detalles de los equipos'
        return context


def show_form(request):
    return render(request, 'registro.html')


def atras(request):
    return redirect('http://127.0.0.1:8000/proyecto_colaborativo/')


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


def Equipos_add(request):  # metodo para insertar equipos
    # Creamos un formulario vacío
    form = EquipoForm
    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # añadimos los datos del formulario
        form = EquipoForm(request.POST)
        # Si el formulario es valido
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo, asi conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            instancia.save()
            # Despues de guardar redireccionamos la lista
            return redirect('http://127.0.0.1:8000/proyecto_colaborativo/equipoalmacenados/')
    # Si llegamos al final renderizamos el formulario
    return render(request, 'add.html', {'form': form})


def Equipos_edit(request, equipo_id):
    # Recuperamos la instancia del equipo
    instancia = Equipo.objects.get(id=equipo_id)
    # Creamos el formulario con los datos de la instacia
    form = EquipoForm(instance=instancia)
    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = EquipoForm(request.POST, instance=instancia)
        # Si el formulario es valido
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo, asi conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
            return redirect('http://127.0.0.1:8000/proyecto_colaborativo/equipoalmacenados/')
    # Si llegamos al final renderizamos el formulario
    return render(request, "editar.html", {'form': form})


def Equipos_delete(request, equipo_id):
    # Recuperamos la instacia del equipo y la borramos
    instancia = Equipo.objects.get(id=equipo_id)
    instancia.delete()
    # Despues redireccionamos a la lista
    return redirect('http://127.0.0.1:8000/proyecto_colaborativo/equipoalmacenados/')

def Ticket_add(request):  # metodo para insertar equipos
    # Creamos un formulario vacío
    form = TicketForm
    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # añadimos los datos del formulario
        form = TicketForm(request.POST)
        # Si el formulario es valido
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo, asi conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            instancia.save()
            # Despues de guardar redireccionamos la lista
            return redirect('http://127.0.0.1:8000/proyecto_colaborativo/tickets/')
    # Si llegamos al final renderizamos el formulario
    return render(request, 'add.html', {'form': form})

def ticket_edit(request, ticket_id):
    # Recuperamos la instancia del equipo
    instancia = ticket.objects.get(id=ticket_id)
    # Creamos el formulario con los datos de la instacia
    form = TicketForm(instance=instancia)
    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = TicketForm(request.POST, instance=instancia)
        # Si el formulario es valido
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo, asi conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
            return redirect('http://127.0.0.1:8000/proyecto_colaborativo/tickets/')
    # Si llegamos al final renderizamos el formulario
    return render(request, "editar.html", {'form': form})


def ticket_delete(request, ticket_id):  # metodo que borra tickets
    # Recuperamos la instacia del equipo y la borramos
    instancia = ticket.objects.get(id=ticket_id)
    instancia.delete()
    # Despues redireccionamos a la lista
    return redirect('http://127.0.0.1:8000/proyecto_colaborativo/tickets')


def show_equipo_form(request):
    form = EquipoForm()
    context = {'form': form}
    return render(request, 'empleado.form.html', context)


def show_empleado_form(request):  # pasa los datos a la plantilla con la tabla "empleado"
    form = EmpleadoForm
    context = {'form': form}
    return render(request, 'empleado.form.html', context)


def show_ticket_form(request):
    form = TicketForm
    context = {'form': form}
    return render(request, 'ticket.form.html', context)



def post_empleado_form(request):
    form = EmpleadoForm(request.POST)
    if form.is_valid():
        empleado = Empleado()
        empleado.nombre = form.cleaned_data['nombre'],
        empleado.apellido = form.cleaned_data['apellido']
        empleado.dni = form.cleaned_data['dni']
        empleado.email = form.cleaned_data['email']
        empleado.telefono = form.cleaned_data['telefono']

        empleado.save()

    return redirect('http://127.0.0.1:8000/proyecto_colaborativo/')

def Empleado_add(request):  # metodo para insertar equipos
    # Creamos un formulario vacío
    form = EmpleadoForm
    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # añadimos los datos del formulario
        form = EmpleadoForm(request.POST)
        # Si el formulario es valido
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo, asi conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            instancia.save()
            # Despues de guardar redireccionamos la lista
            return redirect('http://127.0.0.1:8000/proyecto_colaborativo/listaempleados/')
    # Si llegamos al final renderizamos el formulario
    return render(request, 'add.html', {'form': form})

def Empleados_delete(request, empleado_id):
    # Recuperamos la instacia del equipo y la borramos
    instancia = Empleado.objects.get(id=empleado_id)
    instancia.delete()
    # Despues redireccionamos a la lista
    return redirect('http://127.0.0.1:8000/proyecto_colaborativo/listaempleados')


def Empleado_edit(request, empleado_id):
    # Recuperamos la instancia del equipo
    instancia = Empleado.objects.get(id=empleado_id)
    # Creamos el formulario con los datos de la instacia
    form = Empleado2Form(instance=instancia)
    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = Empleado2Form(request.POST, instance=instancia)
        # Si el formulario es valido
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo, asi conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
            return redirect('http://127.0.0.1:8000/proyecto_colaborativo/listaempleados')
    # Si llegamos al final renderizamos el formulario
    return render(request, "editar.html", {'form': form})
# class ticket_view(View): esto esta en su video min 23 clase 02/04
