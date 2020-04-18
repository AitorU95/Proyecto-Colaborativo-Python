from django.db import models

from django.db import models


class Empleado(models.Model):
    # Campo para la relación one-to-many

    nombre = models.CharField(max_length=40)
    telefono = models.IntegerField(null=True)
    dni = models.CharField(max_length=40, null=True)
    email = models.EmailField(null=True)
    # Es posible indicar un valor por defecto mediante 'default'
    apellido = models.CharField(max_length=50, null=True)

    # Para permitir propiedades con valor null, añadiremos las opciones null=True, blank=True.

    def __str__(self):
        return f"id={self.id},nombre={self.nombre},telefono={self.telefono},dni={self.dni},email={self.email},apellido={self.apellido}"


class ticket(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.

    numeroref = models.CharField(max_length=50, null=True)
    titulo = models.CharField(max_length=50, null=True)
    descripcion = models.CharField(max_length=50, null=True)
    fechaa = models.DateField(null=True)
    fechapm = models.DateField(null=True)
    urgencia = models.CharField(max_length=50, null=True)
    tipo = models.CharField(max_length=50, null=True)
    estado = models.CharField(max_length=50, null=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    comentarios = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"id={self.id},numeroref={self.titulo},titulo={self.titulo},descripcion={self.descripcion},fechaa={self.fechaa},fechapm{self.fechapm}," \
               f"Urgencia={self.urgencia},tipo={self.tipo},estado={self.estado},empleado={self.empleado}comentarios={self.comentarios}"


class Equipo(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.

    modelo = models.CharField(max_length=50)
    ticket=models.ForeignKey(ticket,on_delete=models.CASCADE, null=True)
    numeroserie = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    fechaa = models.DateField()
    fechapm = models.DateField()
    proveedor = models.CharField(max_length=200)
    planta = models.CharField(max_length=200)

    def __str__(self):
        return f"id={self.id},ticket={self.ticket},modelo={self.modelo},marca={self.marca},tipo={self.tipo},fechaa={self.fechaa},fechapm={self.fechapm}," \
               f"proveedor={self.proveedor},planta={self.planta}"
