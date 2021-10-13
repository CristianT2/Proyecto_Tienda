from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Localidad, Persona, Empleado, Cargo, Cliente, Movimiento, Articulo, Item
from .forms import LocalidadForm, PersonaForm, CargoForm, EmpleadoForm, ClienteForm, MovimientoForm, ArticuloForm, ItemForm

# Create your views here.
def mostrar_home(request, template_name= 'tienda/index.html'):
    return render(request,template_name)

def localidad_listar(request, template_name= 'tienda/lista_localidad.html'):
    localidades = Localidad.objects.all()
    dato_localidad = {"localidades" : localidades}
    return render(request, template_name, dato_localidad)

def persona_listar(request, template_name= 'tienda/lista_personas.html'):
    personas = Persona.objects.all()
    dato_persona = {"personas" : personas }
    return render(request, template_name, dato_persona)

def empleado_listar(request, template_name= 'tienda/lista_empleado.html'):
    empleados = Empleado.objects.all()
    dato_empleado = {"empleados" : empleados}
    return render(request, template_name, dato_empleado)

def cargo_listar(request, template_name= 'tienda/lista_cargo.html'):
    cargos = Cargo.objects.all()
    dato_cargo = {"cargos" : cargos}
    return render(request, template_name, dato_cargo)

def cliente_listar(request, template_name= 'tienda/lista_cliente.html'):
    clientes = Cliente.objects.all()
    dato_cliente = {"clientes" : clientes}
    return render(request, template_name, dato_cliente)

def movimiento_listar(request, template_name= 'tienda/lista_movimiento.html'):
    movimientos = Movimiento.objects.all()
    dato_movimiento = {"movimientos" : movimientos}
    return render(request, template_name, dato_movimiento)

def articulo_listar(request, template_name= 'tienda/lista_articulo.html'):
    articulos = Articulo.objects.all()
    dato_articulo = {"articulos" : articulos}
    return render(request, template_name, dato_articulo)

def item_listar(request, template_name= 'tienda/lista_item.html'):
    items = Item.objects.all()
    dato_item = {"items" : items}
    return render(request, template_name, dato_item)

def nueva_localidad(request, template_name= 'tienda/localidad_form.html'):
    if request.method == 'POST':
        form = LocalidadForm(request.POST)
        if form.is_valid():
            form.save(commit= True)
            messages.success(request, "guardado")
            return redirect('nueva_localidad')
        else:
            print(form.errors)    
    else:
        form = LocalidadForm()
    dato = {"form": form}
    return render(request, template_name, dato)   

def nueva_persona(request, template_name= 'tienda/persona_form.html'):

    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save(commit= True)
            messages.success(request, "Guardado")
            return redirect('nueva_persona')
        else:
            print(form.errors)    
    else:
        form = PersonaForm()

    dato = {"form": form}
    return render(request, template_name,dato)    

def nuevo_cargo(request, template_name='tienda/cargo_form.html'):

    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save(commit= True)
            messages.success(request, "Guardado")
            return redirect('nuevo_cargo')
        else:
            print(form.errors)    
    else:
        form = CargoForm()

    dato = {"form": form}

    return render(request, template_name, dato)

def nuevo_empleado(request, template_name= 'tienda/empleado_form.html'):

    if request.method == 'POST' : 
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save(commit= True)
            messages.success(request, "Guardado")
            return redirect('nuevo_empleado')
        else:
            print(form.errors)    
    else:
        form = EmpleadoForm()

    dato = {"form": form}
    return render(request, template_name, dato)

def nuevo_cliente(request, template_name= 'tienda/cliente_form.html'):

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save(commit= True)
            messages.success(request, "Guardado")
            return redirect('nuevo_cliente')
        else:
            print(form.errors)   
    else:
        form = ClienteForm()

    dato = {"form": form}
    return render(request, template_name, dato)

def nuevo_movimiento(request, template_name= 'tienda/movimiento_form.html'):

    if request.method == 'POST':
        form = MovimientoForm(request.POST)
        if form.is_valid():
            form.save(commit= True)
            messages.success(request, "Guardado")
            return redirect('nuevo_movimiento')
        else:
            print(form.errors)  
    else:
        form = MovimientoForm()

    dato = {"form": form}
    return render(request, template_name, dato)

def nuevo_articulo(request, template_name= 'tienda/articulo_form.html'):

    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit= True)
            messages.success(request, "Guardado")
            return redirect('nuevo_articulo')
        else:
            print(form.errors)    
    else:
        form = ArticuloForm()

    dato = {"form": form}
    return render(request, template_name, dato)

def nuevo_item(request, template_name= 'tienda/item_form.html'):

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save(commit= True)
            messages.success(request, "Guardado")
            return redirect('nuevo_item')
        else:
            print(form.errors)    
    else:
        form = ItemForm()

    dato = {"form": form}
    return render(request, template_name, dato)                


def modificar_localidad(request, pk, template_name= 'tienda/localidad_form.html'):
    localidad = Localidad.objects.get(pk= pk)
    form = LocalidadForm(request.POST or None, instance= localidad)
    if form.is_valid():
        form.save(commit= True)
        return redirect('localidad_listar')
    else:
        print(form.errors)

    datos = {"form" : form}
    return render(request, template_name, datos)  


def modificar_persona(request, pk, template_name= 'tienda/persona_form.html'):
    persona = Persona.objects.get(num_doc = pk)
    form = PersonaForm(request.POST or None, instance= persona)
    if form.is_valid():
        form.save(commit= True)
        return redirect('nueva_persona')
    else:
        print(form.errors)

    datos = {"form" : form}
    return render(request, template_name, datos)


def modificar_cargo(request, pk, template_name= 'tienda/cargo_form.html'):
    cargo = Cargo.objects.get(pk = pk)
    form = CargoForm(request.POST or None, instance= cargo)
    if form.is_valid():
        form.save(commit= True)
        return redirect('nuevo_cargo')
    else:
        print(form.errors)

    datos = {"form" : form}
    return render(request, template_name, datos)


def modificar_empleado(request, pk, template_name= 'tienda/empleado_form.html'):
    empleado = Empleado.objects.get(legajo= pk)
    form = EmpleadoForm(request.POST or None, instance= empleado)
    if form.is_valid():
        form.save(commit= True)
        return redirect('nuevo_empleado')
    else:
        print(form.errors)

    datos = {"form": form}
    return render(request, template_name, datos)


def modificar_cliente(request, pk, template_name= 'tienda/cliente_form.html'):
    cliente = Cliente.objects.get(pk = pk)
    form = ClienteForm(request.POST or None, instance= cliente)

    if form.is_valid():
        form.save(commit= True)
        return redirect('nuevo_cliente')
    else:
        print(form.errors)

    datos = {"form" : form}
    return render(request, template_name, datos)


def modificar_movimiento(request, pk, template_name= 'tienda/movimiento_form.html'):
    movimiento = Movimiento.objects.get(pk = pk)
    form = MovimientoForm(request.POST or None, instance= movimiento)

    if form.is_valid():
        form.save(commit= True)
        return redirect('nuevo_movimiento')
    else:
        print(form.errors)

    datos = {"form" : form}
    return render(request, template_name, datos)        


def modificar_articulo(request, pk, template_name= 'tienda/articulo_form.html'):
    articulo = Articulo.objects.get(pk = pk)
    form = ArticuloForm(request.POST or None, instance= articulo)

    if form.is_valid():
        form.save(commit= True)
        return redirect('nuevo_articulo')
    else:
        print(form.errors)

    datos = {"form" : form}
    return render(request, template_name, datos)


def modificar_item(request, pk, template_name= 'tienda/item_form.html'):
    item = Item.objects.get(pk = pk)
    form = ItemForm(request.POST or None, instance= item)

    if form.is_valid():
        form.save(commit= True)
        return redirect('nuevo_item')
    else:
        print(form.errors)

    datos = {"form" : form}
    return render(request, template_name, datos)


def eliminar_localidad(request, pk, template_name= 'tienda/alert_elim_localidad.html'):
    localidad = Localidad.objects.get(pk = pk)
    if request.method == 'POST':
        localidad.delete()
        return redirect('localidad_listar')
    else:
        dato = {"form": localidad}
        return render(request, template_name, dato)
        

def eliminar_persona(request, pk, template_name= 'tienda/alert_elim_persona.html'):
    persona = Persona.objects.get(num_doc = pk)
    if request.method == 'POST':
        persona.delete()
        return redirect('persona_listar')
    else:
        dato = {"form": persona}
        return render(request, template_name, dato) 


def eliminar_empleado(request, pk, template_name= 'tienda/alert_elim_empleado.html'):
    empleado = Empleado.objects.get(legajo = pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('empleado_listar')
    else:
        dato = {"form": empleado}
        return render(request, template_name, dato) 



def eliminar_cargo(request, pk, template_name= 'tienda/alert_elim_cargo.html'):
    cargo = Cargo.objects.get(pk = pk)
    if request.method == 'POST':
        cargo.delete()
        return redirect('cargo_listar')
    else:
        dato = {"form": cargo}
        return render(request, template_name, dato) 


def eliminar_cliente(request, pk, template_name= 'tienda/alert_elim_cliente.html'):
    cliente = Cliente.objects.get(pk = pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_listar')
    else:
        dato = {"form": cliente}
        return render(request, template_name, dato)         


def eliminar_movimiento(request, pk, template_name= 'tienda/alert_elim_movimiento.html'):
    movimiento = Movimiento.objects.get(pk = pk)
    if request.method == 'POST':
        movimiento.delete()
        return redirect('movimiento_listar')
    else:
        dato = {"form": movimiento}
        return render(request, template_name, dato) 


def eliminar_articulo(request, pk, template_name= 'tienda/alert_elim_articulo.html'):
    articulo = Articulo.objects.get(pk = pk)
    if request.method == 'POST':
        articulo.delete()
        return redirect('articulo_listar')
    else:
        dato = {"form": articulo}
        return render(request, template_name, dato) 


def eliminar_item(request, pk, template_name= 'tienda/alert_elim_item.html'):
    item = Item.objects.get(pk = pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_listar')
    else:
        dato = {"form": item}
        return render(request, template_name, dato) 
    





