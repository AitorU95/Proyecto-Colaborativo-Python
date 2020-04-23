from django.db import models

from django.db import models


class Empleado(models.Model):
    # Campo para la relación one-to-many

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=50, null=True)
    dni = models.CharField(max_length=40, null=True)
    telefono = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    # Es posible indicar un valor por defecto mediante 'default'


    # Para permitir propiedades con valor null, añadiremos las opciones null=True, blank=True.

    def __str__(self):
        return f"Id={self.id},Nombre={self.nombre},Apellido={self.apellido},DNI={self.dni},Telefono={self.telefono},Email={self.email}"


class ticket(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    numeroref = models.CharField(max_length=50, null=True)
    titulo = models.CharField(max_length=50, null=True)
    descripcion = models.CharField(max_length=50, null=True)
    fecha_apertura = models.DateField(null=True)
    fecha_resolucion = models.DateField(null=True)
    urgencia = models.CharField(max_length=50, null=True)
    tipo = models.CharField(max_length=50, null=True)
    estado = models.CharField(max_length=50, null=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    comentarios = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"id={self.id},numeroref={self.titulo},titulo={self.titulo},descripcion={self.descripcion},fechaaper={self.fecha_apertura},fechares{self.fecha_resolucion}," \
               f"Urgencia={self.urgencia},tipo={self.tipo},estado={self.estado},empleado={self.empleado}comentarios={self.comentarios}"



class Equipo(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.

    modelo = models.CharField(max_length=50)
    numeroserie = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    fecha_adquisicion = models.DateField()
    fecha_puesta_marcha = models.DateField()
    proveedor = models.CharField(max_length=100)
    planta = models.CharField(max_length=200)

    def __str__(self):
        return f"id={self.id},modelo={self.modelo},marca={self.marca},tipo={self.tipo},fecha_adquisicion={self.fecha_adquisicion},fecha_puesta_marcha={self.fecha_puesta_marcha}," \
               f"proveedor={self.proveedor},planta={self.planta}"





