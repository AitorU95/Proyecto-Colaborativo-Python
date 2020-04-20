from django.shortcuts import render
from .models import Departamento

# Create your views here.
from django.http import HttpResponse

#Devuelve el listado de empresas
def index (request):
    departamentos = Departamento.objects.order_by('nombre')
    output = ', '.join([d.nombre for d in departamentos])
    return HttpResponse(output)

#Dvuelve los datos de un departamento por ID
def detail(request, departamento_id):
    departamento = Departamento.objects.get(pk=departamento_id)
    return HttpResponse(departamento)
