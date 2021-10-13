from django import forms
from django.forms import ModelForm
from .models import Localidad, Persona, Empleado, Cargo, Cliente, Movimiento, Articulo, Item

class LocalidadForm (ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs= {'type': 'text', 'class': 'form-control rounded-pill', 'placeholder': 'Ingrese Localidad', 'title': 'Ingrese Localidad'}),
            'cp': forms.TextInput(attrs= {'type': 'number', 'class': 'form-control rounded-pill', 'placeholder': 'Ingrese Localidad', 'title': 'Ingrese Localidad'})
        }


class PersonaForm (ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'num_doc': forms.TextInput(attrs= {'type': 'number', 'class': 'form-control rounded-pill', 'placeholder': 'Ingrese N° de Documento','title': 'Ingrese su N° de documento'}),
            'apellido': forms.TextInput(attrs= {'type': 'text', 'class': 'form-control rounded-pill', 'placeholder': 'Ingrese Apellido', 'title': 'Ingrese su apellido'}),
            'nombre': forms.TextInput(attrs= {'type': 'text', 'class': 'form-control rounded-pill', 'placeholder': 'Ingrese Nombre', 'title': 'Ingrese su nombre'}),
            'fecha_nac': forms.DateInput(format= '%Y-%m-%d', attrs= {'type': 'date', 'class': 'form-control rounded-pill'}),
            'telefono': forms.TextInput(attrs= {'type': 'number', 'class': 'form-control rounded-pill', 'placeholder': 'Ingrese Telefono', 'title': 'Ingrese su N° de telefono'}),
            'email': forms.EmailInput(attrs= {'type': 'text', 'class': 'form-control rounded-pill', 'placeholder': 'Ingrese Email', 'title': 'Ingrese su Email'}),
            'direccion': forms.TextInput(attrs= {'type': 'text', 'class': 'form-control rounded-pill', 'placeholder': 'Ingrese Direccion', 'title': 'Ingrese su direccion'}),
            'localidad': forms.Select(attrs= {'class': 'form-select rounded-pill'})
        }

class CargoForm (ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs= {'type': 'text', 'class': 'form-control rounded-pill', 'placeholder': 'Ingrese Cargo', 'title': 'Ingrese un cargo'}),
            'nivel': forms.Select(attrs= {'class': 'form-select rounded-pill'}),
            'descripcion': forms.Textarea(attrs= {'type': 'text', 'class': 'form-control ', 'placeholder': 'Ingrese descripcion del cargo', 'title': 'Ingrese una descripcion del cargo'})
        }

class EmpleadoForm (ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets= {
            'persona': forms.Select(attrs= {'class': 'form-select rounded-pill'}),
            'legajo': forms.TextInput(attrs= {'type': 'number', 'class': 'form-control rounded-pill', 'placeholder': 'Ingrese N° de Legajo', 'title': 'Ingrese su N° de legajo'}),
            'cargo': forms.Select(attrs= {'class': 'form-select rounded-pill'})
        }

class ClienteForm (ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets ={
            'persona': forms.Select(attrs= {'class':'form-select rounded-pill'}),
            'categoria': forms.TextInput(attrs= {'type': 'number', 'class': 'form-control rounded-pill', 'placeholder': 'Ingrese Categoria', 'title': 'Ingrese su categoria'}),
            'fecha_alta': forms.DateInput(format= '%Y-%m-%d', attrs= {'type': 'date', 'class': 'form-control rounded-pill'})
        }

class MovimientoForm (ModelForm):
    class Meta:
        model = Movimiento
        fields = '__all__'
        widgets = {
            'tipo': forms.TextInput(attrs= {'type': 'text', 'class': 'form-control rounded-pill', 'placeholder': 'Ingrese tipo de Movimiento', 'title': 'Ingrese tipo de movimiento'}),
            'cliente': forms.Select(attrs= {'class': 'form-select rounded-pill'}),
            'numero': forms.TextInput(attrs= {'type': 'number', 'class': 'form-control rounded-pill','placeholder': 'Ingrese N° de Movimiento', 'title': 'Ingrese numero de movimiento'}),
            'fecha': forms.DateInput(format= '%Y-%m-%d', attrs= {'type': 'date', 'class': 'form-control rounded-pill'})
        }

class ArticuloForm (ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'
        widgets= {
            'id': forms.TextInput(attrs= {'type': 'number', 'class': 'form-control rounded-pill'}),
            'marca': forms.TextInput(attrs= {'type': 'text', 'class': 'form-control rounded-pill', 'placeholder': 'Ingrese Marca', 'title': 'Ingrese marca'}),
            'descripcion': forms.TextInput(attrs= {'type': 'text', 'class': 'form-control rounded-pill', 'placeholder': 'Ingrese Modelo', 'title': 'Ingrese modelo'}),
            'categoria': forms.TextInput( attrs= {'type': 'text', 'class': 'form-control rounded-pill','placeholder': 'Ingrese Categoria', 'title': 'Ingrese categoria'}),
            'stock': forms.TextInput(attrs= {'type': 'number', 'class': 'form-control rounded-pill', 'placeholder': 'Ingrese Stock', 'title': 'Ingrese stock'}),
            'precio': forms.TextInput(attrs= {'type': 'number', 'class': 'form-control rounded-pill', 'placeholder': 'Ingrese Precio', 'title': 'Ingrese precio'}),
            'disponible': forms.Select(attrs= {'class': 'form-select rounded-pill'}),
            'imagen': forms.FileInput (attrs={'type': 'file', 'class': 'form-control rounded-pill'})
        }

class ItemForm (ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets= {
            'articulo': forms.Select(attrs= {'class': 'form-select rounded-pill'}),
            'movimiento': forms.Select(attrs= {'class': 'form-select rounded-pill'}),
            'cantidad': forms.DateInput( attrs= {'type': 'number','class': 'form-control rounded-pill', 'placeholder': 'Ingrese Cantidad', 'title': 'Ingrese Cantidad'})
        }
