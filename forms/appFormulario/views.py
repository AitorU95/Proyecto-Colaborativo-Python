from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def show_form(request):
    return render(request, 'registro.html')


def post_form(request):
    modelo = request.POST["modelo"]
    ticket = request.POST["ticket"]
    Nserie = request.POST["Nserie"]
    marca=request.POST["marca"]
    tipo=request.POST["tipo"]
    fechaa=request.POST["fechaa"]
    fechapm=request.POST["fechapm"]
    proveedor=request.POST["planta"]
    return HttpResponse(F"el model:{modelo} Y EL email: {ticket},Nserie:{Nserie},marca:{marca},tipo:{tipo},fechaa:{fechaa},fechapm={fechapm},proveedor:{proveedor}")
