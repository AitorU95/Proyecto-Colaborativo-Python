from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('equipos/<equipo_id>', views.detail, name='detail'),
    path('empleados/<int:pk>', views.EmpleadoDetailView.as_view(), name='empleado')
]
