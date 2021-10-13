from django.db import models
from datetime import datetime
from django.db.models.enums import Choices

# Create your models here.
class Localidad (models.Model):
    nombre = models.CharField(max_length=50)
    cp = models.IntegerField(default= 0)

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = 'Localidades'

    def __str__(self):
        return self.nombre


class Persona (models.Model):
    num_doc = models.CharField("N° de Documento",max_length= 9,primary_key=True)
    apellido = models.CharField(max_length=50)
    nombre = models.CharField("Nombre/s", max_length=80)
    fecha_nac = models.DateField("Fecha de Nacimiento", default= datetime.now())
    telefono = models.CharField("N° de Telefono",max_length=15)
    email = models.EmailField()
    direccion = models.CharField(max_length=90)
    localidad = models.ForeignKey(Localidad, null= True, blank= True, default= 'Seleccione una opcion', on_delete= models.PROTECT, related_name= "persona_localidad")

    class Meta :
        ordering = ["apellido", "nombre"]

    def __str__(self):
        return '%s %s - DNI: %s' %(self.apellido, self.nombre, self.num_doc)

cargo_nivel= [
    (1, 'Nivel 1'),
    (2, 'Nivel 2'),
    (3, 'Nivel 3'),
    (4, 'Nivel 4'),
    (5, 'Nivel 5'),
]

class Cargo (models.Model):
    nombre = models.CharField("Nombre del cargo", max_length=60)
    nivel = models.IntegerField(choices= cargo_nivel, default=1)
    descripcion = models.CharField(max_length=120)

    class Meta:
        ordering = ["nombre","descripcion"]

    def __str__(self):
        return self.nombre

class Empleado (models.Model):
    persona = models.ForeignKey(Persona, null= True, blank= True, on_delete= models.PROTECT, related_name= "empleado_persona")
    legajo = models.IntegerField("N° de Legajo", primary_key=True)
    cargo = models.ForeignKey(Cargo, null= True, blank= True, on_delete= models.PROTECT, related_name= "empleado_cargo")

    class Meta :
        ordering = ["legajo"]

    def __str__(self):
        return '%s - %s : %s' %(self.legajo, self.persona, self.cargo)

class Cliente (models.Model):
    persona = models.ForeignKey(Persona, null= True, blank= True, on_delete= models.PROTECT, related_name= "cliente_empleado")
    categoria = models.IntegerField()
    fecha_alta = models.DateField("Fecha de Alta", default= datetime.now())

    class Meta:
        ordering = ["categoria", "persona"]

    def __str__(self):
        return '%s' %(self.persona)

class Movimiento (models.Model):
    tipo = models.CharField("Tipo de Movimiento", max_length= 70)
    cliente = models.ForeignKey(Cliente, null= True, blank= True, on_delete= models.PROTECT, related_name="movimiento_cliente")
    numero = models.CharField(max_length= 100)
    fecha = models.DateField(default= datetime.now())

    class Meta:
        ordering = ["tipo","fecha"]

    def __str__(self):
        return '%s' %(self.tipo)

articulo_estado= [
    (1, 'Disponible'),
    (2, 'No Disponible')
]

class Articulo (models.Model):
    id = models.IntegerField(primary_key= True)
    marca = models.CharField(max_length= 70)
    descripcion = models.CharField(max_length= 100)
    categoria = models.CharField(max_length= 80)
    stock = models.IntegerField()
    precio = models.FloatField()
    disponible = models.IntegerField(null= False, blank= False, choices= articulo_estado, default= 1)
    imagen = models.ImageField(upload_to='artuculos', height_field=None, width_field=None, max_length=None )
    
    class Meta :
        ordering = ["marca","precio"]

    def __str__(self):
        return '%s %s ' %(self.marca, self.descripcion)

class Item (models.Model):
    articulo = models.ForeignKey(Articulo, null= True, blank= True, on_delete= models.PROTECT, related_name= "item_articulo")
    movimiento = models.ForeignKey(Movimiento, null= True, blank= True, on_delete= models.PROTECT, related_name= "item_movimiento")
    cantidad = models.IntegerField()

    class Meta:
        ordering = ["movimiento", "articulo"]

    def __str__(self):
        return '%s - %s' %(self.movimiento, self.articulo)

