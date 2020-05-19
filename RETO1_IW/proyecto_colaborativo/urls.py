from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('equipos/<equipo_id>', views.detail, name='equipos'),  # pones id y te muestra equipo
    path('empleados/<int:pk>', views.EmpleadoDetailView.as_view(), name='empleado'),#muestra los detalles de cada empleado
    path('registro/', views.show_form, name='registro'),
    path('mostrardatos/', views.post_form, name='mostrardatos'),
    path('equipo/', views.show_equipo_form, name='equipo.form'),  # insertar equipos
    path('ticket/', views.show_ticket_form, name='ticket.form'),#inserta tickets,excepto empleado que es foreign key
    path('empleado/',views.Empleado_add,name="empleadoadd"),#inserta empleados
    path('empleado/',views.post_empleado_form,name="empleadoadd"),#inserta empleados
    path('equipoalmacenados/', views.equipos, name='equipoalmacenados'),  # lista de equipos
    path('tickets/', views.TicketListView.as_view(), name='tickets'),#muestra la lista de tickets
    path('ticket/<int:pk>', views.TicketDetaiView.as_view(), name='ticket'),#muestra los detalles del ticket
    path('ticketdelete/<int:ticket_id>',views.ticket_delete,name='ticketdelete'),#borrado de tickets
    path('listaempleados/', views.ListaEmpleados, name='listaempleados'),#ordena los empreados
    path('proveedores/', views.proveedor, name='proveedores'),  # lista de los proveedores
    path('añadirequipos/',views.Equipos_add, name ='añadirequipo'),# llama a la funcion para insertar tickets
    path('editarequipo/<int:equipo_id>', views.Equipos_edit, name='editarequipo'),#llama a la funcion insertar equipos
    path('equipodelete/<int:equipo_id>', views.Equipos_delete, name='equipodelete'),# llama  la funcion para el borrado de equipos
    path('empleadodelete/<int:empleado_id>', views.Empleados_delete, name='empleadodelete'),#llama a la funcion para para el borrado de empleados
    path('ticketedit/<int:ticket_id>', views.ticket_edit, name ='ticketedit'),# llama  la funcion para editar tickets
    path('empleadoedit/<int:empleado_id>',views.Empleado_edit,name='empleadoedit'),# llama a la funcion para editar empleados
    path('ticketadd/',views.Ticket_add,name='ticketadd'),# llama a la funcion para insertar tickets
    path('urgencias',views.filtrado,name='urgencias')#llama a la funcion que muestra los tickets urgentes
]
