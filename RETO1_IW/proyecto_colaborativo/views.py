from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView
from django.http import HttpResponse, JsonResponse
from .models import Equipo, Empleado, ticket, Descripcion
from .form import EquipoForm, EmpleadoForm, TicketForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


def filtrado(request):  # metodo para el fintrado de las urgencias, asi el usuario sabe que urgencias gestionar primero
    filtrado = ticket.objects.filter(urgencia='urgente')

    context = {'titulo_pagina': 'tickets con urgencia',
               'tickets': filtrado}
    return render(request, 'urgencias.html', context)


def index(request):
    context = {'titulo_pagina': 'Introduce tus credenciales para acceder a la aplicación:'}
    return render(request, 'login.html', context)  # request, nombre de la template, contenido que se le pasa


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


def VerInicio(request):
    context = {'titulo_pagina': 'Inicio'}
    return render(request, 'Inicio.html', context)


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


# funciones json :
@method_decorator(csrf_exempt, name='dispatch')
class DescripcionListView_Json(View):
    def get(self, request):
        descripcionListado = Descripcion.objects.all()
        return JsonResponse(list(descripcionListado.values()), safe=False)

    def post(self, request):
        tarea = Descripcion()
        tarea.texto = request.POST.get('texto')
        tarea.save()
        return JsonResponse(model_to_dict(tarea))


@method_decorator(csrf_exempt, name='dispatch')
class EmpleadoListView_Json(View):
    def get(self, request):
        EmpleadosList = Empleado.objects.all()
        return JsonResponse(list(EmpleadosList.values()), safe=False)

    def post(self, request):
        empleado = Empleado()
        empleado.nombre = request.POST['nombre']
        empleado.apellido = request.POST['apellido']
        empleado.dni = request.POST['dni']
        empleado.telefono = request.POST['telefono']
        empleado.email = request.POST['email']
        empleado.save()
        return JsonResponse(model_to_dict(empleado))


class EmpleadoDetaiView_Json(View):
    def get(self, request, pk):
        empleado = Empleado.objects.get(pk=pk)
        return JsonResponse(model_to_dict(empleado))


class EquipoListView_Json(View):
    def get(self, request):
        EquipoList = Equipo.objects.all()
        return JsonResponse(list(EquipoList.values()), safe=False)

    def post(self, request):
        equipo = Equipo()
        equipo.modelo = request.POST['modelo']
        equipo.numeroserie = request.POST['numeroserie']
        equipo.marca = request.POST['marca']
        equipo.tipo = request.POST['tipo']
        equipo.fecha_adquisicion = request.POST['fecha_adquisicion']
        equipo.fecha_puesta_marcha = request.POST['fecha_puesta_marcha']
        equipo.proveedor = request.POST['proveedor']
        equipo.save()
        return JsonResponse(model_to_dict(equipo))


class EquipoDetalView_Json(View):
    def get(self, request, pk):
        equipo = Equipo.objects.get(pk=pk)
        return JsonResponse(model_to_dict(equipo))


class TicketListView_Json(View):
    def get(self, request):
        TicketList = ticket.objects.all()
        return JsonResponse(list(TicketList.values()), safe=False)

    def post(self, request):
        Ticket = ticket()
        ticket.numeroref = request.POST['numeroref']
        ticket.titulo = request.POST['titulo']
        ticket.descripcion = request.POST['descripcion']
        ticket.fecha_apertura = request.POST['fecha_apertura']
        ticket.fecha_resolucion = request.POST['fecha_resolucion']
        ticket.urgencia = request.POST['urgencia']
        ticket.tipo = request.POST['tipo']
        ticket.estado = request.POST['estado']
        ticket.empleado = request.POST['empleado']
        ticket.comentarios = request.POST['comentarios']
        ticket.save()
        return JsonResponse(model_to_dict(ticket))


class TicketDetalView_Json(View):
    def get(self, request, pk):
        Ticket = ticket.objects.get(pk=pk)
        return JsonResponse(model_to_dict(Ticket))


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
            return redirect('equipoalmacenados')
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
            return redirect('equipoalmacenados')
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
            return redirect('tickets')
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
            return redirect('tickets')
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


def post_empleado_form(request):  # metodo para insertar equipos
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
            return redirect('listaempleados')
    # Si llegamos al final renderizamos el formulario
    return render(request, 'add.html', {'form': form})


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
    form = EmpleadoForm(instance=instancia)
    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = EmpleadoForm(request.POST, instance=instancia)
        # Si el formulario es valido
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo, asi conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
            return redirect('http://127.0.0.1:8000/proyecto_colaborativo/listaempleados')
            return redirect('listaempleados')
    # Si llegamos al final renderizamos el formulario
    return render(request, "editar.html", {'form': form})
