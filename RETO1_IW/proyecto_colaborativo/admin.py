from django.contrib import admin
from .models import Equipo, ticket, Empleado,Descripcion

# Register your models here.
admin.site.register(Equipo)
admin.site.register(ticket)
admin.site.register(Empleado)
admin.site.register(Descripcion)
