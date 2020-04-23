from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('equipos/<equipo_id>', views.detail, name='equipos'),#pones id y te muestra equipo
    path('empleados/<int:pk>', views.EmpleadoDetailView.as_view(), name='empleado'),
    path('registro/', views.show_form, name='registro'),
    path('mostrardatos/', views.post_form, name='mostrardatos'),
    path('equipo/', views.show_equipo_form, name='equipo.form'),#insertar equipos
    path('equipoalmacenados/', views.equipos, name='equipoalmacenados'),#lista de equipos
    path('comprobacion/', views.post_equipo_form, name='comprobacion'),#compreba si has metido correctamente
    path('tickets/', views.TicketListView.as_view(), name = 'tickets'),
    path('ticket/<int:pk>', views.TicketDetaiView.as_view(), name = 'ticket'),
    path('listaempleados/',views.EmpleadoListView.as_view(),name='listaempleados')
]
