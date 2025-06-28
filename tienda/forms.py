from django import forms
from .models import Cliente, Producto, Empleado

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'correo']
        
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'informacion', 'precio']
        
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'puesto', 'dni']

class BuscarProductoFormulario(forms.Form):
    nombre = forms.CharField(label = "Nombre del producto", max_length=100)