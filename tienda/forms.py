from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente, Producto, Empleado

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


#Forms tercer entregable

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