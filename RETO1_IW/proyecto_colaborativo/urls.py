from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('equipos/<equipo_id>', views.detail, name='equipos'),  # pones id y te muestra equipo
    path('empleados/<int:pk>', views.EmpleadoDetailView.as_view(), name='empleado'),
    path('registro/', views.show_form, name='registro'),
    path('mostrardatos/', views.post_form, name='mostrardatos'),
    path('equipo/', views.show_equipo_form, name='equipo.form'),  # insertar equipos
    path('ticket/', views.show_ticket_form, name="ticket.form"),#inserta tickets,excepto empleado que es foreign key
    path('empleado/',views.show_empleado_form,name="empleado.form"),#inserta empleados
    path('equipoalmacenados/', views.equipos, name='equipoalmacenados'),  # lista de equipos
    #path('equipoalmacenados2/<ekipo_id>', views.borradoPrueba, name='equipoalmacenado2'),
    path('comprobacion/', views.post_equipo_form, name='comprobacion'),  # compreba si has metido correctamente
    path('tickets/', views.TicketListView.as_view(), name='tickets'),
    path('ticket/<int:pk>', views.TicketDetaiView.as_view(), name='ticket'),
    path('listaempleados/', views.EmpleadoListView.as_view(), name='listaempleados'),
    path('proveedores/', views.proveedor, name='proveedores'),  # lista de los proveedores
    path('añadirequipos/',views.Equipos_add, name ='añadirequipo'),
    path('editarequipo/<int:equipo_id>', views.Equipos_edit, name='editarequipo'),
    path('equipodelete/<int:equipo_id>', views.Equipos_delete, name='equipodelete'),
    path('ticketedit/<int:ticket_id>', views.ticket_edit, name ='ticketedit')
]
