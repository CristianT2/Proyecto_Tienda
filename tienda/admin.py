from django.contrib import admin
from .models import Localidad, Persona, Cargo, Empleado, Cliente, Movimiento, Articulo, Item

# Register your models here.
my_models= [Localidad, Persona, Empleado, Cargo, Cliente, Movimiento, Articulo, Item]

admin.site.register(my_models)